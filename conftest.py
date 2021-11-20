import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
browser = None



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Select locale here")
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose chrome or firefox')


@pytest.fixture(scope="function")
def browser(request):
    global browser
    language = request.config.getoption("language")
    options = Options()
    browser_name = request.config.getoption("browser")
    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        request.cls.browser = browser
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        options = webdriver.FirefoxOptions()
        options.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
        request.cls.browser = browser

    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    """
        #Automatically take screenshot when test fails and attach to allure report
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            allure.attach(browser.get_screenshot_as_png(), name=file_name,
                          attachment_type=AttachmentType.PNG)

