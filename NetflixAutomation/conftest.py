# conftest.py
import pytest
from utils.driver_manager import SingletonNavegadorWeb

@pytest.fixture(scope="function")
def navegador_web():
    driver = SingletonNavegadorWeb.obtener_instancia()
    yield driver
    driver.quit()
