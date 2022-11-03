from turtle import *

import random

log = {0: [0]}
flag = True

hideturtle()
speed(0)

def clicked(x,y):
    global flag
    flag = False
onscreenclick(clicked)

while flag:
    x, y = pos()

    directions = [0, 90, 180, 270]

    randdirection = random.choice(directions)
    left(randdirection)

    print((x, y), randdirection)

    forward(5)

    if abs(pos()) < 1:
        break

showturtle()

done()