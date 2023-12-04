# tests/netflix_home.py
from pages.NetflixHomePage import NetflixHomePage
from utils.Selectors import Selectores

def test_acceso_a_netflix(navegador_web):
    # Crear una instancia de la página de inicio de Netflix
    netflix_home = NetflixHomePage(navegador_web)
    netflix_home.configurar_espera_implicita(10)  # Configurar espera implícita

    try:
        # Navegar a la página de inicio de Netflix
        netflix_home.ir_a_home()

        # Utilizar espera explícita antes de obtener el título y la URL
        netflix_home.esperar_elemento(Selectores.INICIAR_SESION, tipo_espera=['visibilidad', 'clickeable', 'presencia'])

        # Obtener e imprimir el título y la URL de la página
        titulo = netflix_home.obtener_titulo()
        url = netflix_home.obtener_url()
        print(f"Título de la página: {titulo}")
        print(f"URL de la página: {url}")

    except Exception as e:
        print(f"Se produjo un error durante la prueba: {e}")
        raise  # Re-lanzar la excepción para notificar el fallo de la prueba
