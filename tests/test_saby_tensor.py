from pages.saby_main_page import SabyMainPage
from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage

def test_saby_to_tensor(driver):
    saby_main = SabyMainPage(driver)
    saby_contacts = SabyContactsPage(driver)
    tensor = TensorMainPage(driver)
    about = TensorAboutPage(driver)

    print("STEP 1: open saby main page")
    saby_main.open()

    print("STEP 2: go to contacts region")
    saby_main.open_contacts_region()
    assert "contacts" in driver.current_url

    print("STEP 3: click Tensor banner")
    saby_contacts.click_tensor_banner()

    print("STEP 4: switch to Tensor site")
    tensor.switch_to_tensor()
    assert "tensor.ru" in driver.current_url

    print("STEP 5: check 'Power in people' block")
    tensor.power_block_is_present()

    print("STEP 6: open About page")
    tensor.open_about_page()
    assert "/about" in driver.current_url

    print("STEP 7: check images size in 'Work' block")
    about.check_images_have_same_size()