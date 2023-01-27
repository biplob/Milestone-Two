from requests import get

with open('Image_url.text', 'r') as file:
    url_list = file.readlines()

# print(url_list)
i = 0
for url in url_list:
    url_strip = url.strip('\n')
    res = get(url)
    with open(f'Images/{i}.jpg', 'wb') as file:
        file.write(res.content)
        i += 1