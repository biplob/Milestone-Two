import requests
api_find_url = 'https://api.ipify.org?format=json'
res = requests.get(api_find_url)
# print(res.json())

if res.status_code == 200:
    data = res.json()
    ip = data.get('ip')
    # print("Your ip address is: ", ip)

ip_location_url = f'https://ipapi.co/{ip}/json/'
r = requests.get(ip_location_url)

if r.status_code == 200:
    ip_details = r.json()
    city = ip_details.get('city')
    region = ip_details.get('region')
    country_name = ip_details.get('country_name')
    org = ip_details.get('org')


sentence = f'Ip address is {ip} also location in {city} {region}, {country_name}. your organation name is {org}'

print(sentence)