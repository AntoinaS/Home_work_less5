from pages.base_page import BasePage
from pages.registration_page import RegistrationPage
#from .authorization_page import AuthorizationPage
from pages.all_goods_page import AllGoodsPage
import time


class MainPageLocators:
    login_link = "#login_link"
    oscar_link = ".col-sm-7 a"
    all_goods_page = "[href$='/catalogue/']"
    main_page_menu = ".open"
    main_page_basket = ".basket-mini"
    main_page_language_control = "option[selected='selected']"
    main_page_search_string = "#id_q"
    main_page_search_btn = ".navbar-right.navbar-form input.btn"
    main_page_search_result_header = ".page-header h1"
    main_page_search_result_item = ".product_pod"
    main_page_search_result_not_found = ".form-horizontal p"


class MainPageData:
    name_of_item = "The shellcoder's handbook"
    part_of_name_of_item = "The shellcoder's"
    unreal_name_of_item = "Chapi apple"


class MainPage(BasePage):

    def check_main_page_menu(self):
        #Assert
        assert self.find(MainPageLocators.main_page_menu).is_displayed(), "Main page menu not found"
        if (self.find(MainPageLocators.main_page_menu).is_displayed()):
            return True

    def check_main_page_amount_in_basket(self):
        #Assert
        assert '0.00' in self.find(
            MainPageLocators.main_page_basket).text, "Basket is not empty for new user"

    def check_language_on_page(self):
        #Assert
        assert self.find(MainPageLocators.main_page_language_control).get_attribute(
            "value") == self.get_requests_header(), "Languages are not the same"

    def go_to_login_page(self):
        #Act
        self.find(MainPageLocators.login_link).click()
        return RegistrationPage(self.browser, self.browser.current_url)

    def go_to_oscar_link(self):
        #Act
        self.find(MainPageLocators.oscar_link).click()
        assert self.check_main_page_menu(), "Main page menu not found"
    
    def go_to_all_goods_page(self):
        #Act
        self.find(MainPageLocators.all_goods_page).click()
        return AllGoodsPage(self.browser, self.browser.current_url)

    def search_name_of_item(self):
        #Act
        self.find(MainPageLocators.main_page_search_string).clear()
        self.find(MainPageLocators.main_page_search_string).send_keys(
            MainPageData.name_of_item)
        self.find(MainPageLocators.main_page_search_btn).click()
        #Assert
        result_search = self.find(
            MainPageLocators.main_page_search_result_header).text
        result_item = self.find(MainPageLocators.main_page_search_result_item)
        assert (MainPageData.name_of_item in result_search) and (
            result_item.is_displayed()), "Search didn't find the item or header is incorrect"

    def search_part_name_of_item(self):
        #Act
        self.find(MainPageLocators.main_page_search_string).clear()
        self.find(MainPageLocators.main_page_search_string).send_keys(
            MainPageData.part_of_name_of_item)
        self.find(MainPageLocators.main_page_search_btn).click()
        #Assert
        result_search = self.find(
            MainPageLocators.main_page_search_result_header).text
        result_item = self.find(MainPageLocators.main_page_search_result_item)
        assert (MainPageData.part_of_name_of_item in result_search) and (
            result_item.is_displayed()), "Search didn't find part name of item or header is incorrect"

    def search_unreal_name_of_item(self):
        #Act
        self.find(MainPageLocators.main_page_search_string).clear()
        self.find(MainPageLocators.main_page_search_string).send_keys(
            MainPageData.unreal_name_of_item)
        self.find(MainPageLocators.main_page_search_btn).click()
        #Assert
        result_search = self.find(
            MainPageLocators.main_page_search_result_header).text
        result_not_found = self.find(
            MainPageLocators.main_page_search_result_not_found)
        assert (MainPageData.unreal_name_of_item in result_search) and (
            result_not_found.is_displayed()), "Search find unreal name of item or header is incorrect"
