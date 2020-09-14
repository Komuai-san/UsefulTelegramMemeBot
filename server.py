  
from bot import telegram_chatbot
import praw
import re
import requests
import config
from pyxlsb import convert_date
import random

reddit = praw.Reddit(client_id=config.client_id, 
                     client_secret=config.client_secret, 
                     username=config.username, 
                     password=config.password, 
                     user_agent=config.user_agent)

bot = telegram_chatbot("config.cfg")

exceptiontext = '''Hi!! It looks like an error occurred or something.

Here are the list of commands you can tell me (case sensitive):

1.) new (plus) subreddit of your choice = A list of latest topics from your desired subreddit.

2.) hot (plus) subreddit of your choice = A list of hottest topics from your desired subreddit.

3.) rand (plus) subreddit of your choice = A single, random post from your desired subreddit.

4.) randsubpost = a completely random post from a completely random subreddit.

5.) rising = a completely random "rising" post from a completely random subreddit.

6.) randsubpostnsfw = This might return a N S F W content from a random subreddit. Be warned.

7.) quote = get a completely random quote.

8.) dadjoke = witness a dad joke.'''



def listToString(s):
    str1 = "\n \n"
    return (str1.join(s))


def make_reply(msg):
    reply = None

    if msg is not None:        
        # ==========================QUOTES==================================
        if msg == "quote":
            url = 'https://api.quotable.io/random'
            quote = requests.get(url).json()

            reply = quote['content'] + " - " + quote['author']

        elif msg == "dogs" or msg == "dog":
            DOG_URL = 'http://api.thedogapi.com/v1/images/search'
            DOG_API_KEY = '3b392042-b329-4b00-a6f6-b14d3b585396'
            DOG_HEADERS = { 'x-api-key': DOG_API_KEY  }
            IMG_PARAMS = ['jpg,png', 'gif',]
            params = {"mime_types": random.choice(IMG_PARAMS)}
            thecat = requests.request("GET", DOG_URL, params=params, headers= DOG_HEADERS).json()
            reply = "Cute Doge Incoming!!" + "\n" + thecat[0]['url']

        # ==========================P U S S Y SECTION========================
        elif msg == "cats" or msg == "cat":
            CAT_URL = 'http://api.thecatapi.com/v1/images/search'
            CAT_API_KEY = 'fccdd277-481e-4ce8-91f6-74494640b167'
            CAT_HEADERS = { 'x-api-key': CAT_API_KEY  }
            IMG_PARAMS = ['jpg,png', 'gif',]
            params = {"mime_types": random.choice(IMG_PARAMS)}
            thecat = requests.request("GET", CAT_URL, params=params, headers= CAT_HEADERS).json()
            reply = "What? Never seen a cool cat?" + "\n" + thecat[0]['url']

        # ==========================D A D J O K E S========================
        elif msg == "dadjoke":
            url = 'https://icanhazdadjoke.com/'
            headers =  { 'Accept': 'application/json' }
            thejoke = requests.request("GET", url, headers=headers).json()
            reply = thejoke['joke']

        #===========================DICTIONARY SECTION======================
        elif "dict" in msg:
            try:
                index = 0
                msg = msg.replace("dict ", "")
                url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + msg
                response = requests.get(url).json()
                mgawords = []
                mgawords.append(response[0]['word'])
                mgawords.append(response[0]['phonetics'][0]['text'])
                while index <= 10:
                    try:
                        
                        mgawords.append(response[0]['meanings'][index]['partOfSpeech'])
                        mgawords.append(response[0]['meanings'][index]['definitions'][0]['definition'])
                        index += 1

                    except:
                        break

                mgawords.append(response[0]['phonetics'][0]['audio'])

                reply = "I guess this is what yer looking for. " + "\n \n" + listToString(mgawords)

            except:
                reply = exceptiontext

        #====================REDDIT SECTION==========================
        elif msg == "rising":
            try:
                thesub = reddit.random_subreddit()
                submission = thesub.rising()
                for subs in submission:
                    reply = subs.title + "\n \n" + subs.selftext + "\n" + subs.url

            except:
                reply = exceptiontext

        elif msg == "randsubpost":
            try:
                thesub = reddit.random_subreddit()
                submission = thesub.random()
                reply = submission.title + "\n" + submission.selftext + "\n" + submission.url

            except:
                reply = exceptiontext

        elif msg == "randsubpostnsfw":
            try:
                thesub = reddit.random_subreddit(nsfw=True)
                submission = thesub.random()
                reply = submission.title + "\n" + submission.selftext + "\n" + submission.url

            except:
                reply = exceptiontext

        elif "rand" in msg:
            try:
                msg = msg.replace("rand ", "")
                submission = reddit.subreddit(msg).random()
                reply = submission.title + "\n" + submission.selftext + "\n" + submission.url


            except:
                reply = exceptiontext

        elif "new" in msg:
            try:
                msg = msg.replace("new ", "")
                subreddit = reddit.subreddit(msg)
                new = subreddit.new(limit=5)
                redlist = []

                for index, submission in enumerate(new, start=1):
                    redlist.append(str(index) + "). " + submission.title)
                    if(submission.selftext == ""):
                        pass
                    else:
                        redlist.append("- " + submission.selftext)
                    redlist.append(submission.url)

                reply = "Here are the newest topics at " + msg + " : " + "\n \n" + listToString(redlist)

            except:
                reply = exceptiontext

        elif "hot" in msg:
            try:
                msg = msg.replace("hot ", "")
                subreddit = reddit.subreddit(msg)
                hot = subreddit.hot(limit=5)
                redlist = []
                
                for submission in hot:
                    redlist.append(submission.title)
                    redlist.append(submission.url)

                reply = "Here are the hottest topics at " + msg + " : " + "\n \n" + listToString(redlist)

            except:
                reply = exceptiontext

        else:
            reply = exceptiontext

    return reply

update_id = None

while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)