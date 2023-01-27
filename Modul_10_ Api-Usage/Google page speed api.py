import requests
api_key = 'AIzaSyDXTuREHBJz_wbIXPjH1fp3onak9p8xFEs'
test_url = 'https://developers.google.com'
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}&key={api_key}'

res = requests.get(api_url)
if res.status_code == 200:
    data = res.json()
    cls_score = data.get('loadingExperience').get('metrics').get('EXPERIMENTAL_INTERACTION_TO_NEXT_PAINT').get('percentile')
    first_day = data.get('loadingExperience').get('metrics').get('FIRST_INPUT_DELAY_MS').get('distributions')[1].get('proportion')
    print(cls_score)
    print(first_day)

else:
    print('Something else')
