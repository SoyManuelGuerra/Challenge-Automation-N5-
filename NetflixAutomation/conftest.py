# conftest.py
import pytest
from utils.DriverManager import SingletonNavegadorWeb

@pytest.fixture(scope="function")
def navegador_web():
    driver = SingletonNavegadorWeb.obtener_instancia()
    yield driver
    driver.quit()
