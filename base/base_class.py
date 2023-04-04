import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Метод для получения URL"""
    def get_url(self):
        url = self.driver.current_url
        print("Полученный url " + url)

    """Метод для сравнения assert"""
    def assert_price(self, price_1, price_2):
        try:
            assert price_1 == price_2
            print('Цены совпадают')
        except AssertionError:
            print("Цены не совадают!")

    """Метод для скриншота"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'  # можно так называть скриншот с названием теста, чтобы потом не запутаться. если без даты скриншот указывать, то он будет пересохраняться
        self.driver.save_screenshot('C:\\Users\\chelo\\PycharmProjects\\finalProject\\screen\\' + name_screenshot)

    """Метод для сравнения url assert"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL совпали")





