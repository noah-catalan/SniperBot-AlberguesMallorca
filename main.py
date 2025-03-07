from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Se ha de introducir los siguientes campos:
    # check_stock:
        # Refugio a reservar
        # Número de visitantes

    # select_day
        # Cantidad de huéspedes mayores de edad (para la ecotasa de 1€ por persona +18)

    # fill_form
        # Se da por hecho que el documento es NIF y la nacionalidad española

        # Nombre, apellido1 y apellido2
        # Fecha de nacimiento, DNI y fecha de expedición del DNI
        # Número de telefono y email
        # Matrícula

refugio = "Coma de Binifaldó"
numero_huespedes = "2"

# No he probado a poner más noches
noches = "1"

huespedes_mayoria_edad = "2"

nombre = "Noah"
apellido1 = "Catalán"
apellido2 = "Rosell"
fecha_nacimiento = "22/09/2005"
dni = "49613235G"
fecha_expedicion = "19/04/2022"
telefono = "666035940"
email = "n.catalros@gmail.com"

acceso_vehiculos = False
matricula = "1234ABC"

url_albergues = "https://www.caib.es/albergsfront"




def main():
    driver = webdriver.Firefox()
    driver.get(url_albergues)

    check_stock(driver)
    select_day(driver)
    fill_form(driver)

def check_stock(driver):
    # Seleccionar el refugio
    select_refugio = Select(driver.find_element(By.ID, "seleccion.idRefugio"))
    select_refugio.select_by_visible_text(refugio)

    # Seleccionar numero de huespedes
    select_visitantes = Select(driver.find_element(By.ID, "seleccion.visitantes"))
    select_visitantes.select_by_visible_text(numero_huespedes)

    # Seleccionar noches
    select_noches = Select(driver.find_element(By.ID, "seleccion.noches"))
    select_noches.select_by_visible_text(noches)

    driver.find_element(By.CLASS_NAME, "p-button").click()

    # Comprobar disponibilidad

    while True:
        elementos = driver.find_elements(By.CLASS_NAME, "disponible")  # Buscar elementos con la clase

        if elementos:  # Si encuentra al menos un elemento, sale del bucle
            print("¡Hay disponibilidad!")
            break

        print("No hay disponibilidad. Esperando 1 segundo y recargando...")
        sleep(1)  # Esperar 1 segundo
        driver.refresh()  # Recargar la página

def select_day(driver):

    # Una vez encontrada la plaza libre la seleccionamos

    driver.find_element(By.CLASS_NAME, "disponible").click()

    # Cantidad de mayores de edad (ecotasa)
    select_ecotasa = Select(driver.find_element(By.ID, "ecotasa.visitantesMayores"))
    select_ecotasa.select_by_visible_text(huespedes_mayoria_edad)

    driver.find_element(By.CLASS_NAME, "p-button-primary").click()

def fill_form(driver):
    # Rellenamos el formulario

    select_documento = Select(driver.find_element(By.ID, "responsable.tipoDocumento"))
    select_documento.select_by_visible_text("NIF")
    select_nacionalidad = Select(driver.find_element(By.ID, "responsable.nacionalidad"))
    select_nacionalidad.select_by_visible_text("ESPAÑA")

    # Nombre y apellidos
    driver.find_element(By.ID, "responsable.nombre").send_keys(nombre)
    driver.find_element(By.ID, "responsable.primerApellido").send_keys(apellido1)
    driver.find_element(By.ID, "responsable.segundoApellido").send_keys(apellido2)

    # Fecha de nacimiento y DNI
    driver.find_element(By.ID, "responsable.fechaNacimiento").send_keys(fecha_nacimiento)
    driver.find_element(By.ID, "responsable.numeroDocumento").send_keys(dni)
    driver.find_element(By.ID, "responsable.fechaExpedicionDocumento").send_keys(fecha_expedicion)

    # Contacto: teléfono y mail
    driver.find_element(By.ID, "contacto.telefono1").send_keys(telefono)
    driver.find_element(By.ID, "contacto.email").send_keys(email)

    # Aceptar condiciones
    driver.find_element(By.ID, "obligacionesVisitantes").click()
    driver.find_element(By.ID, "veracidad").click()
    driver.find_element(By.ID, "covid").click()

    driver.find_element(By.ID, "condicionesGenerales").click()
    driver.find_element(By.CLASS_NAME, "ui-button").click()

    # Matrícula
    if acceso_vehiculos:
        driver.find_element(By.ID, "matricula_1").send_keys(matricula)

    driver.find_element(By.XPATH, '//button[@title="Pagament"]').click()
    driver.find_element(By.XPATH, '//button[span[text()="Anar al pagament"]]').click()

if __name__=="__main__":
    main()
