"""
Поиск по номеру телефона — пробив через открытые API.
Результат: имя, соцсети, оператор, регион.
"""
def lookup_urls(number):
    return [
        # GetContact — определяет имя
        {
            'info': {'country': 'ALL', 'attack': 'LOOKUP', 'website': 'GetContact.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.getcontact.com/v2/search',
            'data': {'phone': number},
        },
        # Karma — кто звонил
        {
            'info': {'country': 'RU', 'attack': 'LOOKUP', 'website': 'Karma.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.karma.ru/v1/phones',
            'data': {'phone': number},
        },
        # ЦБ РФ — проверка номера в мошеннических базах
        {
            'info': {'country': 'RU', 'attack': 'LOOKUP', 'website': 'CBR.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://cbr.ru/api/phone-check',
            'params': {'phone': number},
        },
        # Номер — оператор и регион
        {
            'info': {'country': 'RU', 'attack': 'LOOKUP', 'website': 'PhoneInfo.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://phoneinfo.ru/api',
            'params': {'phone': number},
        },
        # Прозвон — проверка базы
        {
            'info': {'country': 'RU', 'attack': 'LOOKUP', 'website': 'ProZvon.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://prozvon.ru/api/check',
            'data': {'phone': number},
        },
        # SocialFinder
        {
            'info': {'country': 'ALL', 'attack': 'LOOKUP', 'website': 'SocialFinder.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://socialfinder.com/api/search',
            'data': {'phone': number},
        },
        # Facebook search
        {
            'info': {'country': 'ALL', 'attack': 'LOOKUP', 'website': 'Facebook.com', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://www.facebook.com/search/top',
            'params': {'q': number},
        },
        # VK search
        {
            'info': {'country': 'RU', 'attack': 'LOOKUP', 'website': 'VK.com', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://vk.com/search',
            'params': {'c[q]': number, 'c[section]': 'people'},
        },
        # OK search
        {
            'info': {'country': 'RU', 'attack': 'LOOKUP', 'website': 'OK.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://ok.ru/search',
            'params': {'st.query': number},
        },
        # FindClone
        {
            'info': {'country': 'ALL', 'attack': 'LOOKUP', 'website': 'FindClone.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://findclone.ru/register',
            'params': {'phone': '+' + number},
        },
        # TrueCaller API
        {
            'info': {'country': 'ALL', 'attack': 'LOOKUP', 'website': 'TrueCaller.com', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://api.truecaller.com/v1/search',
            'params': {'phone': number},
        },
    ]
