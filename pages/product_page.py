from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.registration_page import RegistrationPage
from pages.authorization_page import AuthorizationPage

class ProductPageLocators:
    login_link = "#login_link"
    product_page_add_to_basket = ".btn-add-to-basket"
    product_page_success_mess = ".alert:nth-child(1) .alertinner strong"
    product_page_name_of_product = ".product_main h1"
    product_page_total_basket_value = ".alert:nth-child(3) .alertinner strong"
    product_page_basket_value = ".basket-mini"
    product_page_price_of_product = ".product_main .price_color"
    product_page_basket_link = ".alertinner [href$='/basket/']"


class ProductPage(BasePage):
    def add_product_to_basket(self):
        #Act
        present_value_not_float = self.find(ProductPageLocators.product_page_basket_value).text
        present_value_float = float((present_value_not_float.split('£')[1]).split('V')[0])
        self.find(ProductPageLocators.product_page_add_to_basket).click()
        #Assert
        success_mess=self.find(ProductPageLocators.product_page_success_mess).text 
        product_name = self.find(ProductPageLocators.product_page_name_of_product).text
        assert product_name == success_mess, "The product name is missing from the message" 
        #Assert
        basket_value = self.find(ProductPageLocators.product_page_total_basket_value).text
        price_product_not_float = self.find(ProductPageLocators.product_page_price_of_product).text
        price_product_float = float(price_product_not_float[1:len(price_product_not_float)])
        assert str(price_product_float + present_value_float) in basket_value, \
            f"The product {price_product_float} price is not equal to {present_value_float} the basket price "
    
    def go_to_basket_from_product_page(self):
        #Act
        self.find(ProductPageLocators.product_page_basket_link).click()
        return BasketPage(self.browser, self.browser.current_url) 
    
    def go_to_login_page(self):
        #Act
        self.find(ProductPageLocators.login_link).click()
        return RegistrationPage(self.browser, self.browser.current_url)
    
    def go_to_auth_page(self):
        #Act
        self.find(ProductPageLocators.login_link).click()
        return AuthorizationPage(self.browser, self.browser.current_url)
