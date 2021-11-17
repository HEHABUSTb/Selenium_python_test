import pytest
from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
import time

link = 'https://rahulshettyacademy.com/AutomationPractice/'


@pytest.mark.usefixtures('browser')
@pytest.mark.buttons
class TestClass:

    def test_multi_browser(self):
        page = BasePage(self.browser, link)
        time.sleep(2)
        page.open()
        assert 1 == 2, 'Allure automate screenshot test'

    def test_radio_buttons(self, browser):
        browser.get(link)
        buttons = browser.find_elements(By.CSS_SELECTOR, "input[name='radioButton']")
        for button in buttons:
            button.click()
            time.sleep(1)
            assert button.is_selected(), 'RadioButton is not selected'

    def test_suggestion_example(self, browser):
        logger = BasePage(self.browser, link).getLogger()
        browser.get(link)
        field = browser.find_element(By.CSS_SELECTOR, '#autocomplete')
        field.send_keys('RUS')
        countries = browser.find_elements(By.CSS_SELECTOR, 'li[class="ui-menu-item"] .ui-menu-item-wrapper')
        for country in countries:
            logger.info(country.text)
            if 'Russian' in country.text:
                logger.info('In if statement block: ' + country.text)
                country.click()
                time.sleep(1)
                break
        assert field.get_attribute('value') == 'Russian Federation', 'Selected country not Russia'


