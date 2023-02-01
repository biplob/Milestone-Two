from requests import get, post
import json
import base64

username = 'biplob'
password = 'PV4w 1R83 vxlB FnV2 eXCI ScgR'
wp_credential = f'{username}:{password}'
wp_token = base64.b64encode(wp_credential.encode())
wp_header = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}




data_url = 'https://mobile-phone-server.vercel.app/phones'
res = get(data_url)

if res.status_code == 200:
    data = res.json()
    phones = data.get('RECORDS')

def media_from_url(img_src, phone_name):
    """
    This will return the word press media code from url
    """
    codes = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} -->'\
    f'<figure class="wp-block-image aligncenter size-large">'\
    f'<img src="{img_src}" alt="{phone_name} image"/><figcaption class="wp-element-caption"><strong>{phone_name}</strong></figcaption></figure>'\
    f'<!-- /wp:image -->'
    return codes
def wp_table_dict(dictionary):
    """
    This will generate word press table code from dictinary
    :param dictionary:
    :return: html table string
    """
    codes = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        codes += tr_data
    codes += '</tbody></table></figure><!-- /wp:table -->'
    return codes

def wp_parapgraph(text):
    """
    This will generate word press gutenburg parapgraph code
    """
    codes = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return codes
def wp_heading_two(text):
    return f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'

def concatenate_string(*args):
    final = ''
    for arg in args:
        final += arg
    return final

def slugify(name):
    text = name.strip().replace(' ', '-')
    return text
def create_wp_post(title, content, slug, excerpt, status = 'publish'):
    api_url = 'https://biplobsite.local/wp-json/wp/v2/posts'
    data = {
        'title' : title,
        'content' : content,
        'slug': slug,
        'status': status,
        'excerpt': excerpt
    }
    response = post(api_url, headers=wp_header, json=data, verify=False)
    print(f'{title} is posted')

for phone in phones:
    name = phone.get('name').title()
    released_at = phone.get('released_at').lower().replace("Released ", '')
    chipset = phone.get('chipset')
    body = phone.get('body')
    os = phone.get('os')
    picture = phone.get('picture')
    first_dictionary = {
        'name': name,
        'released_at ': released_at,
        'chipset': chipset,
        'body': body
    }
    first_paragraph = f'{name} has been {released_at}. '\
                      f'It comes with {chipset} chipset. The body of this {body} '\
                      f'{os} is the built in android version.'
    artical_paragraph = wp_parapgraph(first_paragraph)
    first_image = media_from_url(picture, name)
    first_heading = wp_heading_two(f'{name} overview')
    first_table = wp_table_dict(first_dictionary)

    # specifications Sections
    second_heading = wp_heading_two('Specifications')
    specifications_string = phone.get('specifications')
    specifications = json.loads(specifications_string)
    second_table = wp_table_dict(specifications)
    content = concatenate_string(artical_paragraph,first_image, first_heading, first_table, second_heading, second_table)
    slug = slugify(name)
    create_wp_post(name, content, slug, first_paragraph)
