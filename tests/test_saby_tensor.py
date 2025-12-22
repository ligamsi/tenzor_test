import pytest
from pages.saby_main_page import SabyMainPage
from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage

@pytest.mark.selenium
def test_saby_to_tensor(driver):
    """
    Сценарий:
    1. Переход Saby -> Контакты -> Баннер Тензор.
    2. Проверка перехода на сайт Тензор.
    3. Проверка блока 'Сила в людях' и страницы 'О компании'.
    4. Сравнение размеров фотографий в разделе 'Работаем'.
    """
    saby_main = SabyMainPage(driver)
    saby_contacts = SabyContactsPage(driver)
    tensor_main = TensorMainPage(driver)
    tensor_about = TensorAboutPage(driver)

    # 1-2. Переход в контакты Saby
    saby_main.open()
    saby_main.open_contacts_region()
    assert "contacts" in driver.current_url, "Не удалось перейти в раздел 'Контакты'"

    # 3-4. Клик по баннеру и переход на Тензор
    saby_contacts.click_tensor_banner()
    tensor_main.switch_to_tensor()
    assert "tensor.ru" in driver.current_url, "Сайт Тензор не открылся"

    # 5. Проверка блока 'Сила в людях'
    assert tensor_main.is_power_block_present(), "Блок 'Сила в людях' не найден"

    # 6. Переход в раздел 'О компании'
    tensor_main.open_about_page()
    assert "/about" in driver.current_url, "Не удалось открыть страницу 'О компании'"

    # 7. Проверка размеров изображений
    tensor_about.check_images_have_same_size()