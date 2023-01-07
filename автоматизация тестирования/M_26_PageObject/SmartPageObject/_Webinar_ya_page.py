from selenium.webdriver.common.by import By
from _Webinar_basepage import BasePage


class YaSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.XPATH, '//*[@id="text"]')
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.XPATH, "/html/body/main/div[2]/form/div[3]/button" )


class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(YaSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send.keys(word)
        return search_field

    def click_button(self):
        return self.find_element(YaSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

