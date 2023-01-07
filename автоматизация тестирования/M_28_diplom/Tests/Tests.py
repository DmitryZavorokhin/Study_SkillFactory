from M_28_diplom.Pages.Settings import valid_email,latin_name, boundary_little_surname, too_big_passw, password_without_lower_case, valid_name_31_simbols, valid_name_30_simbols,  email_without_dog, too_litle_name, valid_password, valid_surname, valid_name, boundary_little_name, valid_email_temp, incorrect_password, little_password
from M_28_diplom.Pages.Reg_page import RegPage
from M_28_diplom.Pages.Auth_page import AuthPage
from M_28_diplom.Pages.Conf import browser

# 1
"""Тест активации селектора типа учетной записи в  зависимости от вводных данный в поле логина"""
def test_auth_active_form(browser):
   auth_page = AuthPage(browser)
   auth_page.enter_email(valid_email)
   auth_page.enter_pass("")
   mail = auth_page.active_email(browser)
   assert "Почта" in mail
# 2  Тест входа в учетную запись по зарегистрированной почте
def test_auth_valid_login_password(browser):
   auth_page = AuthPage(browser)
   auth_page.enter_email(valid_email)
   auth_page.enter_pass(valid_password)
   auth_page.btn_click()
   lk = auth_page.LK(browser)
   assert  "Личные кабинеты" in lk
   auth_page.logout_lk(browser)
# 3  Тест регистрации валидными символами с коротким именем
def test_reg_1_simbol_name(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(too_litle_name)
   reg_page.enter_surname("")
   allert_litle = reg_page.allert_name(browser)
   assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in allert_litle
# 4 Тест отсылки письма подтверждения при регистрации с валидными данными
def test_reg_valid_data(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(boundary_little_name)
   reg_page.enter_surname(valid_surname)
   reg_page.enter_email(valid_email_temp)
   reg_page.enter_pass(valid_password)
   reg_page.enter_pass2(valid_password)
   reg_page.btn_click()
   code = reg_page.reg_code(browser)
   assert "Подтверждение email" in code
# 5 Тест проверки правильности повторного ввода пароля
def test_reg_not_same_password(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(valid_name)
   reg_page.enter_surname(boundary_little_surname)
   reg_page.enter_email(valid_email_temp)
   reg_page.enter_pass(valid_password)
   reg_page.enter_pass2(incorrect_password)
   reg_page.btn_click()
   not_same = reg_page.allert_not_same_passw(browser)
   assert "Пароли не совпадают" in not_same
# 6 Тест проверки ввода короткого пароля с валидными символами при регистрации
def test_reg_with_little_password(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(boundary_little_name)
   reg_page.enter_surname(valid_surname)
   reg_page.enter_email(valid_email_temp)
   reg_page.enter_pass(little_password)
   reg_page.enter_pass2(little_password)
   reg_page.btn_click()
   little_reg_pass = reg_page.allert_little_passw(browser)
   assert "Длина пароля должна быть не менее 8 символов" in little_reg_pass
# 7 Тест регистрации на зарегистрированную учётную запись( по почте)
def test_reg_same_valid_data(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(valid_name)
   reg_page.enter_surname(valid_surname)
   reg_page.enter_email(valid_email)
   reg_page.enter_pass(valid_password)
   reg_page.enter_pass2(valid_password)
   reg_page.btn_click()
   same_user_reg = reg_page.allert_same_user(browser)
   assert "Учётная запись уже существует" in same_user_reg
# 8 Тест регистрации с указанием почты без @
def test_reg_same_valid_data(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(valid_name)
   reg_page.enter_surname(valid_surname)
   reg_page.enter_email(email_without_dog)
   reg_page.enter_pass(valid_password)
   reg_wrong_email = reg_page.allert_wrong_reg_email(browser)
   assert "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru" in reg_wrong_email
# 9  Тест регистрации латинскими символами
def test_reg_latin_simbol_name(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(latin_name)
   reg_page.enter_surname("")
   allert_litle = reg_page.allert_name(browser)
   assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in allert_litle
# 10  Тест регистрации валидными данными длинной равной 30 символов
def test_reg_valid_name_30_simbols(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(valid_name_30_simbols)
   reg_page.enter_surname(valid_surname)
   reg_page.enter_email(valid_email_temp)
   reg_page.enter_pass(valid_password)
   reg_page.enter_pass2(valid_password)
   reg_page.btn_click()
   code = reg_page.reg_code(browser)
   assert "Подтверждение email" in code
# 11  Тест регистрации валидными данными имя длинной > 30 символов, фамилия 2-30 символов
def test_reg_valid_name_31_simbols(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(valid_name_31_simbols)
   reg_page.enter_surname(valid_surname)
   reg_page.enter_email(valid_email_temp)
   reg_page.enter_pass(valid_password)
   reg_page.enter_pass2(valid_password)
   reg_page.btn_click()
   allert_litle = reg_page.allert_name(browser)
   assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in allert_litle
# 12 Тест проверки ввода пароля с невалидными символами при регистрации
def test_reg_password_without_lower_case(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(valid_name)
   reg_page.enter_surname(valid_surname)
   reg_page.enter_email(valid_email_temp)
   reg_page.enter_pass(password_without_lower_case)
   reg_page.enter_pass2(password_without_lower_case)
   reg_page.btn_click()
   little_reg_pass = reg_page.allert_little_passw(browser)
   assert "Пароль должен содержать хотя бы одну прописную букву" in little_reg_pass
# 13 Тест проверки ввода длинного пароля с валидными символами при регистрации
def test_reg_with_too_big_passw(browser):
   auth_page = AuthPage(browser)
   auth_page.link_reg()
   reg_page = RegPage(browser)
   reg_page.enter_name(valid_name)
   reg_page.enter_surname(valid_surname)
   reg_page.enter_email(valid_email_temp)
   reg_page.enter_pass(too_big_passw)
   reg_page.enter_pass2(too_big_passw)
   reg_page.btn_click()
   reg_pass_bad = reg_page.allert_passw_more_20_simbols(browser)
   assert "Длина пароля должна быть не более 20 символов" in reg_pass_bad
# 14  Тест входа в учетную запись по зарегистрированной почте c неверным паролем
def test_auth_valid_login_with_incorrect_password(browser):
   auth_page = AuthPage(browser)
   auth_page.enter_email(valid_email)
   auth_page.enter_pass(incorrect_password)
   auth_page.btn_click()
   allert_message = auth_page.wrong_passw(browser)
   assert  "Неверный логин или пароль" in allert_message
# 15  Тест входа в учетную запись по незарегистрированной почте
def test_auth_incorrect_login(browser):
   auth_page = AuthPage(browser)
   auth_page.enter_email(valid_email_temp)
   auth_page.enter_pass(incorrect_password)
   auth_page.btn_click()
   allert_message = auth_page.wrong_passw(browser)
   assert  "Неверный логин или пароль" in allert_message
