from selenium.webdriver.common.by import By
from _Webinar_basepage import BasePage

class YaSearchPageLocator:
    LOCATOR_NAVI_BAR = (By.CSS_SELECTOR, ".service__name")

class SearchPageHelper(BasePage):
    def CheckNaviBar(self):
        all_list =self.find_elements(YaSearchPageLocator.LOCATOR_NAVI_BAR)
        return [x.text for x in all_list]