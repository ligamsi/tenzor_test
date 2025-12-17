from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorAboutPage:
    WORK_IMAGES = (
        By.XPATH,
        "//h2[normalize-space()='Работаем']/following::div[1]//img"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def check_images_have_same_size(self):
        # Скроллим к заголовку, чтобы блок точно прогрузился
        header = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Работаем']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", header
        )

        images = self.wait.until(
            EC.presence_of_all_elements_located(self.WORK_IMAGES)
        )

        assert len(images) > 1, "В блоке 'Работаем' не найдено изображений"

        sizes = [(img.size["width"], img.size["height"]) for img in images]

        assert len(set(sizes)) == 1, (
            f"Размеры изображений отличаются: {set(sizes)}"
        )