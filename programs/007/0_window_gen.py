from tkinter import *

#ウィンドウ生成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

#画面をループさせる
win.mainloop() #mainloopは必ず最終行に記述