import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.home_page import HomePage
from Pages.shop_page import ShopPage



import pytest




@pytest.mark.usefixtures('browser')
@pytest.mark.HomePage
@pytest.mark.All
class Test_Home_Page():

    @pytest.fixture(params=HomePage.home_page_data)
    def get_data(self, request):
        return request.param

    def test_smoke_home_page(self, get_data):
        home_page = HomePage(self.browser, HomePage.link)
        home_page.open()
        home_page.fill_name_email_password_field(get_data['name'], get_data['email'], get_data['password'])
        home_page.select_checkbox_i_love_icecream()
        home_page.select_gender(get_data['gender'])
        home_page.select_employment_status(get_data['status'])
        home_page.send_date_of_birth(get_data['date'])
        home_page.push_submit_button()
        home_page.alert_success_is_disappeared()

    def test_alert_danger_name(self):
        home_page = HomePage(self.browser, HomePage.link)
        home_page.open()
        home_page.fill_name_email_password_field('1', 'email', 'password')
        home_page.alert_name_should_be_at_least_2_characters_is_present()
        home_page.fill_name_field('A')
        home_page.alert_name_should_be_at_least_2_characters_is_disappeared()
        home_page.clear_name_field()
        home_page.alert_name_is_required()

    def test_guest_can_go_to_shop_page_and_back_to_home_page(self):
        home_page = HomePage(self.browser, HomePage.link)
        home_page.open()
        home_page.check_title(HomePage.title)

        shop_page = home_page.go_to_shop()
        shop_page.check_title(ShopPage.title)

        home_page = shop_page.go_to_home_page()
        home_page.check_title(HomePage.title)
