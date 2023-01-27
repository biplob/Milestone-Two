from bs4 import BeautifulSoup
import requests

url = 'https://www.discovermagazine.com/sitemap.xml'
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
locs = soup.findAll('loc')

for loc in locs:
    #
    with open('loc.txt', 'a+') as file:
        file.writelines(loc.text+'\n')