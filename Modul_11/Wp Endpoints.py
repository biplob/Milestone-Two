from httpx import get
from pprint import  pprint

base_url = f'http://www.jpi.edu.bd/wp-json/wp/v2'

page_api = f'{base_url}/pages?page=5'

res = get(page_api)
api_data = res.json()
# print(api_data)

for page in api_data:
    try:
      title = page.get('title')
      link = page.get('link')
      print(title, link, sep=', ')
    except:
        print('Page Not Found')