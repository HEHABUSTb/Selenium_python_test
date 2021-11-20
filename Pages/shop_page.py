import time
import allure
import pytest
from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from Pages.locators import ShopPageLocators


class ShopPage(BasePage):
    link = 'https://rahulshettyacademy.com/angularpractice/shop'
    title = 'ProtoCommerce'

    shop_page_data = [{'phone_model': ['iphone X'], 'country': 'Russia'},
                      {'phone_model': ['iphone X', 'Samsung Note 8', 'Nokia Edge', 'Blackberry'], 'country': 'India'}
                      ]

    @allure.step
    def add_phones_in_cart(self, phones_names):
        phones = self.browser.find_elements(*ShopPageLocators.phones_list)
        dict_phones = {}

        for phone in phones:
            phone_model = phone.find_element(*ShopPageLocators.phones_name).text
            phone_price = phone.find_element(*ShopPageLocators.phones_price).text
            if phone_model in phones_names:
                dict_phones[phone_model] = phone_price
                add_button = phone.find_element(*ShopPageLocators.phones_add_button)
                add_button.click()

        checkout_text = self.browser.find_element(*ShopPageLocators.go_to_cart_button).text
        len_phones_names = str(len(phones_names))
        assert len_phones_names in checkout_text, f'Looks like {checkout_text} dont increase after add to cart, should be {len_phones_names}'
        return dict_phones

    @allure.step
    def check_names_of_phones_in_cart(self, dict_phones):
        phones_names_in_cart = self.browser.find_elements(*ShopPageLocators.phones_names_in_cart)
        for name in phones_names_in_cart:
            if name.text not in dict_phones:
                raise AssertionError(f'{name.text} not in {dict_phones}')
        assert len(phones_names_in_cart) == len(dict_phones), f'Items in cart {len(phones_names_in_cart)} should be {len(dict_phones)}'

    @allure.step
    def check_prices_of_phones_in_cart(self, phones_name):
        pass

    @allure.step
    def choose_location(self, country):
        location = self.browser.find_element(*ShopPageLocators.location)
        location.send_keys(country[0:3])
        self.ec_wait(By.LINK_TEXT, country)
        select_country = self.browser.find_element(By.LINK_TEXT, country)
        select_country.click()
        location = location.get_attribute('value')
        assert location == country, f'Current location {location} not equal data {country}'


    @allure.step
    def go_to_home_page(self):
        from Pages.home_page import HomePage
        home_button = self.browser.find_element(*ShopPageLocators.home_button)
        home_button.click()
        home_page = HomePage(self.browser, HomePage.link)
        return home_page

    @allure.step
    def go_to_cart(self):
        checkout_button = self.browser.find_element(*ShopPageLocators.go_to_cart_button)
        checkout_button.click()

    @allure.step
    def push_checkout_button(self):
        checkout_button = self.browser.find_element(*ShopPageLocators.checkout_button)
        checkout_button.click()

    @allure.step
    def push_purchase_button(self):
        button = self.browser.find_element(*ShopPageLocators.purchase_button)
        button.click()
        assert self.is_element_present(*ShopPageLocators.alert_success), 'Alert success is not present'

    @allure.step
    def select_checkbox_i_agree(self):
        checkbox = self.browser.find_element(*ShopPageLocators.checkbox_i_agree)
        checkbox.click()
        hide_checkbox = self.browser.find_element(*ShopPageLocators.checkbox_i_agree_hide)
        assert hide_checkbox.is_selected(), 'Checkbox is not selected'
