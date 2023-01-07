from selenium import webdriver

class BasePage:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/user/d"&"v/Documents/chromedriver')
        self.base_url = "https://petfriends.skillfactory.ru/all_pets"