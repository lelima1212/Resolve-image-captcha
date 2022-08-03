from twocaptcha import TwoCaptcha
API_KEY = '4f098de090a5156bdec28cc240725c2b'

config = {
            'server':           '2captcha.com',
            'apiKey':           'API_KEY',
            'softId':            123,
            'callback':         'https://www.senescyt.gob.ec/web/guest/consultas',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }
solver = TwoCaptcha(**config)