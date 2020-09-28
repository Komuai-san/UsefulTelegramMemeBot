import requests
import json
from udpy import UrbanClient
import basc_py4chan as chan
import random

"""goodweedskey = 'BITG2oRAnefsoqrs4VT21Q'
goodweeds = 'eBUSUEE6rZWGnearzpO6m5lKMOjzqStTutX1MLXIA0'
myid = '45546009'
#url = 'https://www.goodreads.com/review/list?v=2&key={}&id={}&shelf=to-read&sort=random&per_page=1'.format(goodweedskey, myid)

url = 'https://www.goodreads.com/book/title.json?author=Arthur+Conan+Doyle&key=BITG2oRAnefsoqrs4VT21Q&title=Hound+of+the+Baskervilles'

book = requests.get(url).json()
print(book)"""

"""client = UrbanClient()

defs = client.get_random_definition()
for index, d in enumerate(defs):
    print(str(index) + "). " + d.definition + '\n')
    print(d.word)"""


boardlist = ['g', 'pol', 'tv', 'a', 'x', 'jp']
b = chan.Board(random.choice(boardlist))
c = b.get_all_threads(expand=False)
thelist = []


while True:
    thread = random.choice(c)
    for r in thread.replies:
        if r.has_file == True:
            thelist.append(r.text_comment)
            thelist.append(r.file_url)

    if not thelist:
        continue
    
    else:
        break

print(thelist)

            