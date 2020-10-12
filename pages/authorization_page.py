from pages.base_page import BasePage
from pages.main_page import MainPage

class AuthorizationPageLocators:
    auth_email = "#id_login-username"
    auth_pass = "#id_login-password"
    send_auth_form = "[name='login_submit']"

class AuthorizationData:
    email = "1@mailinator.com"
    password= "U7LqDeeRv2q2cvQ"

class AuthorizationPage(BasePage):
    def enter_data_and_go_to_LK (self):
        #Act
        self.find(AuthorizationPageLocators.auth_email).send_keys(AuthorizationData.email)
        self.find(AuthorizationPageLocators.auth_pass).send_keys(AuthorizationData.password)
        self.find(AuthorizationPageLocators.send_auth_form).click() 

        return MainPage(self.browser,self.browser.current_url)