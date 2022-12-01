from .base_page import BasePage
from .locatores import ProductPageLocators


class ProductPage(BasePage):
    def save_product_name(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return self.product_name

    def save_price_product(self):
        self.product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        return self.product_price

    def add_product_to_cart(self):
        button_add = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button_add.click()

    # Проверка наличия названия товара в сообщении об успешной добавке в корзину
    def must_be_the_name_of_the_product(self):
        name_product = self.browser.find_elements(*ProductPageLocators.MESSAGES_IN_THE_BASKET)
        name_product = name_product[0].text
        assert self.product_name in name_product, f'Имя <{self.product_name}> не найдено в сообщении об успешной добавке'

    # Цена корзины должна быть равна стоимости товара
    def must_be_price_basket_equal_price_product(self):
        basket_product = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        basket_product = basket_product.text
        assert basket_product in self.product_price, f'Цена в корзине <{basket_product}> не соответствует цене ' \
                                                     f'товара <{self.product_price}>'
