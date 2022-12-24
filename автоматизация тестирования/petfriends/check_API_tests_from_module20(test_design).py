import json
import requests
from settings import incorrect_filter
from requests_toolbelt.multipart.encoder import MultipartEncoder
auth_key = {'key': '8233278b9ffccbdcd87368c39d537c90505e5ca4f5c4aec65626c5c3'}
# auth_key = {'key': 'шошпровмшлршль'}
base_url = "https://petfriends.skillfactory.ru/"
headers = {'auth_key': auth_key['key']}
filter = "my_pets"
pet_id = '154ea698-5384-4a28-890c-5e70b459eb7e'
pet_id_other = 'c13b20ed-953b-4a02-b3b1-75ad825bcf69'
pet_id_incorrect = 'c13b20ed-953b-4a02-b3b1-75ad825bcf690'
pet_photo = 'D:\YandexDisk\Диме\I5_QAP\Test_git_repository\Study_SkillFactory\автоматизация тестирования\petfriends\dist.jpg'

"""GET запрос"""
# res = requests.get(base_url + 'api/pets', headers=headers, params='my_pets')
# status = res.status_code
# result = res.json()
# print(status)
# print(res.headers)
# print(res.is_redirect)
# print(res.elapsed)
# print(res.history)
# print(result)

"""POST запрос и попытка вытащить разные варианты ответа"""
# data = {'name': "cat",'animal_type': "caty",'age': "5", 'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
# res = requests.post(base_url + 'api/pets', headers=headers, data=data)
# status = res.status_code
# print(status)
# print(res.headers)
# print(res.text)
# print(res.json,'\n')
# print(res.content)

"""PUT запрос """
data = {'name': "dhzhd ",'animal_type': "dfhhd",'age': "28614658"}
res = requests.delete(base_url + 'api/pets/'+ '14bbb058-8338-464c-8ebb-3dcb19acf2e9', headers=headers, data=data)
status = res.status_code

print(status)
print(res.headers)
print(res.elapsed)
# print(res.text)
# print(res.json,'\n')
print(res.content)


"""DELETE запрос """

# res = requests.patch(base_url + 'api/pets/'+ '14bbb058-8338-464c-8ebb-3dcb19acf2e9', headers=headers)
# status = res.status_code
#
# print(status)
# print(res.headers)
# print(res.elapsed)
# print(res.text)
# print(res.json,'\n')
# print(res.content)