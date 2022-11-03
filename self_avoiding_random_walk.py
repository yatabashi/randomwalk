from turtle import *
import random
import draw

step = 10

# 準備
t = Turtle()

t.speed(0)

log = {}

# 始点描画
draw.origin(t, 6)

# 酔歩
while True:
    # 現在地取得
    x, y = t.pos()
    x, y = round(x), round(y) # 上下左右のいずれかに進むはずだが、なぜか誤差が生まれるので丸めて無視

    # 現在地をlogに追加
    if x in log.keys():
        log[x].add(y)
    else:
        log[x] = {y}

    # 移動可能な方向を取得
    directions = [0, 90, 180, 270]

    if y+step in log[x]:
        directions.remove(90)
    
    if y-step in log[x]:
        directions.remove(270)

    if x+step in log.keys():
        if y in log[x+step]:
            directions.remove(0)

    if x-10 in log.keys():
        if y in log[x-10]:
            directions.remove(180)

    if len(directions) == 0:
        break

    # 移動方向を取得
    randdirection = random.choice(directions)
    t.setheading(randdirection)

    # 現在地と移動方向を出力
    print((x, y), randdirection)

    # 移動
    t.forward(step)

print(log)

done()