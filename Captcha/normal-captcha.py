from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import sys
from twocaptcha import TwoCaptcha
from config import API_KEY
from readexcel import get_cedulas
from readexcel import write_cedulas
from tkinter import messagebox
api_key = os.getenv('APIKEY_2CAPTCHA', API_KEY)
solver = TwoCaptcha(api_key)
#Abrir el excel y obtener la lista de las cédulas
cedulas = get_cedulas()
print(cedulas)
sizecedula = len(cedulas)

#Abrir el navegador y capturar cada cedula
messagebox.showinfo(message="Se iniciará el programa. Por favor, no cierre el navegador.", title="Inicio")
try:
    for i in range(sizecedula):
        browser = webdriver.Chrome()
        browser.get('https://www.senescyt.gob.ec/consulta-titulos-web/faces/vista/consulta/consulta.xhtml')

        captcha_img = browser.find_element(By.ID, 'formPrincipal:capimg')
        captcha_img.screenshot('Captcha/imagenes/captchas/captcha'+cedulas[i]+'.png')
        try:
            result = solver.normal('Captcha/imagenes/captchas/captcha'+cedulas[i]+'.png')

        except Exception as e:
            print(e)
        else:
            code = result['code']
            browser.find_element(By.ID, 'formPrincipal:identificacion').send_keys(cedulas[i])
            browser.find_element(By.ID, 'formPrincipal:captchaSellerInput').send_keys(code)
            submit_button = browser.find_element(By.ID, 'formPrincipal:boton-buscar').click()
            time.sleep(1)
            msgrojo = []
            errorchar = []
            try:
                msgrojo.append(browser.find_element(By.CLASS_NAME , 'msg-rojo'))
                errorchar.append(browser.find_element(By.CLASS_NAME, 'ui-messages-error-summary'))
            except NoSuchElementException:  #spelling error making this code not work as expected
                pass
            finally: 
                if len(msgrojo) > 0:
                    browser.maximize_window()
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    browser.save_screenshot('Captcha/imagenes/screenshots/'+cedulas[i]+'_VERIFICAR_CEDULA'+'.png')
                    msgrojo = []
                    msg = write_cedulas('fallo', i)
                elif len(errorchar) > 0:
                    i = i-1
                    browser.maximize_window()
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    browser.save_screenshot('Captcha/imagenes/screenshots/'+cedulas[i]+'.png')
                    errorchar = []
                else:
                    browser.maximize_window()
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    browser.save_screenshot('Captcha/imagenes/screenshots/'+cedulas[i]+'.png')
                    msg = write_cedulas('exito', i)
        time.sleep(1)
    messagebox.showinfo(message="Se finalizó el programa. Gracias por la espera", title="Fin")
    sys.exit()
except Exception as e:
    messagebox.showinfo(message="Cerró el programa, ejecútelo nuevamente", title="Error")
    
