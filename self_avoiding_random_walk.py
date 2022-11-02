from turtle import *
import random

step = 10

# 準備
speed(0)

log = {}

# 始点描画
forward(3)
left(90)

begin_fill()
forward(3)
for _ in range(3):
    left(90)
    forward(6)
left(90)
forward(3)
end_fill()

left(90)
forward(3)

# 酔歩
while True:
    # 現在地取得
    x, y = pos()
    x, y = round(x), round(y)

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
    setheading(randdirection)

    # 現在地と移動方向を出力
    print((x, y), randdirection)

    # 移動
    forward(step)

print(log)

done()