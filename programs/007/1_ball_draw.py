from tkinter import *

# 1.基本情報
ball = {
    "dirx": 15, # X方向のボールの速さ
    "diry": -15, # Y方向のボールの速さ
    "x": 300, # ボールの位置
    "y": 200,
    "w": 12, # ボールの幅
}

# 2.ウィンドウ生成
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

# 6.ループ処理
def game_loop():
    draw_objects()
    win.after(50, game_loop)

game_loop()
win.mainloop() #mainloopは必ず最終行に記述