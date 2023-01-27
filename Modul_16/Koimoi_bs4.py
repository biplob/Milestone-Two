import requests
from bs4 import BeautifulSoup

url = 'https://www.koimoi.com/'

res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
links = soup.findAll('a')
for link in links:
    print('https://www.koimoi.com/'+link.get('href'))
    # with open('koimoi.text', 'a+') as file:
    #     file.writelines(link.text)