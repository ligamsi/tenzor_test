from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SabyContactsPage:
    # Элементы меню
    TENSOR_BANNER = (By.XPATH,"//img[contains(@alt,'Тензор')]/ancestor::a")
    REGION_NAME = (By.CSS_SELECTOR, 'span.sbis_ru-Region-Chooser__text')
    PARTNERS_LIST = (By.CSS_SELECTOR, 'div.sbisru-Contacts-List__col')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_tensor_banner(self):
        # ждём, что страница контактов загрузилась
        self.wait.until(lambda d: "contacts" in d.current_url)
        # прокрутка вниз
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        banner = self.wait.until(EC.presence_of_element_located(self.TENSOR_BANNER))
        # доводим элемент в видимую область
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            banner
        )
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER))
        banner.click()

    def region_should_be(self, expected_region: str):
        region = self.wait.until(EC.visibility_of_element_located(self.REGION_NAME)).text
        assert expected_region in region, (
            f"Ожидался регион '{expected_region}', фактически - '{region}'"
        )

    def partners_list_should_not_be_empty(self):
        partners = self.wait.until(
            EC.presence_of_all_elements_located(self.PARTNERS_LIST)
        )
        assert len(partners) > 0, "Список партнёров пуст"