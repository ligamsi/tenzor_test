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
    saby_contacts.partners_should_be_present()

    old_partners = saby_contacts.get_partners_names()

    print("STEP 4: change region to Камчатский край")
    saby_contacts.change_region("Камчатский край")

    print("STEP 5: check region, partners, url and title")
    saby_contacts.region_should_be("Камчатский край")

    new_partners = saby_contacts.get_partners_names()
    assert old_partners != new_partners, "Список партнёров не изменился после смены региона"

    saby_contacts.check_url_and_title_contains_region("Камчатский")