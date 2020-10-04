from .base_page import BasePage


class SuccessRegPageLocators:
    success_alert = ".alertinner"


class SuccessRegPage(BasePage):
    def chek_success_message_after_reg(self):
        return self.find(SuccessRegPageLocators.success_alert).text
