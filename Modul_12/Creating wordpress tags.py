import requests
import base64
from pprint import pprint
user_name = 'biplob'
password = 'jLjV zDje d54D h1Bs wtYj GL9v'
token = base64.b64encode(f'{user_name}:{password}'.encode())
header = {'Authorization': f'Basic {token.decode("utf-8")}'}

# def wp_tags(text):
#     code = f'<!-- wp:post-terms {"term":"{text}"} /-->'
#     return code

# tag = 'Good Point of the tag'

# tags = wp_tags(tag)
content_data = {
    'name': 'Monsur Biplob',
    'description': 'This is good description',
    'slug': 'my-awesome-slug',
    'meta': 'view filed'
}
wp_endpoints = 'https://biplobsite.local/wp-json/wp/v2/tags'
res = requests.post(wp_endpoints, data=content_data, headers=header, verify=False)

