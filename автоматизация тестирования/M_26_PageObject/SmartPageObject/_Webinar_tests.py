from M_26_PageObject.SmartPageObject._Webinar_searchPage import SearchPageHelper
from M_26_PageObject.SmartPageObject._Webinar_ya_page import SearchHelper
from M_26_PageObject.SmartPageObject._Webinar_conftest import browser


def test_search(browser):
    ya_main_page = SearchHelper(browser)
    ya_search_page = SearchPageHelper(browser)
    ya_main_page.go_to()
    ya_main_page.enter_word("Человек-мотылёк")
    ya_main_page.click_button()
    elements = ya_search_page.CheckNaviBar()
    assert "Картинка" and "Видео" in elements
