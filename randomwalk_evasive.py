from turtle import *
import draw
import random

# 三つ以上の亀を相互回避酔歩させる

# 設定
num_of_turtles = 4 # 亀の頭数。1以上の整数を入力
init_positions = [(50, 50), (-50, 50), (-50, -50), (50, -50)] # 亀の初期位置。2つの実数からなるタプルnum_of_turtles個の配列を入力。相互回避が成立するためには、任意の2つのタプルの第n要素について、その差がstepの正整数倍である必要がある（n=0,1）。
step = 10 # 亀の歩幅。0より大きい実数を入力

# 変数定義
turtles = []
is_alive = []

# Turtle生成
for i in range(num_of_turtles):
    command = f"""t{i} = Turtle()
turtles.append(t{i})"""
    exec(command)

# Turtleの設定
for (t, init_pos) in zip(turtles, init_positions):
    is_alive.append(True)
    t.speed(0)

    t.penup()
    t.setpos(init_pos[0], init_pos[1])
    t.pendown()

# log作成
log = {}

for init_pos in init_positions:
    x, y = init_pos
    
    if x in log.keys():
        log[x].add(y)
    else:
        log[x] = {y}


# 始点描画
for t in turtles:
    draw.origin(t, 6)

# 酔歩
while any(is_alive):
    for (t, t_is_alive, num) in zip(turtles, is_alive, range(num_of_turtles)):
        if t_is_alive:
            # 現在地取得
            x, y = t.pos()
            x, y = round(x), round(y)

            # 移動可能な方向を取得
            directions = [0, 90, 180, 270]

            if x+step in log.keys():
                if y in log[x+step]:
                    directions.remove(0)

            if y+step in log[x]:
                directions.remove(90)

            if x-step in log.keys():
                if y in log[x-step]:
                    directions.remove(180)

            if y-step in log[x]:
                directions.remove(270)

            # いずれの方向にも移動不可能である場合は移動を終了
            if len(directions) == 0:
                is_alive[num] = False
                continue

            # 移動方向を決定
            randdirection = random.choice(directions)
            t.setheading(randdirection)

            # 現在地と移動方向を出力
            print((x, y), randdirection)

            # 移動
            t.forward(step)

            # 現在地をlogに追加
            if randdirection == 0:
                if x+step in log.keys():
                    log[x+step].add(y)
                else:
                    log[x+step] = {y}
            elif randdirection == 90:
                log[x].add(y+step)
            elif randdirection == 180:
                if x-step in log.keys():
                    log[x-step].add(y)
                else:
                    log[x-step] = {y}
            elif randdirection == 270:
                log[x].add(y-step)

# 終了
print(log)
done()
