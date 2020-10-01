from .base_page import BasePage
from .registration_page import RegistrationPage


class MainPageLocators:
    LOGIN_LINK = "#login_link"


class MainPage(BasePage):
    def go_to_login_page(self):
        self.find(MainPageLocators.LOGIN_LINK).click()

        return RegistrationPage(browser=self.browser, url=self.browser.current_url)
