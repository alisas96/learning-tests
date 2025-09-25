from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
	def add_product_to_busket(self):
		add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
		add_product_button.click()

	def should_be_correct_product_name(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		product_name_in_basket = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME_IN_BASKET)).text
		assert product_name == product_name_in_basket, \
            f"Expected product name '{product_name}', but got '{product_name_in_basket}'"
		
	def should_be_correct_product_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		basket_price = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.BASKET_PRICE)
        ).text
		assert product_price == basket_price, \
            f"Expected basket price '{product_price}', but got '{basket_price}'"
		
	
	
