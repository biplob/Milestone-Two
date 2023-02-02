import requests
from pprint import pprint
from wpfuncation import image_url, list_html_list, headers, dict_list, wph2, openai_text
api_url = 'https://www.themealdb.com/api/json/v1/1/search.php?f=a'

res = requests.get(api_url)
meals = res.json().get('meals')
single_meals = meals[0]
meal_name = single_meals.get('strMeal')
meal_area = single_meals.get('strArea')
image = single_meals.get('strMealThumb')
youtube = single_meals.get('strYoutube')
instructions = single_meals.get('strInstructions')

i = 1

ingredient = {}

while i < 21:
    key_Ingredient = f'strIngredient{i}'
    key_measurement = f'strMeasure{i}'
    if (single_meals.get(key_Ingredient) != None) and (single_meals.get(key_Ingredient) != ''):
        ingredient[(single_meals.get(key_Ingredient))] = single_meals.get(key_measurement)
    i += 1

instructions_list = instructions.split('\r\n')

title = f'{meal_name} Recepie'
intro = openai_text(f'write about {meal_area} {meal_name}')
image = image_url(image,title)
heading_first = wph2('Ingredients')
ingredient_html = dict_list(ingredient)
heading_second = wph2('Descriptions')
description = list_html_list(instructions_list)

content = f'{intro}{image}{heading_first}{ingredient_html}{heading_second}{description}'

data = {

    'title': title,
    'content': content
}

headers = headers('username', 'wp_password')
endpoint_url = 'https://biplobsite.local/wp-json/wp/v2/posts'
res = requests.post(endpoint_url, data=data, headers=headers, verify=False)
print(res)
