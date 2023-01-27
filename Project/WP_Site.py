from httpx import  get
from pprint import  pprint

base_url = 'https://colorlib.com/wp-json/wp/v2'
page_api = f'{base_url}/pages'

res = get(page_api)
# print(res.status_code)
api_data = res.json()
# print(api_data)

for page in api_data:
    try:
     title = page.get('title')
     slug = page.get('slug')
     link = page.get('link')
     template = page.get('template')
     print(title, slug, link, template, sep=', ')
    except:
        print('Page not found')