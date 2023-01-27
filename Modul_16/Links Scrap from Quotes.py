from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
links = soup.findAll('a')
# print(link)
for link in links:
    print('https://quotes.toscrape.com/'+link.get('href'))
    # with open('link.txt', 'a+') as file:
    #     file.write(link.get('href'))

