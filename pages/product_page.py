from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
 def add_button_actions(self):
  assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket-button is not presented"
  basket=self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
  basket.click()
  self.solve_quiz_and_get_code()
