import os
import json
from petfriends.api import PetFriends
from petfriends.settings import valid_email,valid_password,incorrect_email,incorrect_password,too_big_auth_key, incorrect_filter
import pytest
import requests
import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder
@pytest.fixture()
def get_key(request):
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": 'dmz8@mail.ru', "pass": '123'})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print("\nreturn auth_key")
    return response.request.headers.get('Cookie')

"""код ниже - полностью скопирован от преподавателя для дальнейшего изучения"""

pf = PetFriends()



def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(get_key):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """
    filter = 'my_pets'
    auth_key = get_key()
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    print(result)
    assert status == 200
    assert len(result['pets']) > 0

""" тест добавления не запустился, код ответа 500"""
def test_add_new_pet_with_valid_data(name='EsexT', animal_type='elefant',
                                     age='20', pet_photo='images/dist.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/dist.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


'''------------------------------------------------------------------------------------------------------------------'''
'''                    негативные тест-кейсы                  задание 19.7.2'''
""" Тест № 1 """
def test_get_api_key_for_incorrect_login_user(email=incorrect_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при получении ключа незарегистрированного пользователя
    или при ошибке ввода логина"""
    status, result = pf.get_api_key(email, password)
    assert status == 403

""" Тест № 2 """
def test_get_api_key_for_incorrect_password_user(email=valid_email, password=incorrect_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при ошибке ввода пароля"""
    status, result = pf.get_api_key(email, password)
    assert status == 403

""" Тест № 3 """
def test_get_all_pets_with_incorrect_key(filter=''):
    """ Проверяем что при GET-запросе с неправильным ключом возвращается статус 403, т.е.  доступ к запрошенному ресурсу запрещен"""

    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = {'key': '8233278b9ffccbdcd87368c39d537c90505e5ca4f5c4aec65626c5c31'}
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403

""" Тест № 4 """
def test_get_all_pets_with_too_big_auth_key(filter=''):
    """ Проверяем что при запросе с очень длинным ключом возвращается статус некорректного запроса 400"""

    status, result = pf.get_list_of_pets(too_big_auth_key, filter)

    assert status == 400

""" Тест № 5 """
def test_add_new_pet_with_metod_create_pet_simple_without_photo_with_incorrect_auth_key (name = "", animal_type = '', age =''):
    """ Проверяем, что при добавлении нового питомца без фото с некорректным auth_key  приходит статус  403"""
    auth_key = {'key': '8233278b9ffccbdcd87368c39d537c90505e5ca4f5c4aec65626c5c31'}

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403

""" Тест № 5 """
def test_add_photo_to_with_incorrect_data( pet_photo='images/distemper-logo.png'):
    """Проверяем возможность добавления фото с некорректными данными формата фото, ожидаемый ответ сервера  - ошибка 500"""
    #  получаем и сохраняем ключ
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    #  получаем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # проверяем, есть ли питомцы в списке
    if len(my_pets['pets']) > 0:
        # получаем id последнего в списке питомца
        pet_id = my_pets['pets'][0]['id']
        # Добавляем фото к последнему питомцу
        status, result = pf.Add_photo_of_valid_pet(auth_key, pet_id, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 500

""" Тест № 6 """
def test_add_photo_to_with_incorrect_auth_key( pet_photo='images/dist.jpg'):
    """Проверяем возможность добавления фото с некорректным ключом идентификации, ожидаемый ответ сервера  - ошибка 403"""
      #  получаем и сохраняем ключ
    _, auth_key = pf.get_api_key(valid_email, valid_password)
        #  получаем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # проверяем, есть ли питомцы в списке
    if len(my_pets['pets']) > 0:
        # получаем id последнего в списке питомца
        pet_id = my_pets['pets'][0]['id']
        #  присвоение некорректного ключа
        auth_key = {'key': '8233278b9ffccbdcd87368c39d537c90505e5ca4f5c4aec65626c5c31'}
        # Добавляем фото к последнему питомцу
        status, result = pf.Add_photo_of_valid_pet(auth_key, pet_id, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 403

""" Тест № 7 """
def test_delete_pet_with_incorrect_auth_key():
    """Проверяем возможность удаления питомца с некорректным ключом auth_key, ждём ответ от сервера с ошибкой 403"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Котёнок", "котя", "1", "images/dist.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    #  присвоение некорректного ключа
    auth_key = {'key': '8233278b9ffccbdcd87368c39d537c90505e5ca4f5c4aec65626c5c31'}
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 403

""" Тест № 8 """
def test_add_new_pet_with_incorrect_data(name='EsexT', animal_type='elefant',
                                     age='20'):
    """Проверяем, что добавить питомца с некорректными данными нельзя( без фото), ожидаемая ошибка - 400"""

        # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_bad_pet(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400

""" Тест № 9 (ресурс https://petfriends.skillfactory.ru "прилёг", тест не проверен :-) """
def test_update_pet_info_with_incorrect_auth_key(name='Мур', animal_type='Кот', age=1):
    """Проверяем возможность обновления информации о питомце c некорректным auth_key, ожидаемый ответ от сервера - ошибка 403"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        #  присвоение некорректного ключа
        auth_key = {'key': '8233278b9ffccbdcd87368c39d537c90505e5ca4f5c4aec65626c5c31'}
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 403
        assert status == 403

""" Тест № 10"""
def test_get_my_pets_with_incorrect_filter():
    """ Проверяем что при GET-запросе с неправильным фильтром мои питомцев возвращается статус 403, т.е.  доступ к запрошенному ресурсу запрещен"""
    filter = incorrect_filter
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403


""" Тест метода create_pet_simple  """
def test_add_new_pet_with_metod_create_pet_simple_without_photo_with_valid_data(name = "Tim", animal_type = 'cat', age = '5'):
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

""" Тест метода Add photo of pet  """
""" Подумать перед отправкой на проверку ментору( если буду успевать)(этот комментарий удалить перед отправкой):
- нужна ли проверка фото на меняемом питомце
- вариант выбора pet_id и смена фото на любом питомце
- алгоритм сверки фото по коду в json в assert"""
def test_add_photo_to_valid_pet( pet_photo='images/dist.jpg'):
    #  получаем и сохраняем ключ
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    #  получаем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # проверяем, есть ли питомцы в списке
    if len(my_pets['pets']) > 0:
        # получаем id посленего в списке питомца
        pet_id = my_pets['pets'][0]['id']
        # Добавляем фото к последнему питомцу
        status, result = pf.Add_photo_of_valid_pet(auth_key, pet_id, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['pet_photo'] is not None
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


