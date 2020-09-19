import requests
import json
import datetime
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

"""url = 'https://api.wc3.blizzardquotes.com/v1/quotes/random'

r = requests.get(url).json()

print(r['value'])"""

dt = "2013-08-25 23:59:59"
thedate = dt.replace(" 23:59:59", "").split("-")
print(thedate)
thedate1 = thedate[0] + thedate[1] + thedate[2]

thelist = ["""Mark Anthony Cruz
Disappointment"""]
print(thelist)