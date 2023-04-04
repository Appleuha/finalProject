import time

from selenium.common import MoveTargetOutOfBoundsException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from base.base_class import Base
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium import webdriver


class Product_select(Base):

    def __init__(self, driver):
       super().__init__(driver)

    #locators
    button_close_notice = "//div/div[@class='popmechanic-close']"
    field_brand = "//input[@id='kantFilterBrand']"
    brand_salomon = "//div/div[@data-value='salomon']"
    field_max_price = "//input[@name='price_max']"
    availability_in_shops = "(//div[@class='kant__filter kant__filter--checkbox kant__filter--closed js__filter__open'])[1]"
    shop_msk_tim = "//div[@data-value='moskva_m_timiryazevskaya']"
    shop_msk_nag = "//div[@data-value='moskva_m_nagornaya']"
    third_product = "(//div[@class='kant__catalog__item-image'])[3]"
    third_product_button = "(//div[@class='kant__button'])[3]"
    price = "(//div/span[@class='kant__price'])[4]"

    #getters

    def get_button_close_notice(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close_notice)))

    def get_field_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_brand)))

    def get_check_box_brand_salomon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_salomon)))

    def get_field_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_max_price)))

    def get_availability_in_shops(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.availability_in_shops)))

    def get_shop_msk_tim(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_msk_tim)))

    def get_shop_msk_nag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_msk_nag)))

    def get_third_product_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.third_product_button)))

    def get_third_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.third_product)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))


    #actions

    def close_notice(self):
        self.get_button_close_notice().click()
        print("Закрытие уведомления с предложением акции")

    def input_brand_filter(self):
        self.get_field_brand().send_keys("Salomon")
        print("Ввод в поле для поиска бренда 'Salomon'")

    def choose_checkbox_brand_salomon(self):
        self.get_check_box_brand_salomon().click()
        print("Выбор в списке брендов Salomon")

    def clear_field_max_price(self):
        self.get_field_max_price().click()
        self.get_field_max_price().send_keys(Keys.CONTROL + "a")
        self.get_field_max_price().send_keys(Keys.DELETE)
        print("Очищение поля для ввода максимальной цены")

    def input_max_price(self, max_price):
        self.get_field_max_price().send_keys(max_price)
        self.get_field_max_price().send_keys(Keys.ENTER)
        print("Ввод максимальной цены")

    def click_on_availability_in_shops(self):
        self.get_availability_in_shops().click()
        print("Нажатие на надпись 'Наличие в магазинах'")

    def choose_shop_msk_tim(self):
        self.get_shop_msk_tim().click()
        print("Выбор магазина в Москве на м.Тимирязевская")

    def choose_shop_msk_nag(self):
        self.get_shop_msk_nag().click()
        print("Выбор магазина в Москве на м.Нагорная")

    def choose_third_product(self):
        self.scroll_to_element(self.driver, self.get_third_product())
        self.get_third_product_button().click()
        print("Выбор третьего товара")

    def return_price_in_select(self):
        return self.get_price().text

    def scroll_to_element(self, driver, element_locator):
        actions = ActionChains(driver)
        try:
            actions.move_to_element(self.get_third_product()).perform()
        except MoveTargetOutOfBoundsException as e:
            print(e)
            driver.execute_script("arguments[0].scrollIntoView(true);", element_locator)





    #methods

    def filters_and_product(self):
        self.get_url()
        self.close_notice()
        time.sleep(5)
        self.input_brand_filter()
        time.sleep(5)
        self.choose_checkbox_brand_salomon()
        self.clear_field_max_price()
        self.input_max_price("20000")
        self.click_on_availability_in_shops()
        self.choose_shop_msk_tim()
        self.choose_shop_msk_nag()
        self.scroll_to_element(self.driver, self.get_third_product())

    def go_to_product_page(self):
        time.sleep(2)
        self.get_screenshot()
        self.choose_third_product()