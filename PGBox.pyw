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
import threading
import pystray
from PIL import Image
from pystray import MenuItem, Menu
from BoxTools.aboutPG import checkTag
import ctypes

AppName = "PGBox"
# AppVersion = "v1.1.1"  # 这里可以设置任意文本，于是我放了一个版本号在这里
icoPath = ".\\resource\\pg.ico"
pngPath = ".\\resource\\pg.png"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(AppName)
# time.sleep(5)

try:
    basicFileAsk = open(".\\setting\\Config.json", "r", encoding="utf-8")
    PGDict = json.load(basicFileAsk)
    agree = PGDict.get("agree")
    XHide = PGDict.get("XHide")
    basicFileAsk.close()
except BaseException:
    agree = False
    XHide = False


def openLICENSE(e):
    os.system("start .\\LICENSE.txt")


if not agree:
    def writeTure():
        if not os.path.exists(".\\setting\\Config.json"):  # 如果不存在配置文件就创建
            try:
                os.mkdir(".\\setting")
            except FileExistsError:
                pass
        with open(".\\setting\\Config.json", "w", encoding="utf-8") as firstFile:
            json.dump({"Warning": "请不要随意更改这个文件"}, firstFile, ensure_ascii=False, indent=4)  # 初始化文件夹
        with open(".\\setting\\Config.json", "r", encoding="utf-8") as myF1:
            myDict1 = json.load(myF1)
            myDict1["agree"] = True
        with open(".\\setting\\Config.json", "w", encoding="utf-8") as file:
            json.dump(myDict1, file, ensure_ascii=False, indent=4)
        # 重启是为了避免这个窗口影响主窗口
        ask_win.destroy()
        # os.system(f"start {sys.argv[0]}")
        # sys.exit()


    ask_win = tk.Tk()
    ask_win.title(AppName)
    a_screen_w, a_screen_h = ask_win.winfo_screenwidth(), ask_win.winfo_screenheight()
    a_w, a_h = int(a_screen_w / 4), int(a_screen_h / 4)
    ask_win.geometry(f'{a_w}x{a_h}+{int(a_screen_w / 3)}+{int(a_screen_h / 3)}')
    ask_win.resizable(False, False)
    try:
        ask_win.iconbitmap(icoPath)
        ask_win.wm_iconbitmap(pngPath)  # 这一句和最上面上面的两句相关联,但是放在这里用处不大(大概
    except BaseException:
        pass
    # ask_win.attributes('-alpha', 0.9)

    tk.Label(ask_win, text="\n继续使用本软件\n即表示您已阅读并同意本软件的", font=("微软雅黑", 16)).pack()
    a_label = tk.Label(ask_win, text="LICENSE", foreground="#ED1C24", font=("微软雅黑", 16), cursor="hand2")
    a_label.pack()
    a_label.bind("<Button-1>", openLICENSE)

    tk.Button(ask_win, text="Cancel", command=lambda: sys.exit()).place(relx=.7, rely=.7)
    tk.Button(ask_win, text="Confirm", command=writeTure).place(relx=.2, rely=.7)

    ask_win.mainloop()
    # ask_win = None


def quit_window(icon: pystray.Icon):
    icon.stop()
    window.destroy()


def show_window():
    window.deiconify()


def on_exit():
    window.withdraw()


def drawName(canva, info=AppName):
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
window.title(AppName)
screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
w, h = int(screen_w / 2), int(screen_h / 2)
window.geometry(f'{w}x{h}+{int(screen_w / 4)}+{int(screen_h / 4)}')
window.resizable(False, False)
window.iconbitmap(icoPath)
window.wm_iconbitmap(icoPath)  # 这一句和最上面上面的两句相关联
window.attributes('-alpha', 0.9)

menu = [
    MenuItem("检查更新", action=checkTag),
    MenuItem("官方网站", action=lambda: os.system("start https://github.com/Pfolg/PGBox")),
    MenuItem("设置", action=lambda: os.system("start .\\Setting.pyw")),
    MenuItem('PGBox', action=show_window, default=True, visible=False),
    Menu.SEPARATOR,
    MenuItem("计时器", action=lambda: os.system("start .\\BoxTools\\TimerAPP.pyw")),
    MenuItem("定时关机", lambda: threading.Thread(target=lambda: os.system(".\\BoxTools\\autoShutdownPro.py")).start()),
    MenuItem("txt文件加解密", action=lambda: os.system("start .\\BoxTools\\protectTxt.py")),
    Menu.SEPARATOR,
    MenuItem('退出', quit_window),
]
image = Image.open(pngPath)
icon = pystray.Icon("icon", image, AppName, menu)

if XHide:
    window.protocol('WM_DELETE_WINDOW', on_exit)

threading.Thread(target=icon.run, daemon=True).start()
# 启动动画（fake
# 你说我可不可以拿这个接广子
canva = tk.Canvas(window, width=w, height=h)
canva.pack()
drawName(canva)
canva.pack_forget()

frame0.basicFrame0(w, h, window)

window.mainloop()

# print("程序运行结束!")
