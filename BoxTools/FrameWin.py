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
    os.system(".\\BoxTools\\autoShutdown.py")


def openUrl(url):
    with open(".\\run.bat", "w", encoding="utf-8") as f:
        f.write(f"start {url}")
    os.system(".\\run.bat")
    os.remove(".\\run.bat")
    time.sleep(2)
    pyautogui.press("f11")


def start3process():
    p1 = threading.Thread(target=autoShutdown)
    p1.start()
    p1 = None


lockInfo = ("没有弄懂这个程序怎么运行的请勿使用!\n"
            "BoxTools里有一个[WinLock.py]的文件，\n"
            "将它放到启动文件夹就可以实现掩耳盗铃的电脑锁了，\n"
            "所以极不推荐，\n"
            "可以利用BoxTools里的[makeKey.py]生成密码的哈希值。")

btuComDict = {
    "Windows工具": lambda: os.system("start \"\" \"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Administrative "
                                     "Tools\""),
    "文件资源管理器": lambda: os.system("start explorer.exe"),
    "设置": lambda: os.system("start ms-settings:"),
    "控制面板": lambda: os.system("start control"),
    "Windows安全中心": lambda: os.system("start ms-settings:windowsdefender"),

    "Bug-1": 1,

    "系统信息": lambda: os.system("start msinfo32"),
    "任务管理器": lambda: os.system("start taskmgr"),
    "记事本": lambda: os.system("start notepad"),
    "画图": lambda: os.system("start mspaint"),
    "计算器": lambda: os.system("start calc"),

    "Bug-2": 2,

    "电脑锁": lambda: messagebox.showinfo(title="提示信息", message=lockInfo),
    "定时关机": lambda: start3process(),
    "变身黑客1": lambda: messagebox.showinfo(
        title="你也是闲的", message="这是一个扫盘命令:\n"
                                    "win+r\n"
                                    "cmd\n"
                                    "color a\n"
                                    "dir/s"),
    "变身黑客2": lambda: openUrl("http://geekprank.com/hacker"),
    "关于天文": lambda: openUrl("https://stars.chromeexperiments.com/"),

    "bug-3": 3,
}


def winFunction(frame):
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
