import requests
import json

url = 'https://icanhazdadjoke.com/'
headers =  { 'Accept': 'application/json' }
thejoke = requests.request("GET", url, headers=headers).json()
print(thejoke['joke'])