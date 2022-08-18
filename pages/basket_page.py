from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_BLOCK), "Basket is not empty"

    def basket_empty_message_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_FIELD), \
            "Basket is empty message doesn't preent"
