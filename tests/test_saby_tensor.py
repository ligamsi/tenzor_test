from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_main_page import TensorMainPage

def test_saby_to_tensor(driver):
    saby_page = SabyContactsPage(driver)
    saby_page.open()

    saby_page.click_more_offices()
    saby_page.click_tensor_banner()
    saby_page.switch_to_tensor()

    assert "tensor.ru" in driver.current_url

    tensor_page = TensorMainPage(driver)
    assert tensor_page.is_power_block_present()

    tensor_page.click_more_details()

    assert driver.current_url == "https://tensor.ru/about"