from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
import time


class ProductPage(BasePage):
    def put_to_basket(self):
        add_link = self.browser.find_element(*MainPageLocators.ADD_LINK)
        add_link.click()
        time.sleep(2)
        solve = BasePage(self.browser, self.browser.switch_to.alert)
        solve.solve_quiz_and_get_code()
        time.sleep(2)

    def should_be_in_basket(self):
        check1 = self.browser.find_element_by_css_selector(
            'div.alertinner > strong')
        check2 = self.browser.find_element_by_css_selector(
            'div.product_main > h1')
        assert check1.text == check2.text, 'The name of the product in basket is wrong'
        time.sleep(2)

    def the_price_should_be_equal(self):
        check1 = self.browser.find_element_by_css_selector(
            'div.alertinner > p > strong')
        check2 = self.browser.find_element_by_css_selector(
            'p.price_color')
        assert check1.text == check2.text, 'The prices are not equal'



