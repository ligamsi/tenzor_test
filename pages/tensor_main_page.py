from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage:
    POWER_BLOCK = (By.XPATH, "//section[contains(., 'Сила в людях')]")
    MORE_DETAILS_BUTTON = (By.XPATH, "//a[contains(text(),'Подробнее')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def is_power_block_present(self):
        return self.wait.until(EC.presence_of_element_located(self.POWER_BLOCK))
    
    def click_more_details(self):
        button = self.wait.until(EC.element_to_be_clickable(self.MORE_DETAILS_BUTTON))
        button.click()