import httpx
#
# api_key = '5ed36d5ce5a9cc7de075321a5d3890df'
# city_name = 'Dhaka'
# api_ulr = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
#
# res = httpx.get(api_ulr)
# print(res.json())

# url_list = [
#     'https://www.dogfoodadvisor.com/',
#     'https://dogfoodreviews.com/',
#     'https://www.nytimes.com/wirecutter/reviews/how-to-buy-the-best-dog-food/',
#     'https://www.hepper.com/dog-food-reviews/'
# ]
#
# for url in url_list:
#     res = httpx.get(url)
#     print(url, res.status_code, sep='----')

# food reviws site checking

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
    response_site = httpx.get(url)
    print(url, response_site.status_code, sep='---')