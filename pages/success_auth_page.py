from pages.base_page import BasePage
from pages.main_page import MainPage

class SuccessAuthPage(BasePage):
    def return_main_page(self):
        return MainPage(self.browser,self.browser.current_url)