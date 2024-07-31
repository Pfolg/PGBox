# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   ToolsBox |User    Pfolg
# 2024/7/19   21:42
import sys
import tkinter as tk
import turtle
import time
import frame0


def drawName(canva, info="ToolsBox"):
    theScreen = turtle.TurtleScreen(canva)
    path = turtle.RawTurtle(theScreen)
    path.hideturtle()
    path.penup()
    path.fd(-300)
    path.pencolor("#f0d2dd")
    for i in info:
        path.write(i, font=('微软雅黑', 40, 'bold'))
        path.fd(80)
    time.sleep(1)


window = tk.Tk()
window.title("ToolsBox")
screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
w, h = int(screen_w / 2), int(screen_h / 2)
window.geometry(f'{w}x{h}+{int(screen_w / 4)}+{int(screen_h / 4)}')
window.resizable(False, False)
window.iconbitmap(".\\resource\\ico.ico")
window.attributes('-alpha', 0.9)

# 启动动画（fake
# 你说我可不可以拿这个接广子
canva = tk.Canvas(window, width=w, height=h)
canva.pack()
drawName(canva)
canva.pack_forget()

frame0.basicFrame0(w, h, window)

window.mainloop()
