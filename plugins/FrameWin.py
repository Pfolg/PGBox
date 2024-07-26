# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   FrameWin |User    Pfolg
# 2024/7/20   20:00
import time
from tkinter import ttk
import os
from tkinter import messagebox
import threading
import pyautogui


def autoShutdown():
    os.system(".\\plugins\\autoShutdown.py")


def openUrl(url):
    with open(".\\run.bat", "w", encoding="utf-8") as f:
        f.write(f"start {url}")
    os.system(".\\run.bat")
    os.remove(".\\run.bat")
    time.sleep(2)
    pyautogui.press("f11")


p1 = threading.Thread(target=autoShutdown)


def winFunction(frame):
    # 电脑锁（掩耳盗铃）
    lockInfo = ("没有弄懂这个程序怎么运行的请勿使用!\n"
                "plugins里有一个[WinLock.py]的文件，\n"
                "将它放到启动文件夹就可以实现掩耳盗铃的电脑锁了，\n"
                "所以极不推荐，\n"
                "可以利用plugins里的[makeKey.py]生成密码的哈希值。")
    ttk.Button(frame, text="电脑锁",
               command=lambda: messagebox.showinfo(title="提示信息", message=lockInfo)).place(relx=.02, rely=.1)

    # 定时关机
    ttk.Button(frame, text="定时关机",
               command=lambda: p1.start()).place(relx=.22, rely=.1)

    # 凡人秒变黑客（扫盘命令）
    ttk.Button(
        frame, text="变身黑客1", command=lambda: messagebox.showinfo(
            title="你也是闲的", message="这是一个扫盘命令:\n"
                                        "win+r\n"
                                        "cmd\n"
                                        "color a\n"
                                        "dir/s")
    ).place(relx=.42, rely=.1)

    ttk.Button(
        frame, text="变身黑客2", command=lambda: openUrl("http://geekprank.com/hacker")
    ).place(relx=.62, rely=.1)

    ttk.Button(
        frame, text="关于天文", command=lambda: openUrl("https://stars.chromeexperiments.com/")
    ).place(relx=.82, rely=.1)
