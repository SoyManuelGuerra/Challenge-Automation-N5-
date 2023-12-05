# pages/NetflixHomePage.py
from utils.test_utils import FuncionesBase

class NetflixHomePage(FuncionesBase):
    def __init__(self, controlador):
        super().__init__(controlador)

    def ir_a_home(self):
        """
        Navega a la página de inicio de Netflix.
        """
        self.navegar_a("https://www.netflix.com")

