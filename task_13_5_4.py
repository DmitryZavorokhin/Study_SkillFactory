user_data = {'user': "dan", 'password': '123'} # поиск введенного имени ив списке и сверка введенного  пароля с паролем в базе. Возвращает или True или False
un = str(input("имя: "))
pw = str(input("пароль: "))
def check_user(un, pw):
    if un in user_data.values():
        if pw in user_data.values():
            return True
        else:
            return False
    else:
        return False
print(check_user(un,pw))




# if un in user_data.values(): # работающий код поиска в словаре
#     print(un)
# else:
#     print("not")



# def gwc(s): # работающий код функции
#     if 1 <= s <= 4:
#         return "weak"
#     elif 5 <= s <= 10:
#         return "moderate"
#     elif 11 <= s <= 18:
#         return "strong"
# s = int(input("вводи скорость: "))
# print(gwc(s))