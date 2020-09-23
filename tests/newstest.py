import requests
import json
import random
import html_text

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
    
msg = str(input("Eneter: "))
url = 'http://makeup-api.herokuapp.com/api/v1/products.json?product_type={}'.format(msg)

mek = requests.get(url).json()

"""tags = []

def listToString(s):
    str1 = "\n \n"
    return (str1.join(s).replace(" & ", " AND "))

while True:
    try:
        rando = random.randint(0, 500)
        a = [mek[rando]['brand'], mek[rando]['name'], str(mek[rando]['price']), mek[rando]['product_link'], mek[rando]['image_link'], mek[rando]['description'], str(mek[rando]['rating'])]
        break
    except:
        continue


print(listToString(a))"""

print(mek[2]['name'])


"""color = []
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

print(mek[rando]['tag_list'])"""

"""print(mek[5]['tag_list'])

while True:
    try:
        rando = random.randint(0, 500)
        mekku.append("Brand: " + mek[rando]['brand'])
        mekku.append("Name: " + mek[rando]['name'])
        mekku.append("Price: " + mek[rando]['price'])
        mekku.append("Link: " + mek[rando]['product_link'])
        mekku.append("Image: " + mek[rando]['image_link'])
        mekku.append("Description: " + mek[rando]['description'])
        mekku.append("Rating: " + mek[rando]['rating'])
        print(mekku)
        break

    except:
        continue"""

