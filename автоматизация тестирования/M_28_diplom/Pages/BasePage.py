from selenium import webdriver
from .Settings import base_url

class BasePage:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(executable_path='/user/d"&"v/Documents/chromedriver')
        self.base_url = base_url

