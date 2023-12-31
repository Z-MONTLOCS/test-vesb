from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time
import requests
import os








# def initialize_driver():
#     path = 'C:/Users/chromedriver-win64/chromedriver.exe'
#     service = Service(path)

#     # Inicializar el controlador de Chrome
#     driver = webdriver.Chrome(service=service)


#     # chrome_options = webdriver.ChromeOptions()
#     # chrome_options.add_argument('--headless')  # Agregar la opción headless
#     # driver = webdriver.Chrome(service=service, options=chrome_options)

#     # Sitio web donde se encuentra el elemento
#     website = 'https://aplicaciones.adres.gov.co/bdua_internet/Pages/ConsultarAfiliadoWeb.aspx'
#     driver.get(website)

   

#     return driver




def initialize_driver():
    path = 'C:/Users/chromedriver-win64/chromedriver.exe'
    service = Service(path)

    try:
        # Inicializar el controlador de Chrome
        driver = webdriver.Chrome(service=service)

       

        # Sitio web donde se encuentra el elemento
        website = 'https://aplicaciones.adres.gov.co/bdua_internet/Pages/ConsultarAfiliadoWeb.aspx'
        driver.get(website)

        # Esperar a que cierto elemento esté presente en la página para verificar si la carga fue exitosa
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'btnConsultar'))


            )

            
            #      # Ocultar el botón utilizando JavaScript
            # hide_script = "document.getElementById('btnConsultar').style.display   = 'none';"
            # driver.execute_script(hide_script)


            
           
            print("Página cargada correctamente.")
        except Exception as e:
            print("Error al cargar la página:", e)
            driver.quit()
            raise

        return driver
    except Exception as e:
        print("Error al inicializar el controlador:", e)
        raise





def seleccionar_tipo_documento_y_identificacion(driver, datos):
    document_type = datos.get('document_type')
    identification_number = datos.get('identification_number')

    #Imprimir los datos en la consola
    print("============Datos recibidos Cliente=================")
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

    
    # elemento_input = driver.find_element(By.ID, 'btnConsultar')
    # time.sleep(8)

    #         # Hacer clic en el botón
    # elemento_input.click()

    # driver.close()



def click_send(driver):
    # Buscar el elemento por su id
    elemento_input = driver.find_element(By.ID, 'btnConsultar')
    
    # Esperar antes de hacer clic en el botón
    time.sleep(3)

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


























 
