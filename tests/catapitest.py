import requests
import json
from random import choice
import wikipedia

CAT_URL = 'http://api.thecatapi.com/v1/images/search'
CAT_API_KEY = 'fccdd277-481e-4ce8-91f6-74494640b167'
CAT_HEADERS = { 'x-api-key': CAT_API_KEY  }
IMG_PARAMS = ['jpg,png', 'gif',]
params = {"mime_types": choice(IMG_PARAMS)}

thecat = requests.request("GET", CAT_URL, params=params, headers= CAT_HEADERS).json()
#print(thecat[0]['url'])

#page = wikipedia.page("Billy Herrington")
#print(page.content)

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1b453b589a0691c857ddc95f0921df69'
city = 'Manila'
r = requests.get(url.format(city)).json()
temperature = r['main']['temp']
description = r['weather'][0]['description'].capitalize()
reply = "The weather for today is: \n\n" + "Temperature: " + temperature + ", " + description  
print(reply)
