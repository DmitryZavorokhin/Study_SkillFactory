from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_EMAIL = By.XPATH, "//input[@id='username']"
    AUTH_PASS = By.ID, "password"
    AUTH_BTN = By.ID, "kc-login"
    REGISTRATION_LINK = By.ID,"kc-register"
    FORGOT_PASSWORD = By.ID, "forgot_password"
    NAME_REG = By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container register-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='register-form']/div[@class='name-container']/div[1]/div[1]/input[1]"
    SURNAME_REG = By.CSS_SELECTOR, "div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.name-container:nth-child(2) div.rt-input-container:nth-child(2) div.rt-input.rt-input--rounded.rt-input--orange > input.rt-input__input.rt-input__input--rounded.rt-input__input--orange"
    EMAIL_REG = By.XPATH, "//input[@id='address']"
    PASS_REG = By.XPATH, "//input[@id='password']"
    CONFIRM_PASS_REG = By.XPATH, "//input[@id='password-confirm']"
    BTN_REG = By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]'
    SELECT_TEL_AUTH = By.ID, "t-btn-tab-phone"
    SELECT_MAIL_AUTH = By.ID, "t-btn-tab-mail"
    SELECT_LOGIN_AUTH = By.ID, "t-btn-tab-login"
    SELECT_LS_AUTH = By.ID, "t-btn-tab-ls"
    NUM_INPUT_REG_0 = By.XPATH, '//*[@id="rt-code-0"]'
    NUM_INPUT_FIELD = By.XPATH, '//*[@id="page-right"]/div/div/h1'
    ACTIVE_FIELD_MAIL_IN_AUTH = By.XPATH, '//*[@id="t-btn-tab-mail" and @class="rt-tab rt-tab--small rt-tab--active"]'
    LK = By.XPATH,'//*[@id="app"]/main/div/div[2]/div[3]/h3'
    EXIT_LK = By.ID, 'logout-btn'
    LITTLE_NAME = By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span'# Необходимо заполнить поле кириллицей. От 2 до 30 символов.
    NOT_SAME_PASSW = By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span' # Пароли не совпадают
    LITTLE_PASSW = By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span' # Длина пароля должна быть не менее 8 символов
    SAME_USER = By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2' # Учётная запись уже существует
    WRONG_REG_EMAIL = By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/span' # Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru
    PASS_MORE_20_SIMBOLS = By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span'  # Длина пароля должна быть не более 20 символов
    WRONG_AUTH_PASS = By.XPATH, '//*[@id="form-error-message"]' # Неверный логин или пароль





