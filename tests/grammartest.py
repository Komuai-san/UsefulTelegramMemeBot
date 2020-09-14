"""import pafy  

url = 'https://www.youtube.com/watch?v=UmFFTkjs-O0'
video = pafy.new(url)
audio = video.getbestaudio(preftype="m4a")
print(audio.url)"""

"""import requests
import json
import dateutil.parser"""
def listToString(s):
    str1 = "\n \n"
    return (str1.join(s))

"""url = 'https://covid-193.p.rapidapi.com/statistics'
querystring = { "country": "Philippines" }

headers = {
    'x-rapidapi-host': 'covid-193.p.rapidapi.com',
    'x-rapidapi-key': 'be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041'
}

response = requests.request("GET", url, headers=headers, params=querystring).json()
data = response['response']
d = data[0]
disease = ['All: ' + str(d['cases']['total']), 'Recovered: ' + str(d['cases']['recovered']), 'Deaths: ' + str(d['deaths']['total']), 'New: ' + str(d['cases']['new']), 'Critical: ' + str(d['cases']['critical']), 'Time: ' + (str(dateutil.parser.parse(d['time'])))]
print(listToString(disease))"""

import wikipedia

msg = "Billy Herrington"
wiki_results = wikipedia.search(msg)
text = "Results for: {}".format(msg)
wikilist = []
for results in wiki_results:
    try:
        wikilist.append(wikipedia.page(results).url)

    except: 
        pass
                    
print("Here are the results for " + msg + " : " + "\n \n" + listToString(wikilist))