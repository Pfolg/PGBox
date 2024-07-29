# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   readLICENSE |User    Pfolg
# 2024/7/29   15:50
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk


def readLICENSE(frame):
    ttk.Label(frame, text=("By continuing to use this software, you agree to this LCENSE\n"
                           "继续使用本软件，即表示您同意本LCENSE"), font=("微软雅黑 bold", 12)
              ).place(relx=.1, rely=.02)
    s1 = ScrolledText(frame, width=80, height=20)
    s1.place(relx=.1, rely=.18)

    try:
        with open(".\\LICENSE.txt", "r", encoding="utf-8") as fg:
            c = fg.readlines()
        for i in c:
            s1.insert("end", i)
    except FileNotFoundError:
        pass
    finally:
        s1["state"] = "disabled"
