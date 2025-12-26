from pages.swag_labs import SwagLabs

def test_check_swag_labs(browser):
    browser.get("https://www.saucedemo.com/")
    icon = SwagLabs(browser)
    assert icon.exist_icon()
    assert icon.exist_username()
    assert icon.exist_password()