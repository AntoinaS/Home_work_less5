from .base_page import BasePage
from .success_regstraton_page import SuccessRegPage
import time


class RegistrationPageLocators:
    email_registration = "#id_registration-email"
    pass1_registration = "#id_registration-password1"
    pass2_registration = "#id_registration-password2"
    send_registration_form = "[value='Register']"
    alert_success = "alertinner"


class RegistrationPageData:
    email = str(time.time()) + "@fakemail.org"
    password = "Fake1pass233"


class RegistrationPage(BasePage):

    def enter_data_and_login(self):
        self.find(RegistrationPageLocators.email_registration).\
            send_keys(RegistrationPageData.email)
        self.find(RegistrationPageLocators.pass1_registration).\
            send_keys(RegistrationPageData.password)
        self.find(RegistrationPageLocators.pass2_registration).\
            send_keys(RegistrationPageData.password)
        self.find(RegistrationPageLocators.send_registration_form).click()

        return SuccessRegPage(browser=self.browser, url=self.browser.current_url)