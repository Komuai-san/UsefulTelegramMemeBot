import requests
import json
import random
"""from newsapi import NewsApiClient
import dateutil.parser

newsapi = NewsApiClient(api_key='4f1571a2b1af4f2089d6ab2d33d67109')
topheadlines = newsapi.get_top_headlines(sources="bbc-news")

articles = topheadlines['articles']

news = []

for i in range(len(articles)):
    myarticles = articles [i]

    news.append(myarticles['title'] + "\n\n\nArticle by: " + myarticles['author'] + "\n\n\nDate Posted: " + str(dateutil.parser.parse(myarticles['publishedAt'])) + "\n\n\n" + myarticles['description'] + "\n\n\n" + myarticles['url'] + "\n\n\n" +  myarticles['urlToImage'])


rand = random.randint(0, 10)

while True:
    try:
        print (news[rand])
        break
    except:
        continue"""
    

url = 'http://makeup-api.herokuapp.com/api/v1/products.json?product_type=lipstick'

mek = requests.get(url).json()

tags = []

while True:
    try:
        rando = random.randint(0, 500)
        print(mek[rando]['brand'])
        print(mek[rando]['name'])
        print(mek[rando]['price'])
        print(mek[rando]['product_link'])
        print(mek[rando]['image_link'])
        print(mek[rando]['description'])
        print(mek[rando]['rating'])
        break
    except:
        continue

color = []
index = 0
try:
    
    while index <=10:
        try:
            color.append(mek[rando]['product_colors'][index]['colour_name'])
            index+=1
        except:
            break
except:
    print("Huh")

    
print(str(color)[1:-1])


i2 = 0

print(mek[rando]['tag_list'])