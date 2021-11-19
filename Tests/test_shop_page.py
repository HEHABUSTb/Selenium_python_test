from Pages.shop_page import ShopPage


def test_shop(browser):
    shop_page = ShopPage(browser, ShopPage.link)
    shop_page.open()
