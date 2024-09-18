# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   ToolsBox |User    Pfolg
# 2024/7/19   21:42
import json
import os
import sys
import tkinter as tk
import turtle
import time
import frame0

nowTag = "v1.0.12"
# time.sleep(5)
try:
    basicFileAsk = open(".\\setting\\Config.txt", "r", encoding="utf-8")
    PGDict = json.load(basicFileAsk)
    agree = PGDict.get("agree")
    basicFileAsk.close()
except FileNotFoundError:
    agree = False


def openLICENSE(e):
    os.system("start .\\LICENSE.txt")


if not agree:
    def writeTure():
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF1:
            myDict1 = json.load(myF1)
            myDict1["agree"] = True
        with open(".\\setting\\Config.txt", "w", encoding="utf-8") as file:
            json.dump(myDict1, file, ensure_ascii=False, indent=4)
        # 重启是为了避免这个窗口影响主窗口
        ask_win.destroy()
        # os.system(f"start {sys.argv[0]}")
        # sys.exit()


    ask_win = tk.Tk()
    ask_win.title(f"PGBox {nowTag}")
    a_screen_w, a_screen_h = ask_win.winfo_screenwidth(), ask_win.winfo_screenheight()
    a_w, a_h = int(a_screen_w / 4), int(a_screen_h / 4)
    ask_win.geometry(f'{a_w}x{a_h}+{int(a_screen_w / 3)}+{int(a_screen_h / 3)}')
    ask_win.resizable(False, False)
    ask_win.iconbitmap(".\\resource\\pg.ico")
    # ask_win.attributes('-alpha', 0.9)

    tk.Label(ask_win, text="\n继续使用本软件\n即表示您已阅读并同意本软件的", font=("微软雅黑", 16)).pack()
    a_label = tk.Label(ask_win, text="LICENSE", foreground="#ED1C24", font=("微软雅黑", 16), cursor="hand2")
    a_label.pack()
    a_label.bind("<Button-1>", openLICENSE)

    tk.Button(ask_win, text="Cancel", command=lambda: sys.exit()).place(relx=.7, rely=.7)
    tk.Button(ask_win, text="Confirm", command=writeTure).place(relx=.2, rely=.7)

    ask_win.mainloop()
    # ask_win = None


def drawName(canva, info="PGBox"):
    theScreen = turtle.TurtleScreen(canva)
    path = turtle.RawTurtle(theScreen)
    path.hideturtle()
    path.penup()
    path.fd(-200)
    path.pencolor("#000000")
    for i in info:
        path.write(i, font=('微软雅黑', 40, 'bold'))
        path.fd(80)
    time.sleep(1)


window = tk.Tk()
window.title(f"PGBox {nowTag}")
screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
w, h = int(screen_w / 2), int(screen_h / 2)
window.geometry(f'{w}x{h}+{int(screen_w / 4)}+{int(screen_h / 4)}')
window.resizable(False, False)
window.iconbitmap(".\\resource\\pg.ico")
window.attributes('-alpha', 0.9)

# 启动动画（fake
# 你说我可不可以拿这个接广子
canva = tk.Canvas(window, width=w, height=h)
canva.pack()
drawName(canva)
canva.pack_forget()

frame0.basicFrame0(w, h, window)

window.mainloop()

# print("程序运行结束!")
