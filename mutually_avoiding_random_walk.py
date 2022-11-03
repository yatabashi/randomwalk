from turtle import *
import random
import draw

# 設定
step = 10 # 亀の歩幅を指定。
distance = 60 # 二頭の亀の初期位置の距離を指定。step以上のstepの倍数で入力することを推奨。

# 準備
t1 = Turtle()
t2 = Turtle()
t1_is_alive = True
t2_is_alive = True
t1.speed(0)
t2.speed(0)

t1.penup(); t2.penup()
t1.setpos(-distance/2, 0); t2.setpos(distance/2, 0)
t1.pendown(); t2.pendown()

# log作成
log = {}

for t in [t1, t2]:
    x, y = t.pos()
    x, y = round(x), round(y)
    log[x] = {y}

# t1の始点描画
draw.origin(t1, 6)
draw.origin(t2, 6)

# 酔歩
while t1_is_alive or t2_is_alive:
    if t1_is_alive:
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

        # いずれの方向にも移動不可能である場合は移動を終了
        if len(directions) == 0:
            t1_is_alive = False
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

    if t2_is_alive:
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

        # いずれの方向にも移動不可能である場合は移動を終了
        if len(directions) == 0:
            t2_is_alive = False
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
