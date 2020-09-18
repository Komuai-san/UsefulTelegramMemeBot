import requests
import json

import base64
topics = "Burat"
response = requests.get("https://source.unsplash.com/random?{0}".format(topics))

#r = requests.get('http://memebuild.com/api/1.0/getRecentMemes').json()
#print(r)


imagedata = base64.b64decode(response.content)
filename = 'shit.jpg'

with open(filename, 'wb') as f:
    f.write(imagedata)




