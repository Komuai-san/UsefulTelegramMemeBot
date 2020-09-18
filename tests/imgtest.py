import requests
import json
import random
import base64
topics = "Burat"
response = requests.get("https://source.unsplash.com/random?{0}".format(topics))

#r = requests.get('http://memebuild.com/api/1.0/getRecentMemes').json()
#print(r)

"""url = 'https://api.thesneakerdatabase.com/v1/sneakers'
params = {'limit': '100', 'gender': 'women'}
shoes = requests.request("GET", url, params=params).json()
numba = random.randint(1, 100)"""

#print(r['results'][0]['media']['imageUrl'])

"""def randshoes(numb):
    shoelist = []
    shoelist.append(r['results'][numb]['name'])
    shoelist.append(r['results'][numb]['brand'])
    shoelist.append(r['results'][numb]['colorway'])
    shoelist.append("$"+ (str(r['results'][numb]['retailPrice'])))
    shoelist.append(r['results'][numb]['shoe'])
        
    return shoelist

a = randshoes(numba)
print(a)"""
    
"""shoeslist = []
shoeslist.append("Name: " + shoes['results'][numba]['title'])
shoeslist.append("Brand Name: " + shoes['results'][numba]['brand'])
shoeslist.append("Colours: " + shoes['results'][numba]['colorway'])
shoeslist.append("Date Released:" + shoes['results'][numba]['releaseDate'])
shoeslist.append("Price: $" + str(shoes['results'][numba]['retailPrice']))
if shoes['results'][numba]['media']['imageUrl'] == None:
    shoeslist.append("This one doesn't have an image from the database. Sorry.")
else:
    shoeslist.append("Image: " + shoes['results'][numba]['media']['imageUrl'])



print(shoeslist)"""


query = "Frog"

r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 50,
        'q': query,
        't': 'images',
        'safesearch': 1,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
)

response = r.json().get('data').get('result').get('items')
urls = [r.get('media') for r in response]
print(random.choice(urls))


query = "toulouse pink city"

r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 50,
        'q': query,
        't': 'images',
        'safesearch': 1,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
)

response = r.json().get('data').get('result').get('items')
urls = [r.get('media') for r in response]
print(random.choice(urls))