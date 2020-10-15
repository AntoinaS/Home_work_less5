from pages.base_page import BasePageHeader
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.all_goods_page import AllGoodsPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage
from pages.authorization_page import AuthorizationPage
import pytest


@pytest.fixture
def open_guest_product_page(browser):
    open_main_page = MainPage(browser)
    open_main_page.open_page()
    open_main_page.go_to_all_goods_page()
    all_goods_page = AllGoodsPage(browser, browser.current_url)
    all_goods_page.go_to_product_page()
    open_guest_product_page = ProductPage(browser, browser.current_url)
    return open_guest_product_page


@pytest.fixture
def open_user_main_page(browser):
    open_user_main_page = MainPage(browser)
    open_user_main_page.open_page()
    header = BasePageHeader(browser, browser.current_url)
    header.go_to_login_and_auth_page()
    auth_page = AuthorizationPage(browser, browser.current_url)
    auth_page.enter_data_and_go_to_LK()
    return open_user_main_page


def test_guest_can_add_product_to_basket(browser, open_guest_product_page):
    open_guest_product_page.add_product_to_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, open_guest_product_page):
    open_guest_product_page.add_product_to_basket()
    header = BasePageHeader(browser, browser.current_url)
    header.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_arrange_of_items()


def test_guest_can_go_to_login_page_from_product_page(browser, open_guest_product_page):
    header = BasePageHeader(browser, browser.current_url)
    header.go_to_login_and_auth_page()
    reg_page = RegistrationPage(browser, browser.current_url)
    reg_page.check_reg_form()
    reg_page.check_auth_form()


def test_user_can_add_product_to_basket(browser, open_user_main_page):
    open_user_main_page.go_to_all_goods_page()
    all_goods_page = AllGoodsPage(browser, browser.current_url)
    all_goods_page.go_to_product_page()
    open_user_main_page = ProductPage(browser, browser.current_url)
    open_user_main_page.add_product_to_basket()
