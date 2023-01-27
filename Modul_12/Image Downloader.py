from requests import get
file = open('Image_url.text', 'r+')
url_list = file.readlines()
file.close()

new_url_list = []

for url in url_list:
    new_url = url.rstrip('\n')
    new_url_list.append(new_url)

single_url = new_url_list[0]
res = get(single_url)
with open('google.jpg', 'wb') as file:
    file.write(res.content)