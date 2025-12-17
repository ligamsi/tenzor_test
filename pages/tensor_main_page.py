from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage:
    URL = "https://tensor.ru/"

    POWER_BLOCK = (By.XPATH, "//h2[contains(text(), 'Сила в людях')]")
    MORE_DETAILS_LINK = (By.XPATH, "//a[contains(@href, '/about')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_power_block_present(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.POWER_BLOCK)
        )
    
    def click_more_details(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MORE_DETAILS_LINK)
        ).click()