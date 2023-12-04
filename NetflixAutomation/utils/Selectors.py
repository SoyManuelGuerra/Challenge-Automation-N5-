from selenium.webdriver.common.by import By

class Selectores:
    """
    Contiene los selectores de los elementos de la página web.
    """
# --- Selectores del Home de Netflix ---
    INICIAR_SESION = (By.XPATH, "//a[text()='Iniciar sesión']") # Selector del botón 'Iniciar sesión'