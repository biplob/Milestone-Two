import openai
import base64
import requests

openai.api_key = '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'


def wph2(text):
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code

def wpp(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code

def oai_answer(prompt):
       response = openai.Completion.create(
       model="text-davinci-003",
       prompt= prompt,
       max_tokens=256,
       top_p=1,
       frequency_penalty=0,
       presence_penalty=0
    )

       output = response.get('choices')[0].get('text')
       return output

keyword = input("Enter your keyword: ")
prompt = f'Write three questions about {keyword}'
content = wpp(oai_answer(f'write short into about {keyword}').strip().strip('\n'))
questions = oai_answer(prompt)
questions_list = questions.strip().split('\n')
end_line = 'write a paragraph about it'

qna = {}
for q in questions_list:
    command = f'{q} {end_line}'
    answer = oai_answer(command).strip().strip('\n')
    qna[q] = answer



user = 'biplob'
password = 'TwjA y4Gf eZIw 2Hbb xHma 15ba'
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
    data = res.json()
    id = data.get('id')
    src = data.get('guid').get('rendered')
    image_code = wpimage(id,src, keyword)
    return  image_code


content += media_upload('food.png')

for key, value in qna.items():
    qn = wph2(key)
    ans = wpp(value)
    temp = qn + ans
    content += temp

# wp posting part

title = f'common questions about {keyword}'

data = {

    'title' : title.title(),
    'content' : content,
    'slug' : keyword.replace(' ', '-'),
    'featured_media' :'150'
}

api_url = 'https://biplobsite.local/wp-json/wp/v2/posts'
res = requests.post(api_url, data=data, headers=header, verify=False)


