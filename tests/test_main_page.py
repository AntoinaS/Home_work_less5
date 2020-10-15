import pytest
from pages.main_page import MainPage
from pages.base_page import BasePageHeader
from pages.registration_page import RegistrationPage


@pytest.fixture
def open_main_page(browser):
    open_main_page = MainPage(browser)
    open_main_page.open_page()
    return open_main_page


def test_guest_element_on_main_page(browser, open_main_page):
    open_main_page.check_main_page_menu()
    open_main_page.check_main_page_amount_in_basket()
    open_main_page.check_language_on_page()


def test_guest_can_go_to_login_page_from_main_page(browser, open_main_page):
    header = BasePageHeader(browser, browser.current_url)
    header.go_to_login_and_auth_page()
    reg_page = RegistrationPage(browser, browser.current_url)
    reg_page.check_reg_form()
    reg_page.check_auth_form()


def test_guest_oscar_link(browser, open_main_page):
    header = BasePageHeader(browser, browser.current_url)
    header.go_to_oscar_link()


def test_guest_main_page_search(browser, open_main_page):
    header = BasePageHeader(browser, browser.current_url)
    header.search_name_of_item()
    header.search_part_name_of_item()
    header.search_unreal_name_of_item()
