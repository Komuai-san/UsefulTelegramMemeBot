import requests
import json

"""import random
unsortedlist = []
newlist = []
index = 1

while index <= 40:
    unsortedlist.append(random.randint(1, 10000))
    index += 1

print(unsortedlist)

while unsortedlist:
    smallest = min(unsortedlist)
    newlist.append(smallest)
    unsortedlist.remove(smallest)

print(newlist)"""

url = 'https://api.wc3.blizzardquotes.com/v1/quotes/random'

r = requests.get(url).json()

print(r['value'])

