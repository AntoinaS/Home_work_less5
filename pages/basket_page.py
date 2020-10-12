from pages.base_page import BasePage

class BasketPageLocators:
    basket_page_arrange_of_items = ".basket-items"
    basket_page_picture_of_items = ".thumbnail"
    basket_page_header_of_items = "h3 a[href]"

class BasketPage(BasePage):
    def check_arrange_of_items(self):
        #Assert
        assert self.find_all(BasketPageLocators.basket_page_arrange_of_items) != [], "there are no items in the basket"
        assert self.find_all(BasketPageLocators.basket_page_picture_of_items) !=[], "elements don't have images"
        assert self.find_all(BasketPageLocators.basket_page_header_of_items) !=[],"elements don't have names"


