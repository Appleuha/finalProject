from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Product(Base):

    def __init__(self, driver):
       super().__init__(driver)

    #locators

    button_add_to_cart = "//div[@class='kant__product__buy__button--new']"
    button_go_to_cart = "//div[@class='kant__product__buy kant__product__buy--active js__add-to-basket--filled']"
    price = "//span[@class='kant__product__price__new kant__price']"

    #getters

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))
    def get_button_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_cart)))
    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))


    #actions
    def add_to_cart(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 300)
        self.get_button_add_to_cart().click()
        print("Товар добавлен в корзину")

    def go_to_cart(self):
        self.get_button_go_to_cart().click()
        print("Переход в корзину")

    def return_price_from_description(self):
        return self.get_price().text


    #methods

    def add_product_to_cart(self):
        self.get_url()
        self.add_to_cart()
        self.go_to_cart()
