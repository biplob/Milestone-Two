import base64
import requests
rest_countries = 'https://restcountries.com/v3.1/all'
res = requests.get(rest_countries)
api_data = res.json()
countries = []
for data in api_data:
    country_name = data.get('name').get('official')
    countries.append(country_name)

wp_endpoints = 'https://biplobsite.local/wp-json/wp/v2/categories'
user = 'biplob'
password = 'jLjV zDje d54D h1Bs wtYj GL9v'
token = base64.b64encode(f'{user}:{password}'.encode())
headers = {'Authorization': f'Basic {token.decode("utf-8")}'}

for country in countries:
    data = {'name': country}
    r = requests.post(wp_endpoints,data=data, headers=headers, verify=False)




