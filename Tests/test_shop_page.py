import pytest
from Pages.shop_page import ShopPage

@pytest.mark.usefixtures('browser')
class Test_Shop_Page():

    def test_shop(self):
        shop_page = ShopPage(self.browser, ShopPage.link)
        shop_page.open()
