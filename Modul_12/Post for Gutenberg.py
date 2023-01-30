import  requests
import base64
from pprint import pprint

user = 'biplob'
password = 'fnkw wHHv 5pqr LXVA 5zth c5kr'
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
header = {'Authorization': f'Basic {token.decode("utf-8")}'}

def wp_paragraph(text):
    code =  f'<!-- wp:paragraph --><p>{text}/p><!-- /wp:paragraph -->'
    return code

def heading_h2(head):
    codes = f'<!-- wp:heading --><h2>{head}</h2><!-- /wp:heading -->'
    return codes


title = 'What is Lorem Ipsum?'
paragraph = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
heading = 'This first heading'

content = wp_paragraph(paragraph)
headings = heading_h2(heading)
content_data = {
    'title': title,
    'content': content,
    'heading': headings,
    'categories': '3'
}

api_data_point = 'https://biplobsite.local/wp-json/wp/v2/posts'
res = requests.post(api_data_point, data=content_data, headers=header, verify=False)
print(res.status_code)
