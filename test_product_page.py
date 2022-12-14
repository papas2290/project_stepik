from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.save_product_name()
    page.save_price_product()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.must_be_the_name_of_the_product()
    page.must_be_price_basket_equal_price_product()
