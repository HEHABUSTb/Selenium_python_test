import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.base_page import BasePage



import allure
import pytest




@pytest.mark.usefixtures('browser')
class HomePage(BasePage):

    link = 'https://rahulshettyacademy.com/angularpractice/'
    title = 'ProtoCommerce'

    home_page_data = [
        {'name': 'Alex', 'email': 'ex@mail.fu', 'password': '123', 'gender': 'Male', 'status': 'student', 'date': '03-01-1992'},
        {'name': 'Nina', 'email': 'ex@mail.fu', 'password': '123', 'gender': 'Female', 'status': 'employed', 'date': '03-01-3002'}
    ]

    """locators"""
    name_field = (By.CSS_SELECTOR, 'input[name="name"]')
    email_field = (By.CSS_SELECTOR, 'input[name="email"]')
    password_field = (By.CSS_SELECTOR, '#exampleInputPassword1')
    checkbox_i_love_icecream = (By.CSS_SELECTOR, '#exampleCheck1')
    gender_field = (By.ID, 'exampleFormControlSelect1')
    employment_checkboxes = (By.CSS_SELECTOR, 'div.form-group div input')
    submit_button = (By.CSS_SELECTOR, "input[value='Submit']")
    alert_success_message = (By.CSS_SELECTOR, "[class*='alert-success']")
    close_alert = (By.CSS_SELECTOR, '.close')
    field_date = (By.NAME, 'bday')
    alert_danger = (By.CSS_SELECTOR, '.alert-danger')
    shop_button = (By.LINK_TEXT, 'Shop')

    @allure.step
    def alert_name_is_required(self):
        alert_text = self.browser.find_element(*HomePage.alert_danger).text
        text = 'Name is required'
        assert self.is_element_present(*HomePage.alert_danger) and alert_text == text, \
            f'Alert danger not present or alert text: {alert_text} not equal {text}'


    @allure.step
    def alert_name_should_be_at_least_2_characters_is_present(self):
        alert_text = self.browser.find_element(*HomePage.alert_danger).text
        text = 'Name should be at least 2 characters'
        assert self.is_element_present(*HomePage.alert_danger) and alert_text == text,\
            f'Alert danger not present or alert text: {alert_text} not equal {text}'

    @allure.step
    def alert_name_should_be_at_least_2_characters_is_disappeared(self):
        assert self.is_disappeared(*HomePage.alert_danger)


    @allure.step
    def alert_success_is_disappeared(self):
        close_alert_button = self.browser.find_element(*HomePage.close_alert)
        close_alert_button.click()
        assert self.is_disappeared(*HomePage.alert_success_message)

    @allure.step
    def alert_success_is_present(self):
        assert self.is_element_present(
            *HomePage.alert_success_message), f'Cant find success message {HomePage.alert_success_message}'

    @allure.step
    def clear_name_field(self):
        name_field = self.browser.find_element(*HomePage.name_field)
        name_field.send_keys(Keys.BACK_SPACE*2)
        name_field_text = name_field.get_attribute('value')
        assert name_field_text == '', "Name field is not empty"

    @allure.step
    def fill_name_field(self, name):
        name_field = self.browser.find_element(*HomePage.name_field)
        name_field.send_keys(name)

    @allure.step
    def fill_name_email_password_field(self, firstname, email, password):
        send_name = self.browser.find_element(*HomePage.name_field)
        send_name.send_keys(firstname)
        send_name_text = send_name.get_attribute('value')
        assert send_name_text == firstname, f'Actual name in field {send_name_text} should be {firstname}'
        send_email = self.browser.find_element(*HomePage.email_field)
        send_email.send_keys(email)
        send_email_text = send_email.get_attribute('value')
        assert send_email_text == email, f'Actual name in field {send_email_text} should be {email}'
        send_password = self.browser.find_element(*HomePage.password_field)
        send_password.send_keys(password)
        send_password_text = send_password.get_attribute('value')
        assert send_password_text == password, f'Actual name in field {send_password_text} should be {password}'

    @allure.step
    def go_to_shop(self):
        from Pages.shop_page import ShopPage
        button = self.browser.find_element(*HomePage.shop_button)
        button.click()
        return ShopPage(self.browser, ShopPage.link)


    @allure.step
    def push_submit_button(self):
        button = self.browser.find_element(*HomePage.submit_button)
        button.click()
        self.alert_success_is_present()

    @allure.step
    def select_checkbox_i_love_icecream(self):
        checkbox = self.browser.find_element(*HomePage.checkbox_i_love_icecream)
        checkbox.click()
        assert checkbox.is_selected(), 'Ice Cream Checkbox is not selected'

    @allure.step
    def select_gender(self, gender):
        select = Select(self.browser.find_element(*HomePage.gender_field))
        select.select_by_visible_text(gender)
        select_text = self.browser.find_element(*HomePage.gender_field).get_attribute('value')
        assert select_text == gender, f'Actual gender is {select_text}, should be {gender}'

    @allure.step
    def select_employment_status(self, status):
        checkboxes = self.browser.find_elements(*HomePage.employment_checkboxes)
        if status == 'student':
            checkboxes[0].click()
            assert checkboxes[0].is_selected(), f'Checkbox is not selected {status}'
        elif status == 'employed':
            checkboxes[1].click()
            assert checkboxes[1].is_selected(), f'Checkbox is not selected {status}'
        else:
            raise AssertionError(f'Wrong employment_status {status}')

    @allure.step
    def send_date_of_birth(self, date_birth):
        date = self.browser.find_element(*HomePage.field_date)
        date.send_keys(date_birth)
        date_value = date.get_attribute('value')
        reverse_date = f'{date_birth[6:10]}-{date_birth[3:5]}-{date_birth[0:2]}'
        assert date_value == reverse_date, f'{date_value} not equal {reverse_date}'
