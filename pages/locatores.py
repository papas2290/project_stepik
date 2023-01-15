from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRICE_PRODUCT = (By.XPATH, "//p[@class='price_color']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Добавить в корзину']")
    MESSAGES_IN_THE_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRICE_BASKET = (By.XPATH, "//p[contains(text(), 'Стоимость корзины теперь составляет')]/strong")
