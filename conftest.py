import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # путь к текущей папке проекта для скачивания
    download_path = os.getcwd()

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    # настройки для автоматического скачивания файла
    prefs = {
        "download.default_directory": download_path, # куда сохранять
        "download.prompt_for_download": False,       # не спрашивать куда сохранять
        "safebrowsing.enabled": True                 # разрешить скачивание
    }
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()