# tests/netflix_home.py
from pages.NetflixHomePage import NetflixHomePage
from utils.selectors import Selectores

def test_acceso_a_netflix(navegador_web):
    # Crear una instancia de la página de inicio de Netflix
    netflix_home = NetflixHomePage(navegador_web)
    netflix_home.configurar_espera_implicita(10)  # Configurar espera implícita de 10 segundos
    
    try:
        # Navegar a la página de inicio de Netflix o a la URL proporcionada
        netflix_home.ir_a_home()

        # Utilizar espera explícita para verificar que el boton "Iniciar Sesion" se encuentra antes de obtener el título y la URL
        netflix_home.esperar_elemento(Selectores.INICIAR_SESION, tipo_espera=['visibilidad', 'presencia'])

        # Obtener e imprimir el título y la URL de la página
        titulo = netflix_home.obtener_titulo() # Obtener el título de la página
        url = netflix_home.obtener_url() # Obtener la URL de la página
        print(f"Título de la página: {titulo}") # Imprimir el título de la página
        assert url == "https://www.netflix.com/ar/", f"Ha sido direccionado a una URL incorrecta: {url}" # Verificar que la URL sea la correcta
    
    except Exception as e:
        print(f"Se produjo un error durante la prueba: {e}") # Imprimir el error
        raise  # Re-lanzar la excepción para notificar el fallo de la prueba