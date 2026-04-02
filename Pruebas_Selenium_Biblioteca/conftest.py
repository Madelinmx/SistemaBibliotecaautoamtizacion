import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    # No agregamos opciones de 'headless' para poder ver la ejecución
    driver = webdriver.Chrome(service=service)
    driver.maximize_window() # Esto ayudará a que se vea mejor en el video
    driver.implicitly_wait(10) 
    yield driver
    driver.quit()