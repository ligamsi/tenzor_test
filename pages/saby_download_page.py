import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SabyDownloadPage:
    # вкладка "СБИС Плагин"
    PLUGIN_TAB = (By.XPATH, "//div[contains(@class, 'sbis_ru-DownloadThinTab')]//div[contains(text(), 'СБИС Плагин')]")
    # ссылка на скачивание веб-установщика для Windows
    DOWNLOAD_LINK = (By.XPATH, "//a[contains(@href, 'plugin') and contains(@href, 'exe')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def download_sbis_plugin(self):
        # 1. Переходим на вкладку СБИС Плагин
        self.wait.until(EC.element_to_be_clickable(self.PLUGIN_TAB)).click()
        
        # 2. Получаем ожидаемый размер из текста ссылки
        link_element = self.wait.until(EC.presence_of_element_located(self.DOWNLOAD_LINK))
        link_text = link_element.text
        
        # Извлекаем "3.64"
        expected_size = float(link_text.split(' ')[2]) 
        
        # 3. Кликаем скачать
        link_element.click()
        
        return expected_size

    def wait_for_download(self, file_name, timeout=60):
        # Ожидание завершения загрузки файла
        path = os.path.join(os.getcwd(), file_name)
        end_time = time.time() + timeout
        while time.time() < end_time:
            if os.path.exists(path):
                # Проверяем, что файл не временный
                if not path.endswith('.crdownload'):
                    return path
            time.sleep(1)
        return None