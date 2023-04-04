from selenium import webdriver

from pages.making_order_page import Making_order
from pages.product_page import Product
from pages.product_select_page import Product_select
from pages.start_page import Start_page


def test_buy_product(set_up):
    driver = driver = webdriver.Firefox(executable_path='C:\\Users\\chelo\\PycharmProjects\\resours\\geckodriver.exe')

    st = Start_page(driver)
    st.search_of_product()

    psp = Product_select(driver)
    psp.filters_and_product()
    price_1 = psp.return_price_in_select()
    print("Цена товара на странице сортировки товаров " + price_1)
    psp.go_to_product_page()

    pp = Product(driver)
    price_2 = pp.return_price_from_description()
    print("Цена товара на странице товара " + price_2)
    pp.add_product_to_cart()

    pp.assert_price(price_1, price_2)

    mop = Making_order(driver)
    mop.make_order()
    price_3 = mop.return_result_price()
    price_3 = price_3[11:]
    print("Цена продукта на странице в корзиной " + price_3)

    mop.assert_price(price_2, price_3)




