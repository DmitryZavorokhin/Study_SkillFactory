from selenium.webdriver.common.by import By
class LocatorsPetFriends:
    HEADER = (By.CSS_SELECTOR, "nav[class='navbar.navbar-expand-lg.navbar-light.bg-light.marked-element']")
    LOGO = ( By.CSS_SELECTOR, "a[class = 'navbar-brand.header2']")
    MENU = (By.ID, "navbarNav")
    BUTTON_EXIT = (By.XPATH, "div:nth-of-type(2) > button[class='btn.btn-success']")