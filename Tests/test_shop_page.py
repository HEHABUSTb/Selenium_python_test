import time
import allure
import pytest
from Pages.shop_page import ShopPage

@pytest.mark.usefixtures('browser')
@pytest.mark.ShopPage
@pytest.mark.All
@allure.severity(allure.severity_level.NORMAL)
class Test_Shop_Page():

    @pytest.fixture(params=ShopPage.shop_page_data)
    def get_data(self, request):
        return request.param

    def test_shop(self, get_data):
        shop_page = ShopPage(self.browser, ShopPage.link)
        shop_page.open()
        dict_phones = shop_page.add_phones_in_cart(get_data['phone_model'])
        shop_page.go_to_cart()
        shop_page.check_names_of_phones_in_cart(dict_phones)
        shop_page.check_prices_of_phones_in_cart(dict_phones)
        shop_page.push_checkout_button()
        shop_page.choose_location(get_data['country'])
        shop_page.select_checkbox_i_agree()
        shop_page.push_purchase_button()

