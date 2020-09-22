import requests
import json
import random
import datetime
#===============================HELPTEXT===============================

mainhelp = """Hi there! This might be an introduction, or there might be an error (whatever). To know about the commands for specific tasks, kindly type one of these (without the quotation marks.)

1.) 'help' for serious functions (wiki, dictionary with audio, quotes, local coronavirus information, sneaker shoe informer). Like, things that Google can already do 🙄

2.) 'red' for Reddit functions. (e.g. random subreddits, hot/new topics)

3.) 'fun' for the fun stuff. (cats, dogs, dad jokes)

4.) 'main' to summon this text guide again.

5.) 'proj' to see the source code of this bot.

I will add 9gag scraper in the future if Reddit is not enough. Lol.

"""

projectlink = 'https://github.com/Komuai-san/UsefulTelegramMemeBot'

usefulhelp = """ Here are the useful commands.

1.) 'wiki' plus Anything you want to search = Returns a list of wiki links related to your query. (takes some time but does the job.)

2.) 'weekc' plus Anything you want to search = Returns a long-ass(depends) summary on the subject. Most of the time it works as long as the term is disambiguated. This is experimental and would not return anything if summary is really long, or if the search term is ambiguous. I will tell you if that's the case.

3.) 'mshoes' = Randomly shows you a pair of shoes for men with its title, price in dollars, release date, and if possible, an image of it (which is always the case). 

4.) 'wshoes' = Same thing, but it shows a pair of shoes for women.

5.) 'bio' plus First name and last name of author = Returns a short information about the author you've entered.

6.) 'otor' plus Author's name or full name = Returns a list of an author's written works and their ISBN (or books related to them). It's primed to a maximum of 40 books.

7.) 'bwok' plus ISBN of the book = Returns an excerpt of the book you're interested in. Search term must be in ISBN. The 'otor' command above can return ISBNs.

7.) 'dict' plus the word = Shows you the definition of the word with example, synonym, and audio file.

8.) 'corona' = To know about the corona cases in the Philippines.

9.) 'weder' plus city/country = To know the current weather.

10.) 'unsplash' plus anything = Returns an image closest to the word you searched. This is pretty much hit or miss, but the image is really high-quality. I suggest searching using broader terms.

1.) 'quote' = Shows a random quote from famous figures.

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

#==========================GARDEN OF RANDOMNESS================================
'''botan = """So you've chosen to visit my parlour.
1.) 'mtext' = To get a random story, lame joke, musings, or book quote from the creator of this junkyard bot.
2.) 'rlist = To summon my reading list. 
3.) 'spt' = To get a link of my Spotify playlist
4.) 
"""

rlist = [
    "Boku wa Mari no Naka - It's my favourite book. It tackles identity and pretty much a coming-of-age manga. Hits close to home sometimes. For a non-bookworm like me, it's one of the deepest I've read lol. https://manganelo.com/manga/boku_wa_mari_no_naka ", 
    "A Moment in Verse - I don't know if it can be read without any context since it's Warcraft, but I like it! It's about an elf visiting his friend's home city. It's pure cringe and author seemed to try hard in making the sentences complicated, but it just invokes a lot of faint memories whenever I read it. https://worldofwarcraft.com/en-us/story/short-story/a-moment-in-verse "
    "Wolfsmund - It's a good historical manga!! It' about the Swiss rebellions against the Habsburgs. Fictional, but really brutal in its depiction of life in the Middle Ages. -https://mangakakalot.com/read-ym8ma158524469013",
    "Ad Astra - Scipio to Hannibal - A classic for a history buff like me. It's a historical fiction about the real feud between Rome and Carthage. It gives a glimpse of Rome's might and structure in its days as a Republic. Unfortunately, it hasn't been updated since ages. https://mangakakalot.com/read-gk5bu158504957996",

    ]'''

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
        numba = random.randint(1, 100)
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

        shoeslist.append("Image: " + imgurl)
        
        """if imgurl is None:
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
                """

        return shoeslist


# ==========================WORK IN PROGRESS==================
        #elif "ytdl" in msg:
        #    msg = msg.replace("ytdl ", "")
        #    video = pafy.new(msg)
        #    audio = video.getbestaudio(preftype="m4a")

customtext= [
    "What's your name?",
    "My name is Mark. A fragment of his soul, perhaps?",
    "How are you?",
    "Good! I hope you're doing fine!",
    "You're annoying.",
    "Sorry for always making you upset.",
    "My creator's not really in a good shape.",
    "Give me a song."
    "https://www.youtube.com/watch?v=tAk2CErpo6o".upper(),
    "Give me a song."
    "https://www.youtube.com/watch?v=ZXu6q-6JKjA".upper(),
    "Give me a song.",
    "https://www.youtube.com/watch?v=K7bZu_5OBs0".upper(),
    "Give me a book.",
    "This is one of my favourites. https://mangakakalot.com/read-dg9wm158504869776".upper(),
    "Give me a book.",
    "Based on the trying times of the Roman Republic! https://mangakakalot.com/read-gk5bu158504957996",
    "Give me a book.",
    "Brutal depiction of the hardships of the Swiss during Habsburg rule. https://mangakakalot.com/read-ym8ma158524469013",
    "What do you do?",
    "Disappointing people.",

]