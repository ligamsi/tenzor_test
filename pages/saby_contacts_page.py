from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SabyContactsPage:
    # Локаторы
    TENSOR_BANNER = (By.XPATH, "//img[contains(@alt,'Тензор')]/ancestor::a")
    REGION_CHOOSER = (By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser__text")
    REGION_LIST = (By.CSS_SELECTOR, "div.sbis_ru-Region-Chooser__dropdown li")
    PARTNERS_LIST = (By.CSS_SELECTOR, "div.sbis_ru-Partners__list-item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_tensor_banner(self):
        # ждём, что страница контактов загрузилась
        self.wait.until(lambda d: "contacts" in d.current_url)
        # прокрутка вниз
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        banner = self.wait.until(EC.presence_of_element_located(self.TENSOR_BANNER))
        # доводим элемент в видимую область
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", banner)
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER))
        banner.click()

    def wait_region_is_loaded(self):
        region_el = self.wait.until(lambda d: d.find_element(*self.REGION_CHOOSER))
        self.wait.until(lambda d: region_el.text.strip() != "")
        return region_el.text.strip()

    def region_should_be(self, expected_region: str):
        self.wait_region_is_loaded()
        actual_region = self.wait_region_is_loaded()
        assert "Башкортостан" in actual_region, f"Ожидался регион 'Башкортостан', но найден '{actual_region}'"
        # Проверка через title на случай, если JS динамически изменил страницу
        assert expected_region in self.driver.title, f"Регион '{expected_region}' не найден в заголовке страницы"

    def partners_should_be_present(self):
        partners = self.wait.until(EC.presence_of_all_elements_located(self.PARTNERS_LIST))
        assert len(partners) > 0, "Список партнеров пустой"

    def get_partners_names(self):
        partners = self.wait.until(EC.presence_of_all_elements_located(self.PARTNERS_LIST))
        return [p.text.strip() for p in partners]

    def change_region(self, region_name: str):
        region_chooser = self.wait.until(EC.element_to_be_clickable(self.REGION_CHOOSER))
        region_chooser.click()
        regions = self.wait.until(EC.presence_of_all_elements_located(self.REGION_LIST))
        found = False
        for region in regions:
            if region_name in region.text:
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", region)
                region.click()
                found = True
                break
        assert found, f"Регион '{region_name}' не найден в списке"

    def check_url_and_title_contains_region(self, region_name: str):
        self.wait.until(lambda d: "02 Башкортостан" in d.page_source)
        assert region_name in self.driver.title or region_name in self.driver.current_url, \
            f"URL или заголовок не содержат регион '{region_name}'"