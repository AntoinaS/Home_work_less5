from pages.base_page import BasePage
import time


class MainPageLocators:
    all_goods_page = "[href$='/catalogue/']"
    main_page_menu = ".open"
    main_page_basket = ".basket-mini"
    main_page_language_control = "option[selected='selected']"


class MainPageData:
    name_of_item = "The shellcoder's handbook"
    part_of_name_of_item = "The shellcoder's"
    unreal_name_of_item = "Chapi apple"


class MainPage(BasePage):

    def check_main_page_menu(self):
        # Assert
        assert self.find(MainPageLocators.main_page_menu).is_displayed(
        ), "Main page menu not found"
        if (self.find(MainPageLocators.main_page_menu).is_displayed()):
            return True

    def check_main_page_amount_in_basket(self):
        # Assert
        assert '0.00' in self.find(
            MainPageLocators.main_page_basket).text, "Basket is not empty for new user"

    def check_language_on_page(self):
        # Assert
        assert self.find(MainPageLocators.main_page_language_control).get_attribute(
            "value") == self.get_requests_header(), "Languages are not the same"

    def go_to_all_goods_page(self):
        # Act
        self.find(MainPageLocators.all_goods_page).click()
