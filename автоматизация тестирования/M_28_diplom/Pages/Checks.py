# from M_28_diplom.Pages.Locators import AuthLocators
# from M_28_diplom.Pages.Conf import browser
#
# class ChecksTests(browser):
#     def __init__(self, driver):
#         driver.implicitly_wait(10)
#
#     def active_email(self,driver):
#         active_locator = driver.find_elements(*AuthLocators.ACTIVE_FIELD_MAIL_IN_AUTH)
#         return [x.text for x in active_locator]
#
#     def LK(self,driver):
#         lk = driver.find_elements(*AuthLocators.LK)
#         return [x.text for x in lk]