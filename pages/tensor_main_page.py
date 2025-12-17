from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage:
    POWER_BLOCK = (By.XPATH, "//*[contains(text(),'Сила в людях')]")
    MORE_DETAILS = (By.XPATH, "//a[contains(@href,'/about')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def switch_to_tensor(self):
        # Переключаемся на новое окно Tensor
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def power_block_is_present(self):
        self.wait.until(
            EC.visibility_of_element_located(self.POWER_BLOCK)
        )

    def open_about_page(self):
        about = self.wait.until(EC.element_to_be_clickable(self.MORE_DETAILS))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            about
        )
        about.click()
        self.wait.until(EC.url_contains("/about"))