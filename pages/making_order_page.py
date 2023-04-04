from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Making_order(Base):

    def __init__(self, driver):
       super().__init__(driver)

    #locators

    button_no_authorization = "//div/div[@class='kant__button-link kant__button-link--not-authorized']"
    continue_button = "//button[@class='popup__input-button popup__input-button--flex js__button-show-form']"
    result_price = "(//div/div[@class='kant__basket-price'])[2]"


    #getters

    def get_button_no_authorization(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_no_authorization)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_result_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.result_price)))


    #actions

    def click_button_no_authorization(self):
        self.get_button_no_authorization().click()
        print("Нажатие на кнопку 'Продолжить без регистрации'")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Нажатие на кнопку 'Продолжить'")

    def return_result_price(self):
        return self.get_result_price().text

    #methods
    def make_order(self):
        self.get_url()
        self.click_button_no_authorization()
        self.click_continue_button()


