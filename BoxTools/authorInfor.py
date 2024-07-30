# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   authorInfor |User    Pfolg
# 2024/7/29   14:59
import os
import time
from tkinter import ttk
from tkinter import messagebox
import threading

aboutList = ["我是编程路上一个蹒跚学步的婴儿",
             "我是Python新手村的村民",
             "我是学不进Java的废材",
             "我是一个喜欢花里胡哨的普通人",
             "这个程序是我用来练习和进步的",
             "谢谢你的见证！"]


def authorInfor(frame):
    ttk.Label(frame, text="关于作者-Pfolg").place(relx=.02, rely=.02)

    def showLabel():
        i = 0
        while True:
            try:
                a = ttk.Label(frame, text=aboutList[i], font=("微软雅黑", 16), width=40)
                a.place(relx=.3, rely=.1)
            except RuntimeError:
                break
            if i == len(aboutList) - 1:
                i = 0
            i += 1
            time.sleep(3)

    # 开辟一个线程使事件循环，建议关闭（注释掉）
    threading.Thread(target=showLabel).start()

    ttk.Button(
        frame, text="Bilibili",
        command=lambda: os.system("start https://space.bilibili.com/515553532")
    ).place(relx=.2, rely=.5)

    ttk.Button(
        frame, text="GitHub",
        command=lambda: os.system("start https://github.com/Pfolg")
    ).place(relx=.3, rely=.6)

    ttk.Button(
        frame, text="CSDN",
        command=lambda: os.system("start https://blog.csdn.net/qq_46603846?spm=1010.2135.3001.5421")
    ).place(relx=.4, rely=.7)

    ttk.Button(
        frame, text="作者的个人网站",
        command=lambda: messagebox.showinfo(title="提示信息", message="作者的个人网站早在24年6月崩啦！")
    ).place(relx=.5, rely=.6)

    ttk.Button(
        frame, text="QQ&微信",
        command=None
    ).place(relx=.6, rely=.5)

