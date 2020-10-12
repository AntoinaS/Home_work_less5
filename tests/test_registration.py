from .pages.main_page import MainPage
MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"


def test_registration(browser):
    main_page = MainPage(browser)
    
    reg_page = main_page.go_to_login_page()
    success_page = reg_page.enter_data_and_login()

    success_message = success_page.chek_success_message_after_reg()
    assert success_message is not None, "Assert on Registration not pas"
