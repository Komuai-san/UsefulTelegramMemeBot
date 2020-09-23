from newsapi import NewsApiClient
import dateutil.parser
import random
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
        continue
    

