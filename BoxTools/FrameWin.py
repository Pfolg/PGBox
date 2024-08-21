# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   FrameWin |User    Pfolg
# 2024/7/20   20:00
from tkinter import ttk
import os
from tkinter import messagebox
import threading


def autoShutdown():
    os.system(".\\BoxTools\\autoShutdown.py")


def start3process():
    p1 = threading.Thread(target=autoShutdown)
    p1.start()
    p1 = None


lockInfo = ("没有弄懂这个程序怎么运行的请勿使用!\n"
            "BoxTools里有一个[WinLock.py]的文件，\n"
            "将它放到启动文件夹就可以实现掩耳盗铃的电脑锁了，\n"
            "所以极不推荐，\n"
            "首先你得更改里面的哈希值，不然后果很严重，\n"
            "可以利用[密码生成]生成密码的sha256值。")

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
    "py 打开程序所在目录": lambda: os.system("start .\\"),
    "web 文字转语音": lambda: os.system("start https://ttsmaker.cn/"),
    "web 文件转换": lambda: os.system("start https://convertio.co/zh/"),

    "Bug-3": 3,

    "web 免费素材图片": lambda: os.system("start https://www.pexels.com/zh-cn/"),
    "py 计时器": lambda: os.system("start .\\BoxTools\\TimerAPP.pyw"),
    "py 键盘记录": lambda: os.system("start .\\BoxTools\\recordKeyboard.pyw"),
    "py 轰QW-2000": lambda: os.system("start .\\BoxTools\\autoSend.py"),

}


def winFunction(frame):
    ttk.Label(frame, text="电脑功能").place(relx=.02, rely=.02)
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
