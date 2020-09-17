import requests
import json


#===============================HELPTEXT===============================

mainhelp = """Hi there! To know about the commands for specific tasks, kindly type one of these (without the quotation marks.)

1.) help for serious functions (wiki, dictionary with audio, quotes, local coronavirus information)
2.) red for Reddit functions. (e.g. random subreddits, hot/new topics)
3.) fun for the fun stuff. (cats, dogs, dad jokes)
4.) botan to access my Botanical Gardens of Seething Hatred.


"""

wikihelp = """'wiki' + anything you want to search = Returns a list of wiki links related to your query. (takes some time but does the job.)
weekc + Anything you want to search = Returns a long-ass(depends) summary on the subject. This is experimental and would not return anything if summary is really long. I will tell you if that's the case.
"""

fun = """cats or cat = Returns a random image of a cat in jpg or gif. I really love cats you know.
dogs or dog or doge = Returns a random image of a dog in jpg or gif. I believe it'll cheer anyone up.

"""

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
                    mgawords.append("synonyms: \n" + str1.join(response[0]['meanings'][0]['definitions'][index]['synonyms']))
                except:
                    mgawords.append("synonyms: nope. source didn't return anything.")
                try:
                    mgawords.append("\nExample: \n" + (str.capitalize(response[0]['meanings'][index]['definitions'][0]['example'])))
                except:
                    mgawords.append("Example: N/A")

                index += 1

            except:
                break

            mgawords.append(response[0]['phonetics'][0]['audio'])

        return mgawords



# ==========================WORK IN PROGRESS==================
        #elif "ytdl" in msg:
        #    msg = msg.replace("ytdl ", "")
        #    video = pafy.new(msg)
        #    audio = video.getbestaudio(preftype="m4a")