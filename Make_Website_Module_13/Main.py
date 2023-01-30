from requests import get
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
    first_specifications = phone.get('specifications')
    print(type(first_specifications))