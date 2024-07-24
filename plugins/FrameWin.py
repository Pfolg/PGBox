# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   FrameWin |User    Pfolg
# 2024/7/20   20:00
from tkinter import ttk
import os
from tkinter import messagebox
import threading


def autoShutdown():
    os.system(".\\plugins\\autoShutdown.py")


p1 = threading.Thread(target=autoShutdown)


def winFunction(frame):
    # 电脑锁（掩耳盗铃）
    lockInfo = ("plugins里有一个[WinLock.py]的文件，\n"
                "将它放到启动文件夹就可以实现掩耳盗铃的电脑锁了，\n"
                "所以极不推荐，\n"
                "可以利用plugins里的[makeKey.py]生成密码的哈希值。")
    ttk.Button(frame, text="电脑锁",
               command=lambda: messagebox.showinfo(title="提示信息", message=lockInfo)).place(relx=.02, rely=.1)

    # 定时关机
    ttk.Button(frame, text="定时关机",
               command=lambda: p1.start()).place(relx=.22, rely=.1)
