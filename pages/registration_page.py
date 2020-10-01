from .base_page import BasePage
from .success_regstraton_page import SuccessRegPage
import time


class RegistrationPageLocators:
    EMAIL_REGISTRATON = "#id_registration-email"
    PASS1_REGISTRATION = "#id_registration-password1"
    PASS2_REGSTRATION = "#id_registration-password2"
    SEND_REGISTRATION_FORM = "[value='Register']"
    alert_success = "alertinner"


class RegistrationPageData:
    EMAIL = str(time.time()) + "@fakemail.org"
    PASS = "Fake1Pass233"


class RegistrationPage(BasePage):

    def enter_data_and_login(self):
        self.find(RegistrationPageLocators.EMAIL_REGISTRATON).\
            send_keys(RegistrationPageData.EMAIL)
        self.find(RegistrationPageLocators.PASS1_REGISTRATION).\
            send_keys(RegistrationPageData.PASS)
        self.find(RegistrationPageLocators.PASS2_REGSTRATION).\
            send_keys(RegistrationPageData.PASS)
        self.find(RegistrationPageLocators.SEND_REGISTRATION_FORM).click()

        return SuccessRegPage(browser=self.browser, url=self.browser.current_url)