from  requests import  get
from pprint import pprint
api_key = '33145590-fb69f0e3daf0b60fcd78c48f5&q'
query = 'yellow+flowers'
api_url = f'https://pixabay.com/api/?key={api_key}&q={query}'

res = get(api_url)
# pprint(res.json())
api_data = res.json().get('hits')
# print(api_data)

for data in api_data:
    image_url = data.get('webformatURL')
    file = open('Image_url.csv', 'a+')
    urllist = file.writelines(image_url+'\n')
    file.close()
