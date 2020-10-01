class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()

    def open_page(self):
        self.browser.get(self.url)

    def find(self, selector, time=10):
        return self.browser.find_element_by_css_selector(selector)