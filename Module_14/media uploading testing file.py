import requests
import base64



user = 'biplob'
password = '{wp password}'
credential = f'{user}: {password}'
token = base64.b64encode(credential.encode())
header = {'Authorization': f'Basic {token.decode("utf-8")}'}

def wpimage(id,src, keyword):
    line_one = f'<!-- wp:image {{"align":"center",{id}":143,"sizeSlug":"full","linkDestination":"none"}} -->'
    line_two = f'<figure class="wp-block-image aligncenter size-full"><img src="{src}" alt="{keyword}" class="wp-image-{id}" />'
    line_three = f'<figcaption class="wp-element-caption">{keyword}</figcaption></figure><!-- /wp:image -->'
    code = f'{line_one}{line_two}{line_three}'
    return  code


def media_upload(image):
    media_url = 'https://biplobsite.local/wp-json/wp/v2/media'
    files = {'file':open(image, 'rb')}
    res = requests.post(media_url, files=files, headers=header, verify=False)
    # data = res.json()
    # id = data.get('id')
    # src = data.get('guid').get('rendered')
    # image_code = wpimage(id,src, keyword)
    # return  image_code
    print(res.json())


media_upload('food.png')