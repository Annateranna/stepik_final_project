import pytest

from . import base_page
from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators

# from selenium.webdriver.common.by import By
import time


class ProductPage(BasePage):
    def put_to_basket(self):
        add_link = self.browser.find_element(*MainPageLocators.ADD_LINK)
        add_link.click()
        time.sleep(5)
       # solve = BasePage(self.browser, self.browser.switch_to.alert)
       # solve.solve_quiz_and_get_code()
       # time.sleep(2)

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

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert BasePage.is_not_element_present(*BasePageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        assert BasePage.is_not_element_present(*BasePageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*BasePageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

