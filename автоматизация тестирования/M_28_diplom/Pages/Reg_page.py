from M_28_diplom.Pages.Locators import AuthLocators

class RegPage:

    def __init__(self, driver,timeout=10):
        self.name = driver.find_element(*AuthLocators.NAME_REG)
        self.surname = driver.find_element(*AuthLocators.SURNAME_REG)
        self.email = driver.find_element(*AuthLocators.EMAIL_REG)
        self.pass1 = driver.find_element(*AuthLocators.PASS_REG)
        self.pass2 = driver.find_element(*AuthLocators.CONFIRM_PASS_REG)
        self.submit = driver.find_element(*AuthLocators.BTN_REG)

    def enter_name(self, value):
        self.name.send_keys(value)


    def enter_surname(self, value):
        self.surname.send_keys(value)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.pass1.send_keys(value)

    def enter_pass2(self, value):
        self.pass2.send_keys(value)

    def btn_click(self):
        self.submit.click()

    def reg_code(self,driver):
        code = driver.find_elements(*AuthLocators.NUM_INPUT_FIELD)
        return [x.text for x in code]


    def allert_name(self,driver):
        too_litle_name_allert = driver.find_elements(*AuthLocators.LITTLE_NAME)
        return [x.text for x in too_litle_name_allert]

    def allert_not_same_passw(self,driver):
        not_same_reg_passw = driver.find_elements(*AuthLocators.NOT_SAME_PASSW)
        return [x.text for x in not_same_reg_passw]

    def allert_little_passw(self,driver):
        little_reg_passw = driver.find_elements(*AuthLocators.NOT_SAME_PASSW)
        return [x.text for x in little_reg_passw]

    def allert_same_user(self,driver):
        reg_same_user = driver.find_elements(*AuthLocators.SAME_USER)
        return [x.text for x in reg_same_user]

    def allert_wrong_reg_email(self,driver):
        reg_wrong_email = driver.find_elements(*AuthLocators.WRONG_REG_EMAIL)
        return [x.text for x in reg_wrong_email]

    def allert_passw_more_20_simbols(self,driver):
        reg_bad_and_big_passw = driver.find_elements(*AuthLocators.PASS_MORE_20_SIMBOLS)
        return [x.text for x in reg_bad_and_big_passw]




