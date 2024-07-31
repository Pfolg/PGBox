# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   frameMHY |User    Pfolg
# 2024/7/31   19:08
import os
from tkinter import messagebox, ttk

btuComDict = {
    "Herta_kuru": lambda: os.system("start https://duiqt.github.io/herta_kuru/"),
    "Genshin Impact": lambda: os.system("start https://ys.mihoyo.com/main/"),
    "Honkai：StarRail": lambda: os.system("start https://sr.mihoyo.com/"),
    "Snap.Hutao": lambda: os.system("start https://hut.ao/zh/"),
    "Vilipix": lambda: os.system("start https://www.vilipix.com/"),

    "Bug-1": 1,

}


def winFunction(frame):
    ttk.Label(frame, text="二刺猿\t作者分享的一些网站，点一下就能打开").place(relx=.02, rely=.02)
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
