from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SabyContactsPage:
    # Элементы меню
    CONTACTS_MENU = (By.XPATH, "//span[text()='Контакты']")
    TENSOR_BANNER = (By.XPATH, "//img[contains(@alt,'Tensor')]")
    MORE_OFFICES_BUTTON = (By.XPATH, "//span[contains(text(),'Ещё') and contains(text(),'офис')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    def open(self):
        # Открываем главную страницу Saby
        self.driver.get("https://saby.ru")

    def hover_contacts_menu(self):
        # Ждём пункт меню "Контакты"
        contacts = self.wait.until(EC.visibility_of_element_located(self.CONTACTS_MENU))
        # Наводим мышь
        self.actions.move_to_element(contacts).perform()
        # Ждём появления кнопки
        more_offices = self.wait.until(EC.element_to_be_clickable(self.MORE_OFFICES_BUTTON))
        # Кликаем
        more_offices.click()

    def click_more_offices(self):
        # Ждём кнопку и кликаем
        button = self.wait.until(EC.element_to_be_clickable(self.MORE_OFFICES_BUTTON))
        button.click()

    def click_tensor_banner(self):
        # Кликаем по баннеру Tensor
        banner = self.wait.until(EC.presence_of_element_located(self.TENSOR_BANNER))
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", banner)
        banner.click()

    def switch_to_tensor(self):
        # Переключаемся на новое окно Tensor
        self.wait.until(lambda d: len(d.window_handles) > 1 or "tensor.ru" in d.current_url)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])