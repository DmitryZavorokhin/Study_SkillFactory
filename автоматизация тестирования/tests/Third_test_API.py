import  requests
import json
def api_test_key(email: str, password: str):
    headers = {'email': email, 'password': password }
    url = 'https://petfriends.skillfactory.ru/api/key'
    res = requests.get(url,headers= headers)
    status = res.status_code
    try:
        result = res.json()
        # result = res['key']
    except json.decoder.JSONDecodeError: # не работает( в случае несработки в блоке трай - выдаст ошибку)
        result = res.text()
    return result, status
print(api_test_key('dmz8@mail.ru', '123'))






def get_list_of_pets(auth_key: json, filter: str = "") -> json:
    """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
    со списком наденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
    либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
    собственных питомцев"""
    auth_key = {'key': '8233278b9ffccbdcd87368c39d537c90505e5ca4f5c4aec65626c5c3'}
    headers = {'auth_key': auth_key['key']}
    filter = {'filter': 'my_pets'}

    res = requests.get('https://petfriends.skillfactory.ru/api/pets', headers=headers, params=filter)
    status = res.status_code
    result = ""
    try:
        r = res.json()
        result = str(r.values())
        # result = ': ['.join(r)

        print(result.find('3dcрb19acf2e9'))

    except json.decoder.JSONDecodeError:
        result = res.text
    return r
print(get_list_of_pets('dmz8@mail.ru', '123'))