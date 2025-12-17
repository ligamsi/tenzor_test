import pytest
from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_main_page import TensorMainPage

def test_saby_to_tensor(driver):
    saby_page = SabyContactsPage(driver)
    tensor_page = TensorMainPage(driver)

    print("STEP 1: open saby contacts")
    saby_page.open()

    print("STEP 2: click more offices")
    saby_page.click_more_offices()

    print("STEP 3: click tensor banner")
    saby_page.click_tensor_banner()

    print("STEP 4: switch to tensor site")
    saby_page.switch_to_tensor()

    print("STEP 5: check 'Сила в людях'")
    assert tensor_page.is_power_block_present()

    print("STEP 6: click 'Подробнее'")
    tensor_page.click_more_details()

    print("STEP 7: check about URL")
    assert driver.current_url == "https://tensor.ru/about"