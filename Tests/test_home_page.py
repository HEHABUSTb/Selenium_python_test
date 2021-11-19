import time

from selenium.webdriver.common.by import By
from Pages.home_page import HomePage



import pytest



@pytest.mark.usefixtures('browser')
class Test_Home_Page():

    @pytest.fixture(params=HomePage.home_page_data)
    def get_data(self, request):
        return request.param

    @pytest.mark.smoke
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









