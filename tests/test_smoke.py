def test_browser_open(driver):
    driver.get("https://saby.ru")
    assert "saby" in driver.current_url