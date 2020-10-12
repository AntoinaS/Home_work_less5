from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", action='store', default="en", help="Choose language: ru, en, ar,\
     ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")
    parser.addoption("--browser", action='store', default="chrome", help="Enter chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):

    language = request.config.getoption("--language")
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser {} still is not implemented".format(browser_name))

    yield browser

    browser.quit()
