from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from deathbycaptcha import HttpClient
from selenium.webdriver.common.by import By
import requests
import os
import time
import selenium


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# selenium 4
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import logging













def initialize_driver():

   


    #CHROMEDRIVER_PATH = "/opt/render/project/bin/chromedriver"  

    #CHROME_PATH="/opt/render/project/bin/chrome-linux64"  # Ruta donde se instala Chrome





      
    print("=======================================")
    print("Inicializado:")
    print("*******************************************")


    try:
        
        print("=======================================")
        print("Versión de Selenium:", selenium.__version__)
        print("*******************************************")



      
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")  
        options.add_argument("--disable-extensions") 
        options.add_argument("--disable-dev-shm-usage");
        options.add_argument("--disable-gpu")
        # Inicializar el controlador de Chrome


        CHROMEDRIVER_PATH="/opt/render/project/bin/chromedriver-linux64"  
        print("************************Linea 73 *******************")

        driver = webdriver.Chrome(CHROMEDRIVER_PATH)
        print("************************Linea 76 *******************")

        service = Service(executable_path=CHROMEDRIVER_PATH)

        print("************************Linea 79 *******************")


        driver = webdriver.Chrome( options=options)
        print("************************Linea 84 *******************")

        #driver = webdriver.Chrome(options=options)

        

            

        # URL del sitio web
        website = 'https://aplicaciones.adres.gov.co/bdua_internet/Pages/ConsultarAfiliadoWeb.aspx'
        driver.get(website)

        # Configuración de cliente DeathByCaptcha
        username = "zyrivic"
        password = "5RL:6dRdfadS#Hc"
        client = HttpClient(username, password)

        # Esperar a que cierto elemento esté presente en la página para verificar si la carga fue exitosa
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, 'btnConsultar'))
            )

            print("Página cargada correctamente.")
        except Exception as e:
            print("Error al cargar la página:", e)
            driver.quit()
            raise

        return driver, client
    except Exception as e:
        print("Error al inicializar el controlador:", e)
        raise














def seleccionar_tipo_documento_y_identificacion(driver, datos):
    document_type = datos.get('document_type')
    identification_number = datos.get('identification_number')

    #Imprimir los datos en la consola
    print("============Datos recibidos desde Angular=================")
    print(" ")
    print("Tipo de documento:", document_type)
    print("Número de identificación:", identification_number)
    print("=================================================")
    print(" ")  
    # Seleccionar el elemento <select> por su id
    elemento_select = Select(driver.find_element(By.ID, 'tipoDoc'))
    elemento_select.select_by_value(document_type)

    # Buscar el elemento por su id
    elemento_input = driver.find_element(By.ID, 'txtNumDoc')
    elemento_input.send_keys(identification_number)



def download_captcha_image(driver):
    # Encontrar el elemento img por su ID
    elemento_img = driver.find_element(By.ID, 'Capcha_CaptchaImageUP')

    # Obtener la URL de la imagen
    url_imagen = elemento_img.get_attribute('src')

    # Descargar la imagen usando la librería requests
    response = requests.get(url_imagen)

    # Verificar si la descarga fue exitosa
    if response.status_code == 200:
        # Directorio donde se guardará la imagen
        directorio_guardado = 'C:/test-vesb/test-bakend-api-env-phyton/bdua'

        # Nombre de archivo para la imagen
        nombre_archivo = 'imagen_captcha.png'

        # Ruta completa del archivo
        ruta_archivo = os.path.join(directorio_guardado, nombre_archivo)

        # Guardar la imagen en el directorio especificado
        with open(ruta_archivo, 'wb') as archivo:
            archivo.write(response.content)

        # print(f'Imagen guardada en: {ruta_archivo}')
    else:
        print('Error al descargar la imagen')

    captcha_file = ruta_archivo  # Devolver la ruta completa del archivo de imagen
    return captcha_file
   


def solve_captcha_and_click_button(driver, captcha_text):
    # Buscar el elemento por su id y enviar el texto del captcha
    elemento_input = driver.find_element(By.ID, 'Capcha_CaptchaTextBox')
    elemento_input.send_keys(captcha_text)

    # Buscar el elemento por su id
    elemento_input = driver.find_element(By.ID, 'btnConsultar')

    # Esperar antes de hacer clic en el botón (ajusta el tiempo según sea necesario)
    time.sleep(2)

    # Hacer clic en el botón
    elemento_input.click()

    # Esperar después de hacer clic en el botón (ajusta el tiempo según sea necesario)
    time.sleep(2)

    # Encontrar el elemento span por su id
    elemento_span = driver.find_element(By.ID, 'Capcha_ctl00')

    # Obtener el texto del elemento span
    texto_span = elemento_span.text

    # Imprimir el texto
    # print(texto_span)

    return texto_span




def click_send(driver):
    # Buscar el elemento por su id
    elemento_input = driver.find_element(By.ID, 'btnConsultar')
    
    # Esperar antes de hacer clic en el botón
    time.sleep(8)

    # Hacer clic en el botón
    elemento_input.click()

def close_driver(driver):
    # Cerrar el controlador de Chrome
    driver.close()    




def switch_to_new_tab(driver):
    driver.switch_to.window(driver.window_handles[-1])    

def get_data_table(driver):
    data_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'GridViewBasica'))
    )
    
    data_info = {}
    rows = data_table.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) == 2:
            key = cells[0].text
            value = cells[1].text
            data_info[key] = value
    
    return data_info


def get_affiliation_table(driver):
    affiliation_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'GridViewAfiliacion'))
    )
    
    affiliation_info = {}
    affiliation_rows = affiliation_table.find_elements(By.TAG_NAME, 'tr')
    for affiliation_row in affiliation_rows:
        affiliation_cells = affiliation_row.find_elements(By.TAG_NAME, 'td')
        if len(affiliation_cells) == 6:
            status = affiliation_cells[0].text
            entity = affiliation_cells[1].text
            regime = affiliation_cells[2].text
            effective_date = affiliation_cells[3].text
            end_date = affiliation_cells[4].text
            affiliate_type = affiliation_cells[5].text
            affiliation_info['Status'] = status
            affiliation_info['EPS'] = entity
            affiliation_info['Regime'] = regime
            affiliation_info['Effective Date'] = effective_date
            affiliation_info['End Date'] = end_date
            affiliation_info['Affiliate Type'] = affiliate_type
    
    return affiliation_info

def close_browser(driver):
    driver.quit()



def extract_names(name, last_name):
    names_list = name.split()
    surnames_list = last_name.split()

    first_name = names_list[0] if names_list else None
    middle_name = ' '.join(names_list[1:]) if len(names_list) > 1 else None
    first_surname = surnames_list[0] if surnames_list else None
    second_surname = ' '.join(surnames_list[1:]) if len(surnames_list) > 1 else None

    names_surnames_info = {
        'first_name': first_name,
        'middle_name': middle_name,
        'first_surname': first_surname,
        'second_surname': second_surname
    }

    return names_surnames_info 
