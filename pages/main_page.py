from .base_page import BasePage
from .registration_page import RegistrationPage


class MainPageLocators:
    login_link = "#login_link"


class MainPage(BasePage):
    def go_to_login_page(self):
        self.find(MainPageLocators.login_link).click()

        return RegistrationPage(browser=self.browser, url=self.browser.current_url)
