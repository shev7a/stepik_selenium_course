from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_cart_button_on_the_page(browser):
    browser.get(url)
    cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert cart_button.is_displayed()
