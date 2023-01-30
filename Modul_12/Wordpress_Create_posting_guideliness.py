from requests import post
import base64

username = 'biplob'
user_pass = 'UApP un5S eWm7 P3Fi l1xc cQHX'
wp_credential = f'{username}: {user_pass}'
wp_token = base64.b64encode(wp_credential.encode())
header = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
post_data  = {
    'title': 'Here is my title',
    'slug':'my-awesome-slug',
    'status': 'publish',
    'content': 'This is awesome content of mine',
    'categories':'3'
}
api_end_point = 'https://biplobsite.local/wp-json/wp/v2/posts'
res = post(api_end_point, data=post_data, headers=header, verify=False)

print(res.status_code)
print(res.json())