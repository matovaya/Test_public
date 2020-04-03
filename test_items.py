from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_should_find_add_to_basket_button(browser):
    try:
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    except NoSuchElementException:
        assert NoSuchElementException == 0, "Пионеры спёрли кнопку / Button is not avilable"
