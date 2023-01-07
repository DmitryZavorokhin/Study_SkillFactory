import pytest
from selenium import  webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path='/user/d"&"v/Documents/chromedriver')
    yield driver
    driver.quit()