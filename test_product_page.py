#from .pages.main_page import MainPage
#from .pages.login_page import LoginPage
import pytest
import time
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser,link):
 #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
 page=ProductPage(browser,link)
 page.open()
 time.sleep(3)
 page.add_button_actions()
 page.names_matched
 
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
  link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
  page=ProductPage(browser,link)
  page.open()
  page.add_button_actions()
  time.sleep(3)
  page.cant_see_success_message_after_adding_product_to_basket()
  
@pytest.mark.xfail
def test_guest_cant_see_success_message(browser): 
  link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
  page=ProductPage(browser,link)
  page.open()
  page.cant_see_success_message()
  
@pytest.mark.three
def test_message_disappeared_after_adding_product_to_basket(browser):
  link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
  page=ProductPage(browser,link)
  page.open()
  page.add_button_actions()
  page.message_disappeared_after_adding_product_to_basket()