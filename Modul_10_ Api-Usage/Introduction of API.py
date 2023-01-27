import requests
res = requests.get('https://jsonplaceholder.typicode.com/comments')
print(res.status_code)
print(res.json())