from requests import get
from pprint import pprint

base_url = f'https://www.koimoi.com/wp-json/wp/v2'
api_url =  f'{base_url}/posts'

res = get(api_url)
api_data = res.json()
# print(res.json())

for komoi in api_data:
    try:
      title = komoi.get('title')
      link = komoi.get('link')
      slug = komoi.get('slug')
      print(title, slug, link, sep=', ')

    except:
        print("Page not found")


