"""
ServiceRegistry — хранит состояние всех сервисов:
- сколько раз успешно/неудачно использован
- последний статус (работает/нет)
- авто-отключение мёртвых
"""
import json
import os
import time
import random
import threading

REGISTRY_FILE = "service_registry.json"

_lock = threading.Lock()
_registry = {}

def _load():
    global _registry
    try:
        with open(REGISTRY_FILE) as f:
            _registry = json.load(f)
    except:
        _registry = {}

def _save():
    with open(REGISTRY_FILE, 'w') as f:
        json.dump(_registry, f, indent=2)

def get_key(service):
    """Уникальный ключ для сервиса — URL + method"""
    return f"{service['method']}:{service['url']}"

def record_result(service, success=True, response_time=0):
    """Записать результат работы сервиса"""
    key = get_key(service)
    _load()
    now = time.time()
    if key not in _registry:
        _registry[key] = {
            "website": service['info']['website'],
            "attack": service['info']['attack'],
            "country": service['info']['country'],
            "hits": 0,
            "fails": 0,
            "last_ok": 0,
            "last_fail": 0,
            "enabled": True,
            "avg_response": 0,
            "response_count": 0,
        }
    s = _registry[key]
    s['hits'] += 1
    if success:
        s['last_ok'] = now
        s['avg_response'] = (s['avg_response'] * s['response_count'] + response_time) / (s['response_count'] + 1)
        s['response_count'] += 1
    else:
        s['fails'] += 1
        s['last_fail'] = now
        # Авто-отключение при 5+ неудачах подряд
        total = s['hits'] + s['fails']
        if total >= 5 and (s['fails'] / total) > 0.7:
            s['enabled'] = False
    _save()

def is_enabled(service):
    """Проверить, включён ли сервис"""
    key = get_key(service)
    _load()
    s = _registry.get(key)
    if s is None:
        return True
    return s.get('enabled', True)

def get_stats():
    """Получить общую статистику"""
    _load()
    total = len(_registry)
    enabled = sum(1 for s in _registry.values() if s.get('enabled', True))
    working = sum(1 for s in _registry.values() if s.get('last_ok', 0) > s.get('last_fail', 0))
    return {
        "total": total,
        "enabled": enabled,
        "working": working,
        "dead": total - working,
    }

def get_summary_text():
    """Текстовый отчёт для бота"""
    _load()
    stats = get_stats()
    
    by_type = {}
    for s in _registry.values():
        atype = s.get('attack', '?')
        if atype not in by_type:
            by_type[atype] = {'total': 0, 'enabled': 0, 'hits': 0}
        by_type[atype]['total'] += 1
        if s.get('enabled', True):
            by_type[atype]['enabled'] += 1
        by_type[atype]['hits'] += s.get('hits', 0)
    
    text = f"📊 **Статистика сервисов**\n\n"
    text += f"Всего в базе: {stats['total']}\n"
    text += f"Активно: {stats['enabled']}\n"
    text += f"Рабочие: {stats['working']}\n"
    text += f"Мёртвые: {stats['dead']}\n\n"
    
    for atype, data in by_type.items():
        text += f"▪️ **{atype}**: {data['enabled']}/{data['total']} | запросов: {data['hits']}\n"
    
    return text

def reset_stats():
    """Сбросить всю статистику"""
    global _registry
    _registry = {}
    _save()

def enable_all():
    """Включить все сервисы"""
    _load()
    for s in _registry.values():
        s['enabled'] = True
    _save()

def list_dead_services():
    """Список мёртвых сервисов"""
    _load()
    dead = []
    for key, s in _registry.items():
        if not s.get('enabled', True):
            dead.append(f"  {s['website']} — {s['fails']}/{s['hits']+s['fails']} ошибок")
    return dead
