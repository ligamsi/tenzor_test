from pages.saby_main_page import SabyMainPage
from pages.saby_contacts_page import SabyContactsPage

def test_saby_to_tensor(driver):
    saby_main = SabyMainPage(driver)
    saby_contacts = SabyContactsPage(driver)

    print("STEP 1: open saby main page")
    saby_main.open()

    print("STEP 2: go to contacts region")
    saby_main.open_contacts_region()
    assert "contacts" in driver.current_url

    print("STEP 3: check default region and partners")
    saby_contacts.region_should_be("Республика Башкортостан")
    saby_contacts.partners_list_should_not_be_empty()

    '''print("STEP 4: change region to Kamchatka")
    contacts.change_region("Камчатский край")

    print("STEP 5: check region, partners, url and title")
    contacts.region_should_be("Камчатский край")
    contacts.partners_list_should_be_changed()
    contacts.url_and_title_should_contain("Камчатский край")'''