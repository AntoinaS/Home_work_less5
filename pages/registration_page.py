from pages.base_page import BasePage
from pages.success_regstraton_page import SuccessRegPage
import time


class RegistrationPageLocators:
    registration_form = "#register_form"
    authorization_form = "#login_form"

    email_registration = "#id_registration-email"
    pass1_registration = "#id_registration-password1"
    pass2_registration = "#id_registration-password2"
    send_registration_form = "[value='Register']"


class RegistrationPageData:
    email = str(time.time()) + "@fakemail.org"
    password = "Fake1pass233"


class RegistrationPage(BasePage):

    def enter_data_and_login(self):
        # Act
        self.find(RegistrationPageLocators.email_registration).\
            send_keys(RegistrationPageData.email)
        self.find(RegistrationPageLocators.pass1_registration).\
            send_keys(RegistrationPageData.password)
        self.find(RegistrationPageLocators.pass2_registration).\
            send_keys(RegistrationPageData.password)
        self.find(RegistrationPageLocators.send_registration_form).click()

        return SuccessRegPage(self.browser, self.browser.current_url)

    def check_reg_form(self):
        # Assert
        assert self.find(
            RegistrationPageLocators.registration_form) != None, "Registration form not found"

    def check_auth_form(self):
        # Assert
        assert self.find(
            RegistrationPageLocators.authorization_form) != None, "Authorization form not found"
