from tkinter import *

# 1.基本情報
ball = {
    "dirx": 15, # X方向のボールの速さ
    "diry": -15,  # Y方向のボールの速さ
    "x": 300, # ボールの位置
    "y": 200,
    "w": 12, # ボールの幅
}

# 2.ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

# 4.画面を描画する
def draw_objects():
    cv.delete('all') # 既存の描画を破棄
    # 4.1ボールを描画
    cv.create_oval(
        ball["x"] - ball["w"], ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"],
        fill="green")

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
    move_ball() #追加
    win.after(50, game_loop) #50ms遅らせて実行

game_loop()
win.mainloop() # ゲームウィンドウを表示