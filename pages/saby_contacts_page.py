from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SabyContactsPage:
    TENSOR_BANNER = (By.XPATH, "//img[contains(@alt,'Tensor')]")
    MORE_OFFICES_BUTTON = (By.XPATH, "//span[contains(text(), 'Ещё')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get("https://saby.ru/contacts")

    def click_more_offices(self):
        button = self.wait.until(EC.presence_of_element_located(self.MORE_OFFICES_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.wait.until(EC.element_to_be_clickable(self.MORE_OFFICES_BUTTON))
        button.click()

    def click_tensor_banner(self):
        banner = self.wait.until(EC.presence_of_element_located(self.TENSOR_BANNER))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", banner)
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER))
        banner.click()

    def switch_to_tensor(self):
        self.wait.until(lambda d: len(d.window_handles) > 1 or "tensor.ru" in d.current_url)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])