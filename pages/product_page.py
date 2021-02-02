from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
 def add_button_actions(self):
  name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
  assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket-button is not presented"
  basket=self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
  basket.click()
  self.solve_quiz_and_get_code()

  added=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDING_MESSAGE).text
  assert name==added, "Product name is not matching product name after adding to basket"
