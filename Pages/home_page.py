from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Pages.base_page import BasePage
import allure
import pytest

@pytest.mark.usefixtures('browser')
class HomePage(BasePage):

    link = 'https://rahulshettyacademy.com/angularpractice/'

    home_page_data = [
        {'name': 'Alex', 'email': 'ex@mail.fu', 'password':'123', 'gender': 'Male', 'status':'student'},
        {'name': 'Nina', 'email': 'ex@mail.fu', 'password':'123', 'gender': 'Female', 'status':'employed'}
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

    @allure.step
    def fill_name_email_password_field(self, firstname, email, password):
        send_name = self.browser.find_element(*HomePage.name_field)
        send_name.send_keys(firstname)
        send_email = self.browser.find_element(*HomePage.email_field)
        send_email.send_keys(email)
        send_password = self.browser.find_element(*HomePage.password_field)
        send_password.send_keys(password)

    @allure.step
    def select_checkbox_i_love_icecream(self):
        self.browser.find_element(*HomePage.checkbox_i_love_icecream).click()

    @allure.step
    def select_gender(self, gender):
        select = Select(self.browser.find_element(*HomePage.gender_field))
        select.select_by_visible_text(gender)

    @allure.step
    def select_employment_status(self, status):
        checkboxes = self.browser.find_elements(*HomePage.employment_checkboxes)
        if status == 'student':
            checkboxes[0].click()
        elif status == 'employed':
            checkboxes[1].click()
        else:
            raise AssertionError(f'Wrong employment_status {status}')

    @allure.step
    def push_submit_button(self):
        button = self.browser.find_element(*HomePage.submit_button)
        button.click()

    @allure.step
    def alert_success_is_present(self):
        assert self.is_element_present(*HomePage.alert_success_message), f'Cant find success message {HomePage.alert_success_message}'

