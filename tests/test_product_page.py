from pages.main_page import MainPage
import pytest


@pytest.fixture
def open_guest_product_page(browser):
    open_main_page = MainPage(browser)
    open_main_page.open_page()
    all_goods_page = open_main_page.go_to_all_goods_page()
    open_guest_product_page = all_goods_page.go_to_product_page()
    return open_guest_product_page


@pytest.fixture
def open_user_main_page(browser):
    open_user_main_page = MainPage(browser)
    open_user_main_page.open_page()
    auth_page = open_user_main_page.go_to_auth_page()
    auth_page.enter_data_and_go_to_LK()
    return open_user_main_page


def test_guest_can_add_product_to_basket(browser, open_guest_product_page):
    open_guest_product_page.add_product_to_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, open_guest_product_page):
    open_guest_product_page.add_product_to_basket()
    basket_page = open_guest_product_page.go_to_basket_from_product_page()
    basket_page.check_arrange_of_items()


def test_guest_can_go_to_login_page_from_product_page(browser, open_guest_product_page):
    reg_page = open_guest_product_page.go_to_login_page()
    reg_page.check_reg_form()
    reg_page.check_auth_form()


def test_user_can_add_product_to_basket(browser, open_user_main_page):
    all_goods_page = open_user_main_page.go_to_all_goods_page()
    open_user_main_page = all_goods_page.go_to_product_page()
    open_user_main_page.add_product_to_basket()
