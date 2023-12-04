# pages/NetflixHomePage.py
from utils.TestFunctions import FuncionesBase

class NetflixHomePage(FuncionesBase):
    def __init__(self, controlador):
        super().__init__(controlador)

    def ir_a_home(self):
        """
        Navega a la página de inicio de Netflix.
        """
        self.navegar_a("https://www.netflix.com")

    # def obtener_titulo(self):
    #     """
    #     Obtiene y retorna el título de la página actual.
    #     """
    #     return super().obtener_titulo()

    # def obtener_url(self):
    #     """
    #     Obtiene y retorna la URL de la página actual.
    #     """
    #     return super().obtener_url()

