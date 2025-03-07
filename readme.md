# Reserva automática de refugios con Selenium

Este es un script en Python que automatiza la reserva de refugios en la web del Govern Balear utilizando Selenium. El script busca disponibilidad, selecciona la fecha y rellena el formulario con los datos proporcionados. Sin embargo, no completa el pago, ya que la página bloquea la fecha seleccionada durante 30 minutos para que el usuario pueda finalizar el proceso manualmente.

## Requisitos

### Instalación de dependencias
Asegúrate de tener instalado Python 3.11.9. Luego, instala las librerías necesarias ejecutando:

```sh
pip install selenium
```

### Geckodriver
El script usa Firefox como navegador y requiere `geckodriver.exe`, que ya está incluido en el repositorio. No necesitas instalarlo aparte.

## Uso

El script está diseñado para modificar directamente las variables dentro del código en caso de querer cambiar los datos del formulario. Sin embargo, se podría modificar para recibir parámetros en la ejecución.

Para ejecutar el script:

```sh
python script.py
```

## Parámetros utilizados
El script necesita los siguientes datos, en el archivo main.py vienen declarados como variables al principio del programa, se pueden modificar ahí:

- **check_stock:**
  - Refugio a reservar
  - Número de visitantes
- **select_day:**
  - Número de huéspedes mayores de edad (para la ecotasa de 1€ por persona +18)
- **fill_form:**
  - Nombre, apellidos, fecha de nacimiento, DNI y fecha de expedición del DNI
  - Número de teléfono y email
  - Matrícula (opcional)

## Cómo funciona el script

1. **check_stock(driver):** Selecciona el refugio, el número de huéspedes y la cantidad de noches. Luego, comprueba la disponibilidad recargando la página cada segundo hasta encontrar una fecha libre.
2. **select_day(driver):** Una vez encontrada la disponibilidad, selecciona el número de adultos para la ecotasa y avanza al formulario.
3. **fill_form(driver):** Rellena automáticamente los datos personales, acepta las condiciones y avanza hasta la sección de pago (donde el usuario debe finalizar manualmente).

## Posibles errores y soluciones

- **Error al encontrar elementos en la página:** Asegúrate de que la página no ha cambiado su estructura HTML. En caso de fallos, inspecciona los selectores de los elementos y ajústalos.
- **Problemas con Geckodriver:** Si el script no encuentra Geckodriver, asegúrate de que el archivo `geckodriver.exe` está en la misma carpeta que el script.
- **Permisos en Linux/Mac:** Si usas un sistema Unix, puede que necesites dar permisos de ejecución a Geckodriver:
  

  ```sh
  chmod +x geckodriver
  ```

## Adaptación a otros navegadores

El script está diseñado para Firefox, pero se puede adaptar a otros navegadores cambiando `webdriver.Firefox()` por `webdriver.Chrome()` (Chrome) o `webdriver.Edge()` (Edge) y asegurándose de usar el driver correspondiente.

---

Este proyecto ha sido desarrollado por Noah Catalán Rosell como un ejercicio personal de automatización con Selenium.

