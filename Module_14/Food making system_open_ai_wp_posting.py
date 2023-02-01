import openai
import requests
import base64

openai.api_key = '{open ai api code}'


def wph2(text):
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code

def wpp(text):
    code = f'<!-- wp:paragraph --><p>{text}d</p><!-- /wp:paragraph -->'
    return code
def openai_answer(prompt):
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt= prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
)
            output = response.get('choices')[0].get('text')
            return output
# print(openai_answer("write three sentence for food makeing system"))

keyword = input('Enter your keyword: ')
prompt = f'Write four questions about {keyword}'
questions = openai_answer(prompt)
questions_list = questions.strip().strip('\n')
end_list = 'write a paragraph about it'

qna = {}
for q in questions_list:
    command = f'{q} + {end_list}'
    answer = openai_answer(command).strip().strip('\n')
    qna[q] = answer


user = 'biplob'
password = '{wored press password}'
credential = f'{user}: {password}'
token = base64.b64encode(credential.encode())
header = {'Authorization': f'Basic {token.decode("utf-8")}'}

content = ''

for key, value in qna.items():
    qn = wph2(key)
    ans = wpp(value)
    temp = qn + ans
    content += temp

title = f'Common questions about {keyword}'
data = {

    'title' : title,
    'content': content,
    'slug': keyword.replace(' ', '-'),
}


api_url = 'https://biplobsite.local/wp-json/wp/v2/posts'
res = requests.post(api_url, data=data, headers=header, verify=False)