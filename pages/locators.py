from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_LINK = (By.CSS_SELECTOR,
                ".btn-add-to-basket")
