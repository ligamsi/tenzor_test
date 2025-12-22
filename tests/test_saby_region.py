import pytest
from pages.saby_main_page import SabyMainPage
from pages.saby_contacts_page import SabyContactsPage


@pytest.mark.selenium
def test_change_region_and_check_partners(driver):
    """
    Сценарий:
    1. Переход Saby -> Контакты.
    2. Проверка нашего региона и наличия партнеров.
    3. Выбор нового региона (Камчатский край).
    4. Проверка партнеров, url и title.
    """
    # Данные для теста
    initial_region = "Республика Башкортостан"
    target_region = "Камчатский край"
    target_url_part = "41-kamchatskij-kraj"

    saby_main = SabyMainPage(driver)
    saby_contacts = SabyContactsPage(driver)
    
    # 1. Открываем контакты
    saby_main.open()
    saby_main.open_contacts_region()

    # 2. Проверяем текущий регион и список партнеров
    current_reg = saby_contacts.get_current_region()
    assert current_reg == initial_region, f"Должен быть {initial_region}, а не {current_reg}"
    
    partners_before = saby_contacts.get_partners_list()
    assert len(partners_before) > 0, "Список партнеров пуст"

    # 3. Меняем регион
    saby_contacts.open_region_selector()
    saby_contacts.select_region(target_region)
    
    # 4. Ждем обновления и проверяем результат
    saby_contacts.wait_region_changed_to(target_region)
    partners_after = saby_contacts.get_partners_list()

    # Финальные проверки
    assert partners_before != partners_after, "Список партнеров не обновился после смены региона"
    assert target_url_part in driver.current_url, f"URL не содержит {target_url_part}"
    assert target_region in driver.title, "Title не содержит название нового региона"