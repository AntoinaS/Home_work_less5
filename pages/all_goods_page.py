from pages.base_page import BasePage

class AllGoodsPageLocators:
    product_page_link = "section .row li:nth-child(1) a[title]"

class AllGoodsPage(BasePage):
    def go_to_product_page(self):
        #Act
        self.find(AllGoodsPageLocators.product_page_link).click()