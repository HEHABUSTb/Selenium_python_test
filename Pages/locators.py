from selenium.webdriver.common.by import By

class ShopPageLocators():

    alert_success = (By.CSS_SELECTOR, "div[class*='alert-success']")
    checkout_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    checkbox_i_agree = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    checkbox_i_agree_hide = (By.ID, 'checkbox2')
    go_to_cart_button = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    home_button = (By.LINK_TEXT, 'Home')
    location = (By.ID, 'country')
    phones_list = (By.CSS_SELECTOR, 'app-card-list app-card')
    phones_name = (By.CSS_SELECTOR, 'div div h4 a')
    phones_price = (By.CSS_SELECTOR, 'div div h5')
    phones_add_button = (By.CSS_SELECTOR, '.card-footer button')
    phones_names_in_cart = (By.CSS_SELECTOR, "h4[class='media-heading'] a")
    total_in_cart = (By.CSS_SELECTOR, 'td h3 strong')




    purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")