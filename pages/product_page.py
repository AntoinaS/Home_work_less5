from pages.base_page import BasePage
import time


class ProductPageLocators:
    product_page_add_to_basket = ".btn-add-to-basket"
    product_page_success_mess = ".alert:nth-child(1) .alertinner strong"
    product_page_name_of_product = ".product_main h1"
    product_page_basket_value = ".basket-mini"
    product_page_price_of_product = ".product_main .price_color"


class ProductPage(BasePage):
    def add_product_to_basket(self):
        # Act
        present_value_not_float = self.find(
            ProductPageLocators.product_page_basket_value).text
        present_value_float = float(
            (present_value_not_float.split('£')[1]).split('V')[0])
        self.find(ProductPageLocators.product_page_add_to_basket).click()
        # Assert
        success_mess = self.find(
            ProductPageLocators.product_page_success_mess).text
        product_name = self.find(
            ProductPageLocators.product_page_name_of_product).text
        assert product_name == success_mess, "The product name is missing from the message"
        # Assert
        time.sleep(2)
        basket_value = self.find(
            ProductPageLocators.product_page_basket_value).text
        basket_value = basket_value.split('£')[1]
        price_product_not_float = self.find(
            ProductPageLocators.product_page_price_of_product).text
        price_product_float = float(
            price_product_not_float[1:len(price_product_not_float)])
        assert str(price_product_float + present_value_float) in basket_value, \
            f"The product price is not equal to the basket price\
                 {price_product_float} + {present_value_float} != {basket_value}"
