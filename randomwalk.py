from turtle import *
import random

# 変数定義
flag = True

# Turtleの設定
speed(0)

# 画面クリック時の挙動の設定
def clicked(x,y):
    global flag
    flag = False
onscreenclick(clicked)

# 酔歩
while flag:
    x, y = pos()

    directions = [0, 90, 180, 270]

    randdirection = random.choice(directions)
    left(randdirection)

    print((x, y), randdirection)

    forward(10)

    if abs(pos()) < 1:
        break

# 終了
done()
