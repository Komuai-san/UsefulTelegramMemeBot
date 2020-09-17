from bot import telegram_chatbot
import praw
import re
import requests
import config
from pyxlsb import convert_date
import pafy
import random
import dateutil.parser
import wikipedia
import heart

redditlogic = heart.reddit()
dictlogic = heart.googledict()

reddit = praw.Reddit(client_id=config.client_id, 
                     client_secret=config.client_secret, 
                     username=config.username, 
                     password=config.password, 
                     user_agent=config.user_agent)

bot = telegram_chatbot("config.cfg")

def listToString(s):
    str1 = "\n \n"
    return (str1.join(s))


def make_reply(msg):
    reply = None

    if msg is not None:        
        # ==========================QUOTES==================================
        if msg == "quote" or msg == "quotes":
            url = 'https://api.quotable.io/random'
            quote = requests.get(url).json()

            reply = quote['content'] + " - " + quote['author']

        elif "unsplash" in msg:
            try:
                msg = msg.replace("unsplash ", "")
                url = 'https://source.unsplash.com/random?{0}'.format(msg)
                r = requests.get(url)
                reply = r.url
            except:
                reply = "Oof. Error."

        elif "weder" in msg:
            try:
                msg = msg.replace("weder ", "")
                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1b453b589a0691c857ddc95f0921df69'
                city = msg

                r = requests.get(url.format(city)).json()
                temperature = str(r['main']['temp'])
                description = r['weather'][0]['description'].capitalize()
                if float(temperature) < 30.00:
                    flavor = "Better get those blankets ready. Chilly chilly brrrrrt brrrrrt!"
                
                elif float(temperature) > 30.00:
                    flavor = "Hot hot hot! Better get an umbrella or get em fans on full throttle >:)"

                reply = "The weather for today in {} is: \n\n".format(city) + "Temperature: " + temperature + ", " + description + "\n\n" + flavor

            except:
                reply = "Oof. It looks like an error occurred."

        elif "weekc" in msg:    
            try:
                msg = msg.replace("weekc ", "")
                thewik = wikipedia.summary(msg, sentences=5)
                thelink = wikipedia.page(msg)
                reply = thewik + "\n\nLink/Read More: " + thelink.url
            except:
                reply = "I can't return it because maybe the summary's too long, the query is ambiguous, or it doesn't exist!! I'm sorry, master."

        elif "wiki" in msg:
            msg = msg.replace("wiki ", "")

            try:
                wiki_results = wikipedia.search(msg)
                text = "Here are the results for: {}: ".format(msg)
                wikilist = []
                for results in wiki_results:
                    try:
                        wikilist.append(wikipedia.page(results).url)

                    except: 
                        pass

                reply = text + "\n \n" + listToString(wikilist)
            
            except:
                pass

        elif msg == "corona":
            try:
                url = 'https://covid-193.p.rapidapi.com/statistics'
                querystring = { "country": "Philippines" }

                headers = {
                    'x-rapidapi-host': 'covid-193.p.rapidapi.com',
                    'x-rapidapi-key': 'be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041'
                }

                response = requests.request("GET", url, headers=headers, params=querystring).json()
                data = response['response']
                d = data[0]
                disease = ['All: ' + str(d['cases']['total']), 'Recovered: ' + str(d['cases']['recovered']), 'Deaths: ' + str(d['deaths']['total']), 'New: ' + str(d['cases']['new']), 'Critical: ' + str(d['cases']['critical']), 'Time: ' + (str(dateutil.parser.parse(d['time'])))]
                """deses = {
                        'all': d['cases']['total'],
                        'recovered': d['cases']['recovered'],
                        'deaths': d['deaths']['total'],
                        'new': d['cases']['new'],
                        'critical': d['cases']['critical'],
                        'time': dateutil.parser.parse(d['time'])
                }"""
                
                reply = "Let's hope that the virus ends as soon as possible. Here is the latest report in the Philippines:" + "\n \n" + listToString(disease)


            except:
                reply = heart.exceptiontext

        elif msg == "dogs" or msg == "dog" or msg == "doge":
            quotetext = ["Here goes the Doge Barrage!", "Doge: I am the lucid dream. The monster in your nightmares. The fiend of a thousand faces. Just kidding. Can I have my food now?"]
            DOG_URL = 'http://api.thedogapi.com/v1/images/search'
            DOG_API_KEY = '3b392042-b329-4b00-a6f6-b14d3b585396'
            DOG_HEADERS = { 'x-api-key': DOG_API_KEY  }
            IMG_PARAMS = ['jpg,png', 'gif',]
            params = {"mime_types": random.choice(IMG_PARAMS)}
            thecat = requests.request("GET", DOG_URL, params=params, headers= DOG_HEADERS).json()
            reply = random.choice(quotetext) + "\n" + thecat[0]['url']

        # ==========================P U S S Y SECTION========================
        elif msg == "cats" or msg == "cat":
            catquotetext = ["Cat: All will serve me in time.", "Cat: I'm fabulous!"]
            CAT_URL = 'http://api.thecatapi.com/v1/images/search'
            CAT_API_KEY = 'fccdd277-481e-4ce8-91f6-74494640b167'
            CAT_HEADERS = { 'x-api-key': CAT_API_KEY  }
            IMG_PARAMS = ['jpg,png', 'gif',]
            params = {"mime_types": random.choice(IMG_PARAMS)}
            thecat = requests.request("GET", CAT_URL, params=params, headers= CAT_HEADERS).json()
            reply = random.choice(catquotetext) + "\n" + thecat[0]['url']

        # ==========================D A D J O K E S========================
        elif msg == "dadjoke":
            url = 'https://icanhazdadjoke.com/'
            headers =  { 'Accept': 'application/json' }
            thejoke = requests.request("GET", url, headers=headers).json()
            reply = thejoke['joke']

        #===========================DICTIONARY SECTION======================
        elif "dict" in msg:
            try:
                msg = msg.replace("dict ", "")
                url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + msg
                response = requests.get(url).json()
                mgawords = dictlogic.parsetext(response)
                reply = "I guess this is what yer looking for. " + "\n \n" + listToString(mgawords)
            except:
                reply = heart.exceptiontext

        #====================REDDIT SECTION==========================
        elif msg == "rising":
            try:
                thesub = reddit.random_subreddit()
                submission = thesub.rising()
                for subs in submission:
                    reply = subs.title + "\n \n" + subs.selftext + "\n" + subs.url

            except:
                reply = heart.exceptiontext

        elif msg == "randsubpost":
            try:
                thesub = reddit.random_subreddit()
                submission = thesub.random()
                reply = submission.title + "\n" + submission.selftext + "\n" + submission.url

            except:
                reply = heart.exceptiontext

        elif msg == "randsubpostnsfw":
            try:
                thesub = reddit.random_subreddit(nsfw=True)
                submission = thesub.random()
                reply = submission.title + "\n" + submission.selftext + "\n" + submission.url

            except:
                reply = heart.exceptiontext

        elif "rand" in msg:
            try:
                msg = msg.replace("rand ", "")
                submission = reddit.subreddit(msg).random()
                reply = submission.title + "\n" + submission.selftext + "\n" + submission.url


            except:
                reply = heart.exceptiontext

        elif "new" in msg:
            try:
                msg = msg.replace("new ", "")
                subreddit = reddit.subreddit(msg)
                new = subreddit.new(limit=5)
                redlist = redditlogic.hotornew(new)
                reply = "Here are the newest topics at " + msg + " : " + "\n \n" + listToString(redlist)

            except:
                reply = heart.exceptiontext

        elif "hot" in msg:
            try:
                msg = msg.replace("hot ", "")
                subreddit = reddit.subreddit(msg)
                hot = subreddit.hot(limit=5)
                redlist = redditlogic.hotornew(hot)
                reply = "Here are the hottest topics at " + msg + " : " + "\n \n" + listToString(redlist)

            except:
                reply = heart.exceptiontext

        else:
            reply = heart.exceptiontext

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

    