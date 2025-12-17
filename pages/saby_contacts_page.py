from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SabyContactsPage:
    URL = "https://saby.ru/contacts"

    TENSOR_BANNER = (By.XPATH, "//a[contains(@href, 'tensor.ru')]")
    MORE_OFFICES_BUTTON = (By.XPATH, "//span[contains(text(), 'Ещё')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    def click_more_offices(self):
        self.wait.until(EC.element_to_be_clickable(self.MORE_OFFICES_BUTTON)).click()

    def click_tensor_banner(self):
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER)).click()

    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])