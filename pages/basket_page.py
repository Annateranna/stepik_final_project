import pytest

from . import base_page
from .base_page import BasePage
from .locators import BasePageLocators
# from selenium.webdriver.common.by import By
import time


class BasketPage(BasePage):
    def view_basket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()
        time.sleep(2)

    def should_basket_be_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), \
            "Basket must be empty"

    def should_empty_message_be_present(self):
        assert self.is_not_element_present(*BasePageLocators.EMPTY_MESSAGE), \
            "Where is empty message?"

