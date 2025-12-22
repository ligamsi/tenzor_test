from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorAboutPage:
    SECTION_WORKING_TITLE = (By.XPATH, "//h2[normalize-space()='Работаем']")
    WORK_IMAGES = (By.XPATH,"//h2[normalize-space()='Работаем']/following::div[1]//img")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def check_images_have_same_size(self):
        # Проверяем, что все фотографии в разделе 'Работаем' имеют одинаковую высоту и ширину.
        # 1. Ждем заголовок и скроллим к нему
        section_title = self.wait.until(
            EC.visibility_of_element_located(self.SECTION_WORKING_TITLE)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", section_title)

        # 2. Получаем список всех картинок
        images = self.wait.until(EC.presence_of_all_elements_located(self.WORK_IMAGES))
        assert len(images) > 0, "Изображения в блоке 'Работаем' не найдены"

        # 3. Собираем размеры
        # Используем атрибуты 'width' и 'height' из свойств элемента
        sizes = [
            (img.get_attribute("width"), img.get_attribute("height")) 
            for img in images
        ]
        
        # 4. Проверяем идентичность через set()
        # Если все кортежи (w, h) одинаковые, размер set будет равен 1
        unique_sizes = set(sizes)
        assert len(unique_sizes) == 1, (
            f"Обнаружены разные размеры изображений: {unique_sizes}. "
            f"Всего проверено картинок: {len(images)}"
        )