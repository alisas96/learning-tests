from selenium.webdriver.common.by import By 


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
	LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
	ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
	PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
	PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
	PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert-success strong')
	BASKET_PRICE = (By.CSS_SELECTOR, '#messages .alert-info strong')
	