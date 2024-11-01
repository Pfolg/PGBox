# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   FrameWin |User    Pfolg
# 2024/7/20   20:00
import webbrowser
from tkinter import ttk
import os
from tkinter import messagebox
import threading

lockInfo = ("没有弄懂这个程序怎么运行的请勿使用!\n"
            "BoxTools里有一个[WinLock.py]的文件，\n"
            "将它放到启动文件夹就可以实现掩耳盗铃的电脑锁了，\n"
            "所以极不推荐，\n"
            "首先你得更改里面的哈希值，不然后果很严重，\n"
            "可以利用[密码生成]生成密码的sha256值。")

btuComDict = {
    "Windows工具": lambda: os.system(
        "start \"\" \"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\""),
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
    "py 定时关机": lambda: threading.Thread(target=lambda: os.startfile(".\\BoxTools\\autoShutdownPro.py")).start(),
    "py 快捷方式脚本": lambda: os.startfile(".\\BoxTools\\shortcutMaker.pyw"),
    "web 文字转语音": lambda: webbrowser.open("https://ttsmaker.cn/"),
    "web 文件转换": lambda: webbrowser.open("https://convertio.co/zh/"),

    "Bug-3": 3,

    "web 免费素材图片": lambda: webbrowser.open("https://www.pexels.com/zh-cn/"),
    "py 计时器": lambda: os.startfile(".\\BoxTools\\TimerAPP.pyw"),
    "py 键盘记录": lambda: os.startfile(".\\BoxTools\\recordKeyboard.pyw"),
    "py 轰QW-2000": lambda: os.startfile(".\\BoxTools\\autoSend.py"),
    "py txt文件加解密": lambda: os.startfile(".\\BoxTools\\protectTxt.py"),

    "Bug-4": 4,

    "web 进制转换 9+": lambda: webbrowser.open(
        "https://cn.bing.com/search?q=%E8%AE%A1%E6%95%B0%E5%88%B6%E5%8F%98%E6%8D%A2%E5%99%A8"),
    "py 视频字幕合成": lambda: os.startfile(".\\BoxTools\\makeMp4.py"),
    "py 中文Gui-NirCmd": lambda: os.startfile(".\\BoxTools\\NirCmd-Gui-Chinese.pyw"),
    "web 快捷工具栏": lambda: webbrowser.open("https://blog.csdn.net/qq_46603846/article/details/143086863"),
    "py 激活Windows": lambda: os.startfile(".\\BoxTools\\runwin.py"),

    "Bug-5": 5,

    "py 查看WiFi信息": lambda: os.startfile(".\\BoxTools\\questionWifi.py")
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

    ttk.Button(
        frame, text="说明", width=8, command=lambda: messagebox.showinfo(
            title="提示信息",
            message="有些功能尚不稳定，请谨慎使用，若发现程序问题，请积极到官网反馈"
                    "\n开发者不会承担因不当使用程序而对用户财产造成损害之责任")
    ).place(relx=.8, rely=.9)
