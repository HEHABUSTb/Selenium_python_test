from Pages.base_page import BasePage

from Pages.locators import ShopPageLocators


class ShopPage(BasePage):
    link = 'https://rahulshettyacademy.com/angularpractice/shop'
    title = 'ProtoCommerce'

    def go_to_home_page(self):
        home_button = self.browser.find_element(*ShopPageLocators.home_button)
        home_button.click()

