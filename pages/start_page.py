from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Start_page(Base):
    url = 'https://www.kant.ru/'
    def __init__(self, driver):
        super().__init__(driver)


    #locators

    button_close_notice = "//a[@class='popmechanic-submit popmechanic-submit-main']"
    search_field = "(//input[@placeholder='Поиск по сайту'])[1]"
    button_search = "(//input[@type='submit'])[1]"


    #getters

    def get_notice(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close_notice)))

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_button_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_search)))

    #actions

    """Закрытие уведомлении о предложении подписаться на новости"""
    def close_notice(self):
        self.get_notice().click()
        print("Закрыто уведомление с предложением о подписке")

    def input_search_field(self, product):
        self.get_search_field().send_keys(product)
        print("Ввод названия товара")

    def click_button_search(self):
        self.get_button_search().click()
        print("Нажатие на кнопки поиска")

    def click_Enter_in_search_field(self):
        self.get_search_field().send_keys(Keys.ENTER)
        print("Нажатие кнопки Enter в поле для поиска товара")







    #methods
    def search_of_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_url()
        self.close_notice()
        self.input_search_field("Кроссовки треккинговые")
        self.click_Enter_in_search_field()
        # self.assert_url('https://www.kant.ru/search/?q=%D0%9A%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8+%D1%82%D1%80%D0%B5%D0%BA%D0%BA%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D1%8B%D0%B5')
        # self.get_search_field().send_keys(Keys.ENTER)

        # self.click_button_search()





