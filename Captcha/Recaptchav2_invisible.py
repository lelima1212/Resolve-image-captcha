from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from twocaptcha import TwoCaptcha
from config import API_KEY
from readexcel import get_ruc

api_key = os.getenv('APIKEY_2CAPTCHA', API_KEY)
solver = TwoCaptcha(api_key)
#Abrir el excel y obtener la lista de rucs
rucs = get_ruc()
print(rucs)
sizeruc = len(rucs)

#Abrir el navegador y capturar cada ruc
'''for i in range(sizeruc):
    browser = webdriver.Chrome()
    browser.get('https://www.senescyt.gob.ec/consulta-titulos-web/faces/vista/consulta/consulta.xhtml')

    captcha_img = browser.find_element(By.ID, 'formPrincipal:capimg')
    captcha_img.screenshot('Captcha/imagenes/captchas/captcha'+rucs[i]+'.png')
    try:
        result = solver.normal('Captcha/imagenes/captchas/captcha'+rucs[i]+'.png')

    except Exception as e:
        print(e)
    else:
        code = result['code']
        browser.find_element(By.ID, 'formPrincipal:identificacion').send_keys(rucs[i])
        browser.find_element(By.ID, 'formPrincipal:captchaSellerInput').send_keys(code)
        submit_button = browser.find_element(By.ID, 'formPrincipal:boton-buscar').click()
        time.sleep(1)
        msgrojo = [1]
        errorchar = [1]
        try:
            msgrojo[0] = browser.find_element(By.CLASS_NAME , 'msg-rojo')
            errorchar[0] = browser.find_element(By.CLASS_NAME, 'ui-messages-error-summary')
        except NoSuchElementException:  #spelling error making this code not work as expected
            msgrojo = []
            errorchar = []
            pass 
        if len(msgrojo) > 0 and msgrojo[0].is_displayed():
            browser.maximize_window()
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            browser.save_screenshot('Captcha/imagenes/screenshots/'+rucs[i]+'VERIFICAR_CEDULA'+'.png')
            msgrojo = []
        elif len(errorchar) > 0 and errorchar[0].is_displayed():
            i -= 1
            browser.maximize_window()
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            browser.save_screenshot('Captcha/imagenes/screenshots/screenie'+rucs[i]+'.png')
            errorchar = []
        else:
            browser.maximize_window()
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            browser.save_screenshot('Captcha/imagenes/screenshots/screenie'+rucs[i]+'.png')
    time.sleep(2)'''

