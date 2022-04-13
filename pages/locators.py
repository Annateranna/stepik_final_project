from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_LINK = (By.CSS_SELECTOR,
                ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "// *[ @ id = 'default'] / header / div[1] / div / div[2] / span / a")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    BASKET_ITEMS = (By.XPATH, "//*[@id='basket_formset']/div/div")
    EMPTY_MESSAGE = (By.XPATH, "//*[@id='content_inner']/p/text()")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value = 'Register']")
    ALL_ITEMS = (By.XPATH, "//*[@id='browse']/li/ul/li[1]/a")
