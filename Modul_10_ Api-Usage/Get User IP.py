import requests
user_api = 'https://api.ipify.org?format=json'
res = requests.get(user_api)
# print(data.status_code)
# print(data.json())

if res.status_code == 200:
    data = res.json()
    ip = data.get('ip')
    print("Your Ip is: ", ip)
    # print(data)
    # print(data.json())