from random import randint,random, choice
from time import sleep
from tree import RGBXmasTree

tree = RGBXmasTree(brightness=0.15)
tree.off()

def rc():
    #heightened chance of landing in range 0-25 or 225-250
    return choice(list(range(225, 251)) + list(range(0, 255, 50)) + list(range(0, 26)))

#the comma in 3 makes it a tuple
pairs = [(15, 16), (14, 17), (13, 18), (3,), (4, 2), (5, 1), (6, 0)]
while True:
    c = (rc(), rc(), rc())

    for pair in pairs:
        #turn on both lights in the pair as soon after each other as possilbe
        for n in pair:
            tree[n].color = c
        #sleep for between 0.1 and 0.4 seconds after each pair
        sleep(randint(100, 400)/1000)

    #sleep for 0-1 seconds to give time to see the tree fully lit up
    sleep(random())

    for n in list(range(0, 7)) + list(range(13, 19)):
        tree[n].off()
        #sleep for between 0.1 and 0.175 seconds
        sleep(randint(100, 175)/1000)
    sleep(random())

