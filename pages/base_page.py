import requests

class BasePage:
    def __init__(self, browser, url='http://selenium1py.pythonanywhere.com/', timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()
    
    def open_page(self):
        self.browser.get(self.url)

    def get_requests_header(self):
        response = requests.get(self.url)
        return response.headers['Content-Language']


    def find(self, selector):
        return self.browser.find_element_by_css_selector(selector)
    
    def find_all(self, selector):
        return self.browser.find_elements_by_css_selector(selector)