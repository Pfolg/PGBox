# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   aboutPG |User    Pfolg
# 2024/8/10   20:02
import os
import threading
import time
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter as tk

flag = True


def openFile(path=".\\README.md"):
    kk = threading.Thread(target=lambda: os.system(path))
    kk.start()
    kk = None


def PGAbout(frame):

    ttk.Label(frame, text="关于PGBox", font=("微软雅黑", 16)).place(relx=.02, rely=.02)

    l1 = ttk.Label(frame, text=("By continuing to use this software, you agree to this LCENSE\n"
                                "继续使用本软件，即表示您同意本LCENSE"), font=("微软雅黑 bold", 12)
                   )

    s1 = ScrolledText(frame, width=80, height=15)

    bi = ttk.Button(
        frame, text="Bilibili", width=8,
        command=lambda: os.system("start https://space.bilibili.com/515553532")
    )

    git = ttk.Button(
        frame, text="GitHub", width=8,
        command=lambda: os.system("start https://github.com/Pfolg")
    )

    csdn = ttk.Button(
        frame, text="CSDN", width=8,
        command=lambda: os.system("start https://blog.csdn.net/qq_46603846?spm=1010.2135.3001.5421")
    )

    word = tk.StringVar()
    l = ttk.Label(frame, textvariable=word, font=("微软雅黑", 16))

    def scl():
        global flag
        aboutList = ["我是编程路上一个蹒跚学步的婴儿",
                     "我是Python新手村的新人",
                     "我是学不进Java的废材",
                     "我是一个喜欢花里胡哨的普通人",
                     "这个程序是我用来练习和进步的",
                     "谢谢你的见证！"]
        k = 0
        while flag:
            l.place(relx=.2, rely=.6)
            if k == len(aboutList):
                k = 0
            word.set(aboutList[k])
            k += 1
            time.sleep(3)

    def forgetThem():
        global flag
        flag = False
        for i in [l1, s1, bi, git, csdn, l]:
            i.place_forget()

    def showAuthor():
        forgetThem()
        global flag
        flag = True
        threading.Thread(target=scl).start()
        listBtu = [bi, git, csdn]
        for i in range(len(listBtu)):
            listBtu[i].place(relx=.1 + 0.1 * i, rely=.3)

    def showLICENSE():
        forgetThem()
        l1.place(relx=.1, rely=.3)
        s1.place(relx=.1, rely=.4)

    try:
        with open(".\\LICENSE.txt", "r", encoding="utf-8") as fg:
            c = fg.readlines()
        for i in c:
            s1.insert("end", i)
    except FileNotFoundError:
        pass
    finally:
        s1["state"] = "disabled"

    ttk.Button(
        frame, text="关于作者", width=8, command=showAuthor
    ).place(relx=.1, rely=.2)

    ttk.Button(
        frame, text="LICENSE", width=8, command=showLICENSE
    ).place(relx=.2, rely=.2)

    ttk.Button(frame, text="阅读文档", command=openFile, width=8).place(relx=.3, rely=.2)

    ttk.Button(
        frame, text="官方网站", command=lambda: os.system("start https://github.com/Pfolg/PGBox"), width=8
    ).place(relx=.4, rely=.2)
