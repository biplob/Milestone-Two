import requests
import base64
wp_user = 'biplob'
wp_pass = 'UWpF 27v7 fzht DhZS kCuK vXOg'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
header = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

data = {'title': 'This is awosome title'}
wp_post_url = 'https://biplobsite.local/wp-json/wp/v2/posts'
res = requests.post(wp_post_url, data=data, headers=header, verify=False)
print(res.status_code)
# print(res.json())









