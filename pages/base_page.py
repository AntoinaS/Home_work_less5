import requests


class BasePageLocators:
    login_link = "#login_link"
    oscar_link = ".col-sm-7 a"
    all_goods_page = "[href$='/catalogue/']"
    base_page_search_string = "#id_q"
    base_page_search_btn = ".navbar-right.navbar-form input.btn"
    base_page_search_result_header = ".page-header h1"
    base_page_search_result_item = ".product_pod"
    base_page_search_result_not_found = ".form-horizontal p"
    product_page_basket_link = ".alertinner [href$='/basket/']"


class BasePageData:
    name_of_item = "The shellcoder's handbook"
    part_of_name_of_item = "The shellcoder's"
    unreal_name_of_item = "Chapi apple"


class BasePage:
    def __init__(self, browser, url='http://selenium1py.pythonanywhere.com/', timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()

    def open_page(self):
        self.browser.get(self.url)

    def get_requests_header(self):
        response = requests.get(self.url)
        return response.headers['Content-Language']

    def find(self, selector):
        return self.browser.find_element_by_css_selector(selector)

    def find_all(self, selector):
        return self.browser.find_elements_by_css_selector(selector)


class BasePageHeader(BasePage):

    def go_to_basket(self):
        # Act
        self.find(BasePageLocators.product_page_basket_link).click()

    def go_to_login_and_auth_page(self):
        # Act
        self.find(BasePageLocators.login_link).click()

    def go_to_oscar_link(self):
        # Act
        self.find(BasePageLocators.oscar_link).click()

    def search_name_of_item(self):
        # Act
        self.find(BasePageLocators.base_page_search_string).clear()
        self.find(BasePageLocators.base_page_search_string).send_keys(
            BasePageData.name_of_item)
        self.find(BasePageLocators.base_page_search_btn).click()
        # Assert
        result_search = self.find(
            BasePageLocators.base_page_search_result_header).text
        result_item = self.find(BasePageLocators.base_page_search_result_item)
        assert (BasePageData.name_of_item in result_search) and (
            result_item.is_displayed()), "Search didn't find the item or header is incorrect"

    def search_part_name_of_item(self):
        # Act
        self.find(BasePageLocators.base_page_search_string).clear()
        self.find(BasePageLocators.base_page_search_string).send_keys(
            BasePageData.part_of_name_of_item)
        self.find(BasePageLocators.base_page_search_btn).click()
        # Assert
        result_search = self.find(
            BasePageLocators.base_page_search_result_header).text
        result_item = self.find(BasePageLocators.base_page_search_result_item)
        assert (BasePageData.part_of_name_of_item in result_search) and (
            result_item.is_displayed()), "Search didn't find part name of item or header is incorrect"

    def search_unreal_name_of_item(self):
        # Act
        self.find(BasePageLocators.base_page_search_string).clear()
        self.find(BasePageLocators.base_page_search_string).send_keys(
            BasePageData.unreal_name_of_item)
        self.find(BasePageLocators.base_page_search_btn).click()
        # Assert
        result_search = self.find(
            BasePageLocators.base_page_search_result_header).text
        result_not_found = self.find(
            BasePageLocators.base_page_search_result_not_found)
        assert (BasePageData.unreal_name_of_item in result_search) and (
            result_not_found.is_displayed()), "Search find unreal name of item or header is incorrect"
