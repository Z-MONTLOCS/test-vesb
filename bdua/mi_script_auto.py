
from .config_utils_auto import initialize_driver,seleccionar_tipo_documento_y_identificacion,download_captcha_image,solve_captcha_and_click_button,close_driver,switch_to_new_tab,get_data_table,get_affiliation_table,close_browser,extract_names






def ejecutar_mi_script_auto(datos):
    print("************ Incio ejecutar_mi_script_auto **************" )


    print("************ Linea 12 **************" )

    driver, client = initialize_driver()

    seleccionar_tipo_documento_y_identificacion(driver, datos)

  
    print("************ Linea 19  ejecutar_mi_script_auto **************" )

    while True:
            # Descargar la imagen del captcha y obtener su ruta
            captcha_file = download_captcha_image(driver)

          
            captcha = client.decode(captcha_file)

            if captcha:
                captcha_text = captcha["text"]
                texto_span = solve_captcha_and_click_button(driver, captcha_text)

                while "El codigo ingresado no es valido" in texto_span:
                    # El CAPTCHA no se resolvió correctamente, lo reportamos
                    print("CAPTCHA %s solved incorrectly: %s" % (captcha["captcha"], captcha["text"]))
                    client.report(captcha["captcha"])
                    # print("==================================")
                    # print(texto_span)
                    # print("==================================")

                    # Descargar la imagen del captcha y obtener su ruta
                    captcha_file = download_captcha_image(driver)

                    # Put your CAPTCHA file name or file-like object, and optional
                    # solving timeout (in seconds) here:
                    captcha = client.decode(captcha_file)
                    captcha_text = captcha["text"]
                    solve_captcha_and_click_button(driver, captcha_text)

                    # print("===============codigo===================")
                    # print(captcha_text)
                    # print("==================================")


                # El CAPTCHA se resolvió correctamente
                    print("CAPTCHA %s solved: %s" % (captcha["captcha"], captcha["text"]))
                    break  # Terminar el bucle si se resuelve correctamente

                else:
                    # No se pudo resolver el CAPTCHA
                    print("resuelto el CAPTCHA")
                    print(captcha_text)

                    close_driver(driver)


                    break  


    driver.switch_to.window(driver.window_handles[-1])
   
   

    switch_to_new_tab(driver)
    information = get_data_table(driver)


    affiliation_info = get_affiliation_table(driver)

    close_browser(driver)

  
    names_surnames_info = extract_names( information['NOMBRES'], information['APELLIDOS'])


   # Create the info dictionary with the assigned values
    info = {
    'first_name': names_surnames_info['first_name'],
    'middle_name': names_surnames_info['middle_name'],
    'last_name': names_surnames_info['first_surname'],
    'second_last_name': names_surnames_info['second_surname'],
    'eps': affiliation_info['EPS'] 
}


    # Mostrar los resultados
    print('Información:')
    print('Primer nombre:', info['first_name'])
    print('Segundo nombre:', info['middle_name'])
    print('Primer apellido:', info['last_name'])
    print('Segundo apellido:', info['second_last_name'])
    print('EPS:', info['eps'])   



    return info

