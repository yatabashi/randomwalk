from turtle import *
import random

# 変数定義
log = {0: [0]}
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
    x, y = round(x), round(y) # 上下左右のいずれかに進むはずだが、なぜか誤差が生まれるので丸めて無視

    directions = [0, 90, 270] # Uターンできなくしてみた

    randdirection = random.choice(directions)
    left(randdirection)

    print((x, y), randdirection)

    forward(10)

    if abs(pos()) < 1:
        break

# 終了
done()
