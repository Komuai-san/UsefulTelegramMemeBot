import requests
import json
import random
import datetime
#===============================HELPTEXT===============================

mainhelp = """Hi there! This might be an introduction, or there might be an error. To know about the commands for specific tasks, kindly type one of these (without the quotation marks.)

1.) 'help' for serious functions (wiki, dictionary with audio, quotes, local coronavirus information, sneaker shoe informer). Like, things that Google can already do 🙄

2.) 'red' for Reddit functions. (e.g. random subreddits, hot/new topics)

3.) 'fun' for the fun stuff. (cats, dogs, dad jokes)

4.) 'botan' to access my Botanical Gardens of Randomness.

5.) 'main' to summon this text guide again.

6.) 'proj' to see the source code of this bot.

I will add 9gag scraper in the future if Reddit is not enough. Lol.

If you have any concern, kindly let me know here @Komuai .

"""

projectlink = 'https://github.com/Komuai-san/UsefulTelegramMemeBot'

usefulhelp = """ Here are the useful commands.

1.) 'wiki' + Anything you want to search = Returns a list of wiki links related to your query. (takes some time but does the job.)

2.) 'weekc' + Anything you want to search = Returns a long-ass(depends) summary on the subject. This is experimental and would not return anything if summary is really long. I will tell you if that's the case.

3.) 'mshoes' = Randomly shows you a pair of shoes for men with its title, price in dollars, release date, and if possible, an image of it. I've seen an awesome pair here! It looks rad!! (Nike Air Force 1 with a Chinese name)

4.) 'wshoes' = Same thing, but it shows a pair of shoes for women.

5.) 'dict' + the word = Shows you the definition of the word with example, synonym, and audio file.

6.) 'corona' = To know about the corona cases in the Philippines.

7.) 'weder' + city/country = To know the current weather.

8.) 'unsplash' + anything = Returns an image closest to the word you searched. This is pretty much hit or miss, but the image is really high-quality. I suggest searching using broader terms.

9.) 'quote' = Shows a random quote from famous figures.
"""

fun = """ Commands to summon the funny:

1.) 'cats' or 'cat' = Returns a random image of a cat in jpg or gif. I really love cats you know.

2.) 'dogs' or 'dog' or 'doge' = Returns a random image of a dog in jpg or gif. I believe it'll cheer anyone up.

3.) 'dadjoke' = self-explanatory.
"""

exceptiontext = '''Hi!! Here's the commands you can use to see some Reddit content.

Here are the list of commands you can tell me (case sensitive):

1.) new (plus) subreddit of your choice = A list of latest topics from your desired subreddit.

2.) hot (plus) subreddit of your choice = A list of hottest topics from your desired subreddit.

3.) rand (plus) subreddit of your choice = A single, random post from your desired subreddit.

4.) randsubpost = a completely random post from a completely random subreddit.

5.) rising = a completely random "rising" post from a completely random subreddit.

6.) randsubpostnsfw 

'''

botan = """  """



#===============================FUNCTIONS==============================
class reddit:
    def __init__(self):
        pass

    def hotornew(self, redit):
        redlist = []
        
        for index, submission in enumerate(redit, start=1):
            redlist.append(str(index) + "). " + submission.title)

            if(submission.selftext == ""):
                pass
            else:
                redlist.append("- " + submission.selftext)
                
            redlist.append(submission.url)
        
        return redlist



class googledict:
    def __init__(self):
        pass
    
    def parsetext(self, response):
        index = 0
        mgawords = []
        mgawords.append(response[0]['word'])
        mgawords.append(response[0]['phonetics'][0]['text'])
        while index <= 10:
            try:
                str1 = ", "
                mgawords.append(response[0]['meanings'][index]['partOfSpeech'])
                mgawords.append(response[0]['meanings'][index]['definitions'][0]['definition'])
                try: 
                    mgawords.append("-" + response[0]['meanings'][index]['definitions'][1]['definition'])
                except:
                    pass
                
                try:
                    mgawords.append("-" + response[0]['meanings'][index]['definitions'][2]['definition'])
                except:
                    pass

                try:
                    mgawords.append("synonyms: \n\n" +  str1.join(response[0]['meanings'][0]['definitions'][index]['synonyms']))
                except:
                    mgawords.append("synonyms: Nope. source didn't return anything.")
                try:
                    mgawords.append("\nExample: \n\n" + "-" + (str.capitalize(response[0]['meanings'][index]['definitions'][0]['example'])))
                except:
                    mgawords.append("Example: N/A")

                index += 1

            except:
                break

        mgawords.append(response[0]['phonetics'][0]['audio'])

        return mgawords

class sneakerfever:
    def __init__(self):
        pass
    
    def getShoes(self, gender):
        if gender == "mshoes":
            gender = 'men'

        elif gender == "wshoes":
            gender = 'women'

        url = 'https://api.thesneakerdatabase.com/v1/sneakers'
        params = { 'limit': '100', 'gender': gender }
        shoes = requests.request("GET", url, params=params).json()
        shoeslist = []
        numba = random.randint(1, 101)
        price = str(shoes['results'][numba]['retailPrice'])
        imgurl = shoes['results'][numba]['media']['imageUrl']
        shoename = shoes['results'][numba]['title']
        release = shoes['results'][numba]['releaseDate'].replace(" 23:59:59", "").split("-")
        converted = datetime.date(int(release[0]), int(release[1]), int(release[2]))
        thetime = converted.strftime("%B %d, %Y, %A")


        shoeslist.append("Name: " + shoes['results'][numba]['title'])
        shoeslist.append("Brand Name: " + shoes['results'][numba]['brand'])
        shoeslist.append("Colours: " + shoes['results'][numba]['colorway'])
        shoeslist.append("Date Released: " + thetime)

        if price == "None":
            price = ""
            shoeslist.append("Price: Nope. No price indicated in the database.")

        else:
            shoeslist.append("Price: $" + price)
        
        if imgurl is None:
            try:
                imgurl = ""
                query = shoename
                r = requests.get("https://api.qwant.com/api/search/images", params={'count': 50, 'q': query, 't': 'images', 'safesearch': 1, 'locale': 'en_US', 'uiv': 4 }, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' })
                response = r.json().get('data').get('result').get('items')
                urls = [r.get('media') for r in response]
                shoeslist.append("Image: " + urls[1])

            except:
                shoeslist.append("There's no image in the database, and the alternative image source I am using might be dead. Sorry.")
            

        elif shoes['results'][numba]['media']['imageUrl'] == "https://stockx-assets.imgix.net/media/New-Product-Placeholder-Default.jpg?fit=fill":
            try:
                imgurl == ""
                query = shoename
                r = requests.get("https://api.qwant.com/api/search/images", params={'count': 50, 'q': query, 't': 'images', 'safesearch': 1, 'locale': 'en_US', 'uiv': 4 }, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' })
                response = r.json().get('data').get('result').get('items')
                urls = [r.get('media') for r in response]
                shoeslist.append("Image: " + random.choice(urls))
            except:
                shoeslist.append("There's no image in the database, and the alternative image source I am using might be dead. Sorry.")

        else:
            if imgurl == "":
                pass

            else:
                shoeslist.append("Image: " + imgurl)

        return shoeslist


# ==========================WORK IN PROGRESS==================
        #elif "ytdl" in msg:
        #    msg = msg.replace("ytdl ", "")
        #    video = pafy.new(msg)
        #    audio = video.getbestaudio(preftype="m4a")