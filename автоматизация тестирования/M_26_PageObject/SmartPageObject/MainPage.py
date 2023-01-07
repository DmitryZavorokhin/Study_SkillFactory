from M_26_PageObject.pages.base_page import BasePage
from base import WebPage
import os
from elements import WebElement, ManyWebElements

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)

    # поле поиска
    search = WebElement(id='header-search')

    # кнопка поиска
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Название продуктов  в списке
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Кнопка сортировки по цене
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Цены продукта
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')