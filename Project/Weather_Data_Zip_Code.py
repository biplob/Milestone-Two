import  requests

api_key = '5ed36d5ce5a9cc7de075321a5d3890df'
city_name = 'Dhaka'
cnt = '23/01/2023'
api_url = f'api.openweathermap.org/data/2.5/forecast/daily?q={city_name}&cnt={cnt}&appid={api_key}'

res = requests.get(api_url)

print(res.status_code)