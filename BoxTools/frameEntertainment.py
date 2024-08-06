# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   frameMHY |User    Pfolg
# 2024/7/31   19:08
import os
import time
from tkinter import messagebox, ttk
import pyautogui


def openUrl(url):
    with open(".\\run.bat", "w", encoding="utf-8") as f:
        f.write(f"start {url}")
    os.system(".\\run.bat")
    os.remove(".\\run.bat")
    time.sleep(2)
    pyautogui.press("f11")


btuComDict = {
    "Herta_kuru": lambda: os.system("start https://duiqt.github.io/herta_kuru/"),
    "Genshin Impact": lambda: os.system("start https://ys.mihoyo.com/main/"),
    "Honkai：StarRail": lambda: os.system("start https://sr.mihoyo.com/"),
    "Snap.Hutao": lambda: os.system("start https://hut.ao/zh/"),
    "Vilipix": lambda: os.system("start https://www.vilipix.com/"),

    "Bug-1": 1,

    "LifeRestart": lambda: os.system("start https://liferestart.syaro.io/public/index.html"),
    "变身黑客1": lambda: messagebox.showinfo(
        title="你也是闲的", message="这是一个扫盘命令:\n"
                                    "win+r\n"
                                    "cmd\n"
                                    "color a\n"
                                    "dir/s"),
    "变身黑客2": lambda: openUrl("http://geekprank.com/hacker"),
    "关于天文": lambda: openUrl("https://stars.chromeexperiments.com/"),
    "Bilibili": lambda: os.system("start https://www.bilibili.com/"),

    "Bug-2": 2,

    "编程语言流行指数": lambda: os.system("start https://www.tiobe.com/tiobe-index/")

}


def EntertainmentFrame(frame):
    ttk.Label(frame, text="Entertainment\t作者分享的一些网站，点一下就能打开").place(relx=.02, rely=.02)
    i = 0
    j = 1
    for key in btuComDict:
        if i < 5:
            if j < 9:
                ttk.Button(
                    frame, text=key, command=btuComDict.get(key)
                ).place(relx=(0.02 + (i * 2 / 10)), rely=j / 10)
                i += 1
            else:
                break
        else:
            i = 0
            j += 1
