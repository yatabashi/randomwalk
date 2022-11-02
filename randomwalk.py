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
    x, y = round(x), round(y)

    directions = range(-45,46)

    randdirection = random.choice(directions)
    left(randdirection)

    print((x, y), randdirection)

    forward(5)

    if abs(pos()) < 1:
        break

showturtle()

done()