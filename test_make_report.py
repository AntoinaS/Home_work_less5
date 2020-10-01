from .pages.main_page import MainPage
MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"


def test_registration(browser):
    MAIN_PAGE = MainPage(browser, MAIN_PAGE_LINK)
    MAIN_PAGE.open_page()

    REG_PAGE = MAIN_PAGE.go_to_login_page()
    SUCCESS_PAGE = REG_PAGE.enter_data_and_login()

    SUCCESS_MESSAGE = SUCCESS_PAGE.chek_success_message_after_reg()
    assert SUCCESS_MESSAGE is not None, "Assert on Registration not pas"




