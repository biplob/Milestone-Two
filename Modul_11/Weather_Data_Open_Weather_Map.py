from requests import get
from pprint import pprint
api_key = '5ed36d5ce5a9cc7de075321a5d3890df'
city_name = 'Los Angeles'
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

res = get(api_url)
api_data = res.json()
country_name = api_data.get('sys').get('country')
sunrise = api_data.get('sys').get('sunrise')
sunset = api_data.get('sys').get('sunset')
weather_data = api_data.get('main')
feels_like = weather_data.get('feels_like')
temp = weather_data.get('temp')
temp_max = weather_data.get('temp_max')
temp_min = weather_data.get('temp_min')
# print(country_name, sunrise, sunset)
print(country_name, sunrise, sunset, feels_like, temp, temp_max, temp_min)