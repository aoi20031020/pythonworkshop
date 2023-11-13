from tkinter import *

# 1.基本情報
blocks = [] #ブロックの情報を扱う変数
block_size = {"x": 60, "y": 30} #ブロックの基本情報
ball = {"dirx": 15,"diry": -15,"x": 300,"y": 200,"w": 12} #ボールの基本情報
bar = {"x": 0, "w": 100} #バーの基本情報

# 2.ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

# 3.ゲームの初期化
def init_game():

    # 3.2ブロックを初期化
    for iy in range(0, 5):
        for ix in range(0, 10):
            color = "red"
            if (iy + ix) % 2 == 1: color = "blue"
            x1 = 4 + ix * block_size["x"]
            x2 = x1 + block_size["x"]
            y1 = 4 + iy * block_size["y"]
            y2 = y1 + block_size["y"]
            blocks.append([x1, y1, x2, y2, color])

# 4.画面を描画する
def draw_objects():
    cv.delete('all') # 既存の描画を破棄
    # 4.1ボールを描画
    cv.create_oval(
        ball["x"] - ball["w"], ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"],
        fill="green")
    # 4.2ブロックを一つずつ描画
    for w in blocks:
        x1, y1, x2, y2, c = w
        cv.create_rectangle(x1, y1, x2, y2, fill=c, width=0)
    # 4.3バーを描画
    cv.create_rectangle(bar["x"], 390, bar["x"] + bar["w"], 400, 
        fill="yellow")

# 5.ボールの移動
def move_ball():
    # 5.1仮の変数に移動後の値を記録
    bx = ball["x"] + ball["dirx"] #定義した速さ分座標をずらす
    by = ball["y"] + ball["diry"]
    # 5.2上左右の壁に当たった？
    if bx < 0 or bx > 600: ball["dirx"] *= -1
    if by < 0 or by > 400: ball["diry"] *= -1
    # 5.6移動内容を反映
    if 0 <= bx <= 600: ball["x"] = bx
    if 0 <= by <= 400: ball["y"] = by

# 6.ループ処理
def game_loop():
    draw_objects()
    move_ball()
    win.after(50, game_loop) #50ms遅らせて実行

init_game() #追加
game_loop()
win.mainloop() # ゲームウィンドウを表示

