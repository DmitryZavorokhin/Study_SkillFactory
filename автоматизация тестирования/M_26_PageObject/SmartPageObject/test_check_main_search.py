from .MainPage import  MainPage

def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() == 48

    # Проверяем наличие в названии слова iphone
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'iphone' in title.lower(), msg




def test_check_sort_by_price(web_browser):
    """ Проверка сортировки продуктов
    """

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()

    # Прокрутка до элемента, чтобы он стал виден пользователю
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Получение цен всех выведенных продуктов
    all_prices = page.products_prices.get_text()

    # Конвертирование всех цен из строк в числа
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"