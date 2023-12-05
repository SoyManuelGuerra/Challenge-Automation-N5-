# utils/TestFunctions.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class SingletonNavegadorWeb:
    _instancia = None

    @staticmethod
    def obtener_instancia(opciones_adicionales=None):
        """
        Obtiene una instancia única del WebDriver de Chrome. Si la instancia ya existe, devuelve la existente.
        Se pueden proporcionar opciones adicionales de Chrome para configuraciones personalizadas.

        Args:
        - opciones_adicionales (webdriver.ChromeOptions, optional): Configuraciones adicionales para el navegador Chrome.

        Returns:
        - webdriver.Chrome: Una instancia del navegador Chrome.
        """
        if SingletonNavegadorWeb._instancia is None:
            opciones = webdriver.ChromeOptions()
            opciones.add_experimental_option('excludeSwitches', ['enable-page-load-metrics'])  # Desactivar las métricas de carga de la página para evitar un error de Chrome y tener una salida más limpia.
            opciones.add_argument('--log-level=3')  # Desactivar logs de level 3 o inferior para evitar mensajes de advertencia y tener una salida más limpia.
            if opciones_adicionales:
                for opcion in opciones_adicionales:
                    opciones.add_argument(opcion)
            servicio = ChromeService(ChromeDriverManager().install())
            SingletonNavegadorWeb._instancia = webdriver.Chrome(service=servicio, options=opciones)
            SingletonNavegadorWeb._instancia.maximize_window()  # Maximizar navegador al crear la instancia.
        return SingletonNavegadorWeb._instancia
    
    @staticmethod
    def cerrar_instancia():
        """
        Cierra la instancia del navegador Chrome y libera recursos.
        """
        if SingletonNavegadorWeb._instancia:
            SingletonNavegadorWeb._instancia.quit()
            SingletonNavegadorWeb._instancia = None
