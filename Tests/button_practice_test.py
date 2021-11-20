from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Pages.base_page import BasePage
import time
import pytest

link = 'https://rahulshettyacademy.com/AutomationPractice/'


@pytest.mark.usefixtures('browser')
@pytest.mark.buttons
class TestClass:

    def test_allure_automatically_take_screen_when_fail(self):
        page = BasePage(self.browser, link)
        time.sleep(2)
        page.open()
        assert 1 == 2, 'Allure automate screenshot test'

    def test_language_option(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/'
        browser.get(link)
        time.sleep(3)


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
        assert 'QA Click Academy' in browser.title, 'New window is not target'

    def test_switch_tab(self, browser):
        browser.get(link)
        window_button = browser.find_element(By.CSS_SELECTOR, '#opentab')
        window_button.click()
        child_window = browser.window_handles[1]
        browser.switch_to.window(child_window)
        assert 'Academy' in browser.title, 'New tab is not target'

    def test_switch_to_alert(self, browser):
        browser.get(link)
        name = 'ALERT_TEST'
        browser.find_element(By.NAME, 'enter-name').send_keys(name)  #Fill text field for alert
        browser.find_element(By.ID, 'alertbtn').click()  #Push the button to invoke alert
        alert = browser.switch_to.alert
        assert name in alert.text, 'f{name} not present in alert'
        alert.accept()

    def test_switch_to_confirm_alert(self, browser):
        browser.get(link)
        browser.find_element(By.ID, 'confirmbtn').click()
        alert = browser.switch_to.alert
        alert_text = 'Hello , Are you sure you want to confirm?'
        assert alert_text == alert.text, f'{alert_text} not equal {alert.text}'
        alert.dismiss()

    def test_hide_show_example(self, browser):
        browser.get(link)
        hide_show_element = browser.find_element(By.NAME, 'show-hide')
        """
        Few functions to scroll page until element is not be visible:
            hide_show_element.location_once_scrolled_into_view 
        or
            actions = ActionChains(browser)
            actions.move_to_element(hide_show_element).perform()
        or 
            browser.execute_script("arguments[0].scrollIntoView();", hide_show_element)
        """

        browser.execute_script("arguments[0].scrollIntoView();", hide_show_element)

        assert hide_show_element.is_displayed(), 'Button is not displayed, when should'
        hide_button = browser.find_element(By.ID, 'hide-textbox')
        time.sleep(1)
        hide_button.click()
        assert not hide_show_element.is_displayed(), 'Button is displayed, when should not'
        show_button = browser.find_element(By.ID, 'show-textbox')
        time.sleep(1)
        show_button.click()
        assert hide_show_element.is_displayed(), 'Button is not displayed, when should'

    def test_mouse_hover(self, browser):
        browser.get(link)
        action = ActionChains(browser)
        mouse_menu = browser.find_element(By.ID, 'mousehover')
        action.move_to_element(mouse_menu).perform()
        top_mouse_menu = browser.find_element(By.LINK_TEXT, "Top")
        reload_mouse_menu = browser.find_element(By.LINK_TEXT, 'Reload')
        time.sleep(1)
        action.move_to_element(reload_mouse_menu).click().perform()
        time.sleep(1)

    def test_double_click_action(self, browser):
        link = 'https://chercher.tech/practice/practice-pop-ups-selenium-webdriver'
        browser.get(link)
        action = ActionChains(browser)
        double_click_button = browser.find_element(By.ID, 'double-click')
        action.context_click(double_click_button) #right click mouse
        action.double_click(double_click_button).perform()
        alert = browser.switch_to.alert
        alert_message = 'You double clicked me!!!, You got to be kidding me'
        time.sleep(2)
        assert alert_message == alert.text, 'Alert text not equal'
        alert.accept()

    def test_send_file(self, browser):
        link = 'https://chercher.tech/practice/practice-pop-ups-selenium-webdriver'
        browser.get(link)
        choose_button = browser.find_element(By.CSS_SELECTOR, '[name="upload"]')
        choose_button.send_keys('D:\\FlyLera\\HSYN\\G0018693.JPG') #You dont need click on button to send value
        path = 'C:\\fakepath\\G0018693.JPG'
        choose_button_path = choose_button.get_attribute('value')
        assert path == choose_button_path, f'{path} not = {choose_button_path}, check upload button'

    def test_iframe(self, browser):
        browser.get(link)
        browser.switch_to.frame('courses-iframe')
        blog_button = browser.find_element(By.LINK_TEXT, 'Blog')
        blog_button.location_once_scrolled_into_view
        blog_button.click()
        locator_for_blog_text = (By.CSS_SELECTOR, 'h3[data-css="tve-u-17adea8e9a3"]')
        WebDriverWait(browser, 4).until(EC.presence_of_element_located((locator_for_blog_text)))
        assertion_text = browser.find_element(*locator_for_blog_text).text
        verification_text = 'Our Popular Blog Categories'
        assert verification_text == assertion_text,\
            f'{verification_text} not equal {verification_text} check move you to blog page from iframe or not'













