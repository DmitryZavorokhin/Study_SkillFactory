from bs4 import BeautifulSoup
import requests

base = 'https://ru.stackoverflow.com/'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', id = 'question-mini-list')
# a = div.find_all('a', class_=' “question-hyperlink')
# a = div.find_all('a', class_=' “s-link')
h3 = soup.find_all('h3', class_='s-post-summary--content-title')
for elem in h3:
    a = elem.find('a')
    stroka = a.getText('href'), base + a.get('href')
    print(stroka)
# parent = h3.find_parent()
# print(parent)
