from twocaptcha import TwoCaptcha
API_KEY = ''

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
