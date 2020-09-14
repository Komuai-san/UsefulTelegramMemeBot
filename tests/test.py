import random
unsortedlist = []
newlist = []
index = 1

while index <= 40:
    unsortedlist.append(random.randint(1, 10000))
    index += 1

print(unsortedlist)

while unsortedlist:
    smallest = min(unsortedlist)
    newlist.append(smallest)
    unsortedlist.remove(smallest)

print(newlist)

