from pages.main_contacts_page import SabyContactsPage

def test_open_contacts(driver):
    page = SabyContactsPage(driver)
    page.open()
    assert "contacts" in driver.current_url