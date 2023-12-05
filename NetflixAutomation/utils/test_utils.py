# -*- coding: utf-8 -*-
# utils/TestFunctions.py
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class FuncionesBase:
    """
    Contiene funciones base para el manejo de los elementos de la pagina web
    y proporciona un punto de entrada para las funciones de prueba.
    """

# --- Constructor y configuraciones iniciales del driver ---
    def __init__(self, controlador):
        self.controlador = controlador
        
# --- Funciones de manejo de esperas ---

    # ---Esperas explicitas  ---      
    def esperar_elemento(self, selector, tipo_espera=None, tiempo_espera=10):
        """
        Método de utilidad para esperar a que un elemento cumpla con ciertas condiciones.
        Lanza una excepción con un mensaje personalizado si no se encuentra el elemento o si hay algún otro problema.

        Args:
        - selector (tuple): Selector del elemento (tipo, valor).
        - tipo_espera (list, optional): Lista de tipos de espera ('presencia', 'visibilidad', 'clickeable'). Si es None, se consideran todos.
        - tiempo_espera (int, optional): Tiempo máximo de espera en segundos. Por defecto es 30 segundos.

        Returns:
        - WebElement: Elemento que cumple con las condiciones.

        Ejemplo de uso:
        boton = self.esperar_elemento((By.ID, 'botonSubmit'), tipo_espera=['clickeable'])
        boton.click()
        """

        if tipo_espera is None:
            tipo_espera = ['presencia', 'visibilidad', 'clickeable']

        condiciones = {
            'presencia': EC.presence_of_element_located,
            'visibilidad': EC.visibility_of_element_located,
            'clickeable': EC.element_to_be_clickable
        }

        tipo_error = {
            TimeoutException: "no se encontró o no estuvo listo en el tiempo esperado",
            NoSuchElementException: "no se encontró",
            ElementNotInteractableException: "no es interactuable"
        }

        espera = WebDriverWait(self.controlador, tiempo_espera)
        elemento = None

        for condicion in tipo_espera:
            if condicion not in condiciones:
                raise ValueError(f"Condición no reconocida: {condicion}")

            try:
                if not elemento:
                    elemento = espera.until(condiciones[condicion](selector))
                else:
                    espera.until(condiciones[condicion](selector))
            except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
                mensaje = f"El elemento {selector} {tipo_error[type(e)]} (condición: {condicion})."
                raise AssertionError(mensaje) from e

        return elemento

    # ---Esperas implicitas  --- 
    def configurar_espera_implicita(self, tiempo_espera=10):
        """
        Configura el tiempo de espera implícita para todas las operaciones de búsqueda de elementos.

        Args:
        - tiempo_espera (int): Tiempo de espera en segundos.
        """
        self.controlador.implicitly_wait(tiempo_espera)

# --- Funciones de navegación ---

    def navegar_a(self, url):
        """
        Navega a la URL especificada.

        Args:
        - url (str): URL a la que se desea navegar.
        """
        self.controlador.get(url)
        
    def obtener_titulo(self):
        """
        Obtiene y retorna el título de la página actual.
        """
        return self.controlador.title
    
    def obtener_url(self):
        """
        Obtiene y retorna la URL de la página actual.
        """
        return self.controlador.current_url