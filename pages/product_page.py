from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_STRING).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_STRING).text

    def check_added_to_basket(self, product_name):
        assert self.is_element_present(*ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET_MESSAGE), \
            "ADDED TO BASKET message does not present"
        assert self.browser.find_element(*ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET_MESSAGE).text == \
               product_name, "Book name doesn't match"

    def check_basket_total(self, product_price):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "BASKET TOTAL message doesn't present"
        assert self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text == product_price, \
            "Basket total doesn't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET_MESSAGE), \
            "Success message is presented"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET_MESSAGE), \
            "Success message doesn't disappear"
