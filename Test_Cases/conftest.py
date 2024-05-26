from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    ser_obj = Service("C:\\All Project\\software\\chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    driver.implicitly_wait(20)
    driver.maximize_window()
    return driver