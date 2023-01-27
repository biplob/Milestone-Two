import requests
from bs4 import BeautifulSoup

url = 'https://www.discovermagazine.com/sitemap/article/health/1.xml'

response = requests.get(url)
# print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
link_find = soup.findAll('loc')
for locs in link_find:
    # print(locs.text)
    with open('Discover_sitemap_health.text', 'a+') as discover:
        discover.writelines(locs.text+'\n')