import requests
import json
import datetime
import pafy
import shorten_url 
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

"""dt = "2013-08-25 23:59:59"
thedate = dt.replace(" 23:59:59", "").split("-")
print(thedate)
thedate1 = thedate[0] + thedate[1] + thedate[2]
"""
'''thelist = ["""Mark Anthony Cruz
Disappointment"""]
print(thelist)'''

"""query = 'Kawabata'

url = 'https://reststop.randomhouse.com/resources/works/?start=20&max=2&expandLevel=1&search={}'.format(query)
books = requests.get(url, headers= {"Accept": "application/json"}).json()
index = 0"""
"""while index <=44:
    try:
        
    except:
    index+=1"""
    
#print(books)


#print("Title: " + books['work'][index]['titleshort'] + "\nISBN: " + books['work'][index]['titles']['isbn'][index]['$'])


"""url = 'https://reststop.randomhouse.com/resources/authors?firstName=Sigmund&lastName=Freud'
books = requests.get(url, headers= {"Accept": "application/json"}).json()
#print(books['author']['authordisplay'])

index = 0

while index <= 19:
    try:
        print(books['author'][index]['spotlight'])
        break
    except:
        index += 1"""

msg = 'https://www.youtube.com/watch?v=QqV-_7Ms92o'
video = pafy.new(msg)
audio = video.getbestaudio(preftype="m4a")
url = shorten_url.short(audio.url_https)
print(url)


