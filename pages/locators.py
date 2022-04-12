from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_LINK = (By.CSS_SELECTOR,
                ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
