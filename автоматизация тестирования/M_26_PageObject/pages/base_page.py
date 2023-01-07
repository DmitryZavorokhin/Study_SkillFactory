from urllib.parse import urlparse
from selenium import webdriver

class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидани элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = webdriver.Chrome('/user/d"&"v/Documents/chromedriver.exe')
        self.url = url
        self.driver.implicitly_wait(timeout)


    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
