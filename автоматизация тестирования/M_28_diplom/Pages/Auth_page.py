from M_28_diplom.Pages.Settings import base_url
from M_28_diplom.Pages.Locators import AuthLocators


class AuthPage():

    def __init__(self, driver,timeout=10):
        url = base_url
        driver.get(url)
        driver.implicitly_wait(10)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.passw = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.registration = driver.find_element(*AuthLocators.REGISTRATION_LINK)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.passw.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def link_reg(self):
        self.registration.click()

    def active_email(self,driver):
        active_locator = driver.find_elements(*AuthLocators.ACTIVE_FIELD_MAIL_IN_AUTH)
        return [x.text for x in active_locator]

    def LK(self,driver):
        lk = driver.find_elements(*AuthLocators.LK)
        return [x.text for x in lk]

    def logout_lk(self,driver):
        exit = driver.find_element(*AuthLocators.EXIT_LK).click()


    def wrong_passw(self, driver):
        allert = driver.find_elements(*AuthLocators.WRONG_AUTH_PASS)
        return [x.text for x in allert]





