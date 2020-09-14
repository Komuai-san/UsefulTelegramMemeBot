import requests
import json
from random import choice

CAT_URL = 'http://api.thecatapi.com/v1/images/search'
CAT_API_KEY = 'fccdd277-481e-4ce8-91f6-74494640b167'
CAT_HEADERS = { 'x-api-key': CAT_API_KEY  }
IMG_PARAMS = ['jpg,png', 'gif',]
params = {"mime_types": choice(IMG_PARAMS)}

thecat = requests.request("GET", CAT_URL, params=params, headers= CAT_HEADERS).json()
print(thecat[0]['url'])