import requests
import json

topics = "Burat"
response = requests.get("https://source.unsplash.com/random?{0}".format(topics))
print(response.url)