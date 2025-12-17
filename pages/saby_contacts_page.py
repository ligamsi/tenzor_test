from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SabyContactsPage:
    URL = "https://saby.ru/contacts"

    TENSOR_BANNER = (By.XPATH, "//a[contains(@href, 'tensor.ru')]")
    MORE_OFFICES_BUTTON = (By.XPATH, "//span[contains(text(), 'Ещё')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get(self.URL)

    def click_more_offices(self):
        self.wait.until(EC.element_to_be_clickable(self.MORE_OFFICES_BUTTON)).click()

    def click_tensor_banner(self):
        banner = self.wait.until(EC.presence_of_element_located(self.TENSOR_BANNER))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", banner)
        banner.click()

    def switch_to_tensor(self):
        self.wait.until(lambda d: "tensor.ru" in d.current_url or len(d.window_handles) > 1)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])