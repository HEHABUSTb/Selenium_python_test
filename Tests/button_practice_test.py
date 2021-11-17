import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

    def test_dropdown_select(self, browser):
        browser.get(link)
        dropdown = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown-class-example'))
        dropdown.select_by_visible_text('Option1')
        dropdown.select_by_index(2)
        dropdown.select_by_value('option3')
        dropdown_selected_value = browser.find_element(By.CSS_SELECTOR, '#dropdown-class-example').get_attribute('value')
        time.sleep(1)
        option3 = 'option3'
        assert option3 == dropdown_selected_value, f'Selected: {dropdown_selected_value}, should be {option3}'

    def test_checkboxes(self, browser):
        browser.get(link)
        checkboxes = browser.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        for checkbox in checkboxes:
            checkbox.click()
            time.sleep(1)
            assert checkbox.is_selected(), f'Checkbox {checkbox} is not selected'

    def test_switch_window(self, browser):
        browser.get(link)
        window_button = browser.find_element(By.CSS_SELECTOR, '#openwindow')
        window_button.click()
        child_window = browser.window_handles[1]
        browser.switch_to.window(child_window)
        assert 'QA Click Academy' in browser.title, 'New window is not in target'



