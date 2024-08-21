# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   ClickDS |User    Pfolg
# 2024/8/12   14:03
import time
import pyautogui
import tkinter as tk
from tkinter import ttk, messagebox
import threading

flag = True
num = True


def clickS(delta):
    global flag
    while flag:
        pyautogui.click()
        time.sleep(delta)


def clickD(delta):
    global flag
    while flag:
        pyautogui.doubleClick()
        time.sleep(delta)


def mainC(t, x):
    global flag, num
    if num:
        num = False
        flag = True
        if x:
            t1 = threading.Thread(target=lambda: clickS(t))
            t1.start()
            t1 = None
        else:
            t2 = threading.Thread(target=lambda: clickD(t))
            t2.start()
            t2 = None


def changeFlag():
    global flag, num
    if flag:
        flag = False
        num = True


window = tk.Tk()
window.title("连点器")
screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
w, h = int(screen_w / 6), int(screen_h / 12)
window.geometry(f'{w}x{h}+{int(screen_w / 4)}+{int(screen_h / 4)}')
window.resizable(False, False)

ttk.Label(window, width=8, text="间隔时间").place(relx=.15, rely=0)
deltaTime = tk.IntVar()
ttk.Entry(window, width=8, textvariable=deltaTime).place(relx=.4, rely=0)

ttk.Button(
    window, text="单击", width=8, command=lambda: mainC(deltaTime.get(), True)
).place(relx=.1, rely=.5)

ttk.Button(
    window, text="双击", width=8, command=lambda: mainC(deltaTime.get(), False)
).place(relx=.4, rely=.5)

ttk.Button(
    window, text="停止", width=8, command=changeFlag
).place(relx=.7, rely=.5)
ttk.Button(
    window, text="Help", width=5,
    command=lambda: messagebox.showinfo(title="Help", message="可以将鼠标快速移动至左上角紧急停止")
).place(relx=.75, rely=0)

window.mainloop()
