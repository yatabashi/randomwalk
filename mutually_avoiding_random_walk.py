from turtle import *
import random

# 設定
step = 10 # 
distance = 60 # step以上のstepの倍数で入力。

# 準備
t1 = Turtle(); t2 = Turtle()
flag_t1 = True; flag_t2 = True

t1.penup(); t2.penup()
t1.setpos(-distance/2, 0); t2.setpos(distance/2, 0)
t1.pendown(); t2.pendown()

t1.speed(0); t2.speed(0)

# log作成
log = {}

for t in [t1, t2]:
    x, y = t.pos()
    x, y = round(x), round(y)
    log[x] = {y}

# t1の始点描画
t1.forward(3)
t1.left(90)

t1.begin_fill()
t1.forward(3)
for _ in range(3):
    t1.left(90)
    t1.forward(6)
t1.left(90)
t1.forward(3)
t1.end_fill()

t1.left(90)
t1.forward(3)

# t2の始点描画
t2.forward(3)
t2.left(90)

t2.begin_fill()
t2.forward(3)
for _ in range(3):
    t2.left(90)
    t2.forward(6)
t2.left(90)
t2.forward(3)
t2.end_fill()

t2.left(90)
t2.forward(3)

# 酔歩
while flag_t1 or flag_t2:
    if flag_t1:
        # 現在地取得
        x1, y1 = t1.pos()
        x1, y1 = round(x1), round(y1)

        # 移動可能な方向を取得
        directions = [0, 90, 180, 270]

        if y1+step in log[x1]:
            directions.remove(90)
        
        if y1-step in log[x1]:
            directions.remove(270)

        if x1+step in log.keys():
            if y1 in log[x1+step]:
                directions.remove(0)

        if x1-step in log.keys():
            if y1 in log[x1-step]:
                directions.remove(180)

        if len(directions) == 0:
            flag_t1 = False
            continue

        # 移動方向を決定
        randdirection = random.choice(directions)
        t1.setheading(randdirection)

        # 現在地と移動方向を出力
        print((x1, y1), randdirection)

        # 移動
        t1.forward(step)

        # 現在地をlogに追加
        if randdirection == 0:
            if x1+step in log.keys():
                log[x1+step].add(y1)
            else:
                log[x1+step] = {y1}
        elif randdirection == 90:
            log[x1].add(y1+step)
        elif randdirection == 180:
            if x1-step in log.keys():
                log[x1-step].add(y1)
            else:
                log[x1-step] = {y1}
        elif randdirection == 270:
            log[x1].add(y1-step)

    if flag_t2:
        # 現在地取得
        x2, y2 = t2.pos()
        x2, y2 = round(x2), round(y2)

        # 移動可能な方向を取得
        directions = [0, 90, 180, 270]

        if y2+step in log[x2]:
            directions.remove(90)
        
        if y2-step in log[x2]:
            directions.remove(270)

        if x2+step in log.keys():
            if y2 in log[x2+step]:
                directions.remove(0)

        if x2-10 in log.keys():
            if y2 in log[x2-10]:
                directions.remove(180)

        if len(directions) == 0:
            flag_t2 = False
            continue

        # 移動方向を決定
        randdirection = random.choice(directions)
        t2.setheading(randdirection)

        # 現在地と移動方向を出力
        print((x2, y2), randdirection)

        # 移動
        t2.forward(step)

        # 移動先をlogに追加
        if randdirection == 0:
            if x2+step in log.keys():
                log[x2+step].add(y2)
            else:
                log[x2+step] = {y2}
        elif randdirection == 90:
            log[x2].add(y2+step)
        elif randdirection == 180:
            if x2-step in log.keys():
                log[x2-step].add(y2)
            else:
                log[x2-step] = {y2}
        elif randdirection == 270:
            log[x2].add(y2-step)

print(log)

done()