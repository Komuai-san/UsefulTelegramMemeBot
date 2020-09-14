import praw
import re
import requests
import config
from pyxlsb import convert_date

reddit = praw.Reddit(client_id=config.client_id, 
                     client_secret=config.client_secret, 
                     username=config.username, 
                     password=config.password, 
                     user_agent=config.user_agent)


subreddit = reddit.subreddit('python')

hot = subreddit.hot(limit=5)

for submission in hot:
    if not submission.stickied:
        print("Title: {}, By: {}, Posted: {}, Ups: {}, Downs: {}".format(submission.title, submission.author_fullname, submission.created_utc, submission.ups, submission.downs))
        print(submission.selftext)
        print(submission.url)


rand = subreddit.random

for rando in rand:
    print(rando.title)


        
"""comments = submission.comments

for comment in comments.list():
    print(20*'-')
    print(comment.body)
    if len(comment.replies) > 0:
        for reply in comment.replies:
            print('REPLY: ', reply.body)"""
