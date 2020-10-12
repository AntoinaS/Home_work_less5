from pages.base_page import BasePage
from pages.product_page import ProductPage

class AllGoodsPageLocators:
    product_page_link = "section .row li:nth-child(1) a[title]"

class AllGoodsPage(BasePage):
    def go_to_product_page(self):
        #Act
        self.find(AllGoodsPageLocators.product_page_link).click()
        return ProductPage(self.browser, self.browser.current_url)