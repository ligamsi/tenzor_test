from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage:
    POWER_BLOCK = (By.XPATH, "//*[contains(text(),'Сила в людях')]")
    MORE_DETAILS_LINK = (By.XPATH, "//div[contains(@class, 'tensor_ru-Index__block4-content')]//a[contains(@href,'/about')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def switch_to_tensor(self):
        # переключаемся на новое окно Tensor
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_power_block_present(self) -> bool:
        # проверяет наличие блока 'Сила в людях'
        element = self.wait.until(EC.visibility_of_element_located(self.POWER_BLOCK))
        return element.is_displayed()

    def open_about_page(self):
        # находит ссылку 'Подробнее', скроллит к ней и кликает
        about_link = self.wait.until(EC.presence_of_element_located(self.MORE_DETAILS_LINK))
        # скролл к элементу
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", about_link)
        # ожидание кликабельности после скролла
        self.wait.until(EC.element_to_be_clickable(self.MORE_DETAILS_LINK)).click()
        # ждем смены URL
        self.wait.until(EC.url_contains("/about"))