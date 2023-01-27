import requests
from bs4 import BeautifulSoup

url = 'https://www.discovermagazine.com/sitemap/article/environment/1.xml'

res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
locs = soup.findAll('loc')
for loc in locs:
    # print(loc.text)
    with open('discovermagazine.text', 'a+') as file:
        file.writelines(loc.text+'\n')