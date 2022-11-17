from turtle import *
import random
import draw

# 単独の自己回避酔歩

# 設定
step = 10 # 亀の歩幅。0より大きい実数を入力

# 準備
t = Turtle()

t.speed(0)

log = {}
sac = {}
flag = True

# 画面クリック時の挙動の設定
def clicked(x,y):
    global flag
    flag = False
onscreenclick(clicked)

# 始点描画
draw.origin(t, 6)

# 酔歩
while flag:
    # 現在地取得
    x, y = t.pos()
    x, y = round(x), round(y) # 上下左右のいずれかに進むはずだが、なぜか誤差が生まれるので丸めて無視

    # 現在地をlogに追加
    if x in log.keys():
        log[x].add(y)
    else:
        log[x] = {y}

    # 必要であればsacにkey x を作成
    if x not in sac.keys():
        sac[x] = set()

    # 移動可能な方向を取得
    directions = [0, 90, 180, 270]

    # logとsacを確認し、各方向について進めるかどうか調べる
    if y+step in log[x] | sac[x] :
        directions.remove(90)
    
    if y-step in log[x] | sac[x]:
        directions.remove(270)

    if x+step in log.keys() | sac.keys():
        if y in log[x+step]:
            directions.remove(0)

    if x-step in log.keys() | sac.keys():
        if y in log[x-step]:
            directions.remove(180)

    if len(directions) == 0:
        # 現在地をsacに追加
        if x in log.keys():
            sac[x].add(y)
        else:
            sac[x] = {y}

        # 一歩戻る
        t.undo()

        continue

    # 移動方向を取得
    randdirection = random.choice(directions)
    t.setheading(randdirection)

    # 現在地と移動方向を出力
    print((x, y), randdirection)

    # 移動
    t.forward(step)

# 終了
print(log)
done()
