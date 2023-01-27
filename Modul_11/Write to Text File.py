import httpx

url_list = [

     'https://www.reviewtrackers.com/blog/restaurant-review-sites/',
    'https://www.restaurant-website-builder.com/restaurant-review-sites',
    'https://foodaholix.com/',
    'https://foodstory.com.bd/',
    'https://www.brightlocal.com/resources/top-review-sites',
    'https://blog.feedspot.com/restaurant_review_blogs/',
    'http://www.jpi.edu.bd/wp-json/wp/v2'
]

for url in url_list:
    res = httpx.get(url)
    text = f'{url}-----------{res.status_code}'
    # file = open('another list.text', 'a+')
    # file.writelines(text+'\n')
    # file.close()

    file = open('another list.text', 'r+')
    urllist = file.readline()
    file.close()

    print(urllist)