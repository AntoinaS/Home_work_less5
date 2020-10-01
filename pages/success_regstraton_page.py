from .base_page import BasePage


class SuccessRegPageLocators:
    SUCCESS_ALERT = ".alertinner"


class SuccessRegPage(BasePage):
    def chek_success_message_after_reg(self):
        return self.find(SuccessRegPageLocators.SUCCESS_ALERT).text
