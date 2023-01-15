from .pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('promo_offer', [el for el in (range(0, 10))])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.save_product_name()
    page.save_price_product()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.must_be_the_name_of_the_product()
    page.must_be_price_basket_equal_price_product()
