from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import undetected_chromedriver as uc
import time

# Ruta del controlador de Chrome
path = 'C:/Users/chromedriver-win64/chromedriver.exe'

# Configurar el servicio del controlador
service = Service(path)

# Inicializar el controlador de Chrome
driver = webdriver.Chrome(service=service)

# Sitio web donde se encuentra el elemento
website = 'https://aplicaciones.adres.gov.co/bdua_internet/Pages/ConsultarAfiliadoWeb.aspx'
driver.get(website)

# Seleccionar el elemento <select> por su id
elemento_select = Select(driver.find_element(By.ID, 'tipoDoc'))

# Seleccionar la opción 'NT' en el elemento <select>
elemento_select.select_by_value('CC')  # El valor '4' corresponde a la opción 'NT'

# Buscar el elemento por su id
elemento_input = driver.find_element(By.ID, 'txtNumDoc')

# Escribir el valor "1130608129" en el campo de entrada
elemento_input.send_keys('1130608129')

# Buscar el elemento por su id
elemento_input = driver.find_element(By.ID, 'btnConsultar')
time.sleep(10)

# Hacer clic en el botón
elemento_input.click()

# Esperar un tiempo razonable para que la nueva pestaña se abra y se cargue

# Cambiar el enfoque del controlador a la nueva pestaña
driver.switch_to.window(driver.window_handles[-1])

# Obtener la tabla que contiene los datos
tabla_datos = driver.find_element(By.ID, 'GridViewBasica')

# Crear un objeto para almacenar la información
informacion = {}

# Obtener todos los elementos <tr> dentro de la tabla
filas = tabla_datos.find_elements(By.TAG_NAME, 'tr')

# Recorrer las filas de la tabla y extraer las claves y valores
for fila in filas:
    # Obtener todos los elementos <td> dentro de la fila
    celdas = fila.find_elements(By.TAG_NAME, 'td')
    # Si hay dos celdas, guardar la información en el objeto clave-valor
    if len(celdas) == 2:
        clave = celdas[0].text
        valor = celdas[1].text
        informacion[clave] = valor





# Obtener la segunda tabla que contiene los datos de afiliación
tabla_afiliacion = driver.find_element(By.ID, 'GridViewAfiliacion')

# Crear un objeto para almacenar la información de afiliación
informacion_afiliacion = {}

# Obtener todos los elementos <tr> dentro de la tabla de afiliación
filas_afiliacion = tabla_afiliacion.find_elements(By.TAG_NAME, 'tr')

# Recorrer las filas de la tabla de afiliación y extraer las claves y valores
for fila_afiliacion in filas_afiliacion:
    # Obtener todos los elementos <td> dentro de la fila de afiliación
    celdas_afiliacion = fila_afiliacion.find_elements(By.TAG_NAME, 'td')
    # Si hay seis celdas, guardar la información en el objeto clave-valor
    if len(celdas_afiliacion) == 6:
        estado = celdas_afiliacion[0].text
        entidad = celdas_afiliacion[1].text
        regimen = celdas_afiliacion[2].text
        fecha_efectiva = celdas_afiliacion[3].text
        fecha_finalizacion = celdas_afiliacion[4].text
        tipo_afiliado = celdas_afiliacion[5].text
        informacion_afiliacion['ESTADO'] = estado
        informacion_afiliacion['ENTIDAD'] = entidad
        informacion_afiliacion['REGIMEN'] = regimen
        informacion_afiliacion['FECHA DE AFILIACIÓN EFECTIVA'] = fecha_efectiva
        informacion_afiliacion['FECHA DE FINALIZACIÓN DE AFILIACIÓN'] = fecha_finalizacion
        informacion_afiliacion['TIPO DE AFILIADO'] = tipo_afiliado

# Mostrar el objeto clave-valor de afiliación por consola

print(informacion)

print(informacion_afiliacion)

# Tomar una captura de pantalla de la página resultante de la nueva pestaña y guardarla en un archivo llamado "captura.png"
#driver.save_screenshot("captura.png")

# Cerrar el controlador de Chrome
driver.quit()        
