from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SabyMainPage:
    CONTACTS_MENU = (By.XPATH, "//span[text()='Контакты']")
    MORE_OFFICES = (By.XPATH, "//span[contains(text(),'Еще')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get("https://saby.ru")

    def open_contacts_region(self):
        contacts = self.wait.until(EC.visibility_of_element_located(self.CONTACTS_MENU))
        ActionChains(self.driver).move_to_element(contacts).perform()
        more_offices = self.wait.until(EC.element_to_be_clickable(self.MORE_OFFICES))
        more_offices.click()