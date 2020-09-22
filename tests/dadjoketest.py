import requests
import json
import textwrap
import html2text
"""url = 'https://icanhazdadjoke.com/'
headers =  { 'Accept': 'application/json' }
thejoke = requests.request("GET", url, headers=headers).json()
print(thejoke['joke'])"""
query = 'Mishima'

url = 'https://reststop.randomhouse.com/resources/works/?start=0&max=20&expandLevel=1&search={}'.format(query)
books = requests.get(url, headers= {"Accept": "application/json"}).json()
index = 0
while index<=19:
    try:
        print(books['work'][index]['titleshort'])
        try:
            print(books['work'][index]['titles']['isbn'][0]['$'])
        except:
            print("ISBN: None")
    except:
        break
    
    index+=1



"""url = 'https://reststop.randomhouse.com/resources/titles/9780307959614'
books = requests.get(url, headers={'Accept': 'application/json'}).json()
thebok = books['excerpt']
thebok = books['excerpt'].replace("<br>", "\n").replace("&#160;", " ").replace("&rsquo;", "'").replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&mdash;", "—")
print(thebok)
bokbok = thebok.split()
newlist = []

for index, x in enumerate(bokbok):
    if index == 595:
        break
    else:
        newlist.append(x)
        
newlist.append("...")
mark = " "
final = mark.join(newlist)
what = final.replace("<br>", "\n").replace("&#160;", " ").replace("&rsquo;", "'").replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&mdash;", "—")
print(len(final))
print(len(bokbok))"""
    
