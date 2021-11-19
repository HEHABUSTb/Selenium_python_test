import allure

from Pages.base_page import BasePage
from Pages.locators import ShopPageLocators


class ShopPage(BasePage):
    link = 'https://rahulshettyacademy.com/angularpractice/shop'
    title = 'ProtoCommerce'

    @allure.step
    def go_to_home_page(self):
        from Pages.home_page import HomePage
        home_button = self.browser.find_element(*ShopPageLocators.home_button)
        home_button.click()
        home_page = HomePage(self.browser, HomePage.link)
        return home_page

