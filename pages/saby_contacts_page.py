from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SabyContactsPage:
    TENSOR_BANNER = (By.XPATH, "//img[contains(@alt,'Тензор')]/ancestor::a")
    REGION_TEXT = (By.XPATH, "//span[contains(@class,'sbis_ru-Region-Chooser') and contains(@class, 'ml-16')]")
    REGION_PANEL = (By.CSS_SELECTOR, "div.sbis_ru-Region-Panel")
    PARTNER_NAMES = (By.CSS_SELECTOR, "div.sbisru-Contacts-List__name[itemprop='name']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # вспомогательные методы
    def _scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def wait_page_loaded(self):
        self.wait.until(lambda d: "contacts" in d.current_url)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # действия
    def click_tensor_banner(self):
        self.wait_page_loaded()
        banner = self.wait.until(EC.presence_of_element_located(self.TENSOR_BANNER))
        self._scroll_to(banner)
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER)).click()

    def open_region_selector(self):
        self.wait_page_loaded()
        self.wait.until(EC.element_to_be_clickable(self.REGION_TEXT)).click()
        self.wait.until(EC.visibility_of_element_located(self.REGION_PANEL))

    def select_region(self, region_name: str):
        # локатор для любого региона
        region_locator = (By.XPATH, f"//span[@title='{region_name}']")
        self.wait.until(EC.element_to_be_clickable(region_locator)).click()

    # получение данных
    def get_current_region(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.REGION_TEXT)).text

    def get_partners_list(self) -> list:
        self.wait_page_loaded()
        # ждем появления хотя бы одного партнера
        self.wait.until(lambda d: len(d.find_elements(*self.PARTNER_NAMES)) > 0)
        elements = self.driver.find_elements(*self.PARTNER_NAMES)
        return [el.text.strip() for el in elements if el.text.strip()]

    def wait_region_changed_to(self, region_name: str):
        self.wait.until(EC.text_to_be_present_in_element(self.REGION_TEXT, region_name))