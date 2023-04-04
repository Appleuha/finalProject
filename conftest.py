import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print('Start Test')
    yield
    # driver.quit()
    print('Finish Test')
