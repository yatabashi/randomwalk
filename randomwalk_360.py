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

    directions = range(0,360)

    randdirection = random.choice(directions)
    left(randdirection)

    print((x, y), randdirection)

    forward(5)

    if abs(pos()) < 1:
        break

showturtle()

done()