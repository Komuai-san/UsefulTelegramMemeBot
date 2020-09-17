import json
import requests

index = 0
#url = 'https://api.quotable.io/random'
#trythis = requests.get(url).json()
#print(trythis['content'])
#print(trythis['author'])

'''dicturl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/gay?key=aed81778-90f8-4208-9158-329908c52481'
response = requests.get(dicturl).json()
print(response['stems'])'''

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/crazy'
response = requests.get(url).json()
"""print(response[0]['word'])
print(response[0]['phonetics'][0]['text'])
print(response[0]['meanings'][0]['partOfSpeech'])
print(response[0]['meanings'][0]['definitions'][0]['definition'])
print(response[0]['phonetics'][0]['audio'])"""

"""

while index <=4:
    try:
        print(response[0]['meanings'][0]['partOfSpeech'])
        print(response[0]['meanings'][0]['definitions'][index]['definition'])
        index+=1
    except:
        break

print(response[0]['phonetics'][0]['audio'])"""
print(response[0])
print(response[0]['word'])
print(response[0]['phonetics'][0]['text'])
print()
while index<=len(response[0]):
    try:
        print(response[0]['meanings'][index]['partOfSpeech'])
        print(response[0]['meanings'][index]['definitions'][0]['definition'])
        try:
            print("\nExample: \n" + (str.capitalize(response[0]['meanings'][index]['definitions'][0]['example'])))
        except:
            pass
        try:
            thestr = ", "
            final = thestr.join(response[0]['meanings'][0]['definitions'][index]['synonyms'])
            print("\nsynonyms:")
            print(final)
        except:
            pass
        print()
        index+=1

    except:
        break