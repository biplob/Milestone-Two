import openai

openai.api_key = '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'
prompt = input('Enter your command: ')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# print(response)

text = response.get('choices')[0].get('text')
print(text)