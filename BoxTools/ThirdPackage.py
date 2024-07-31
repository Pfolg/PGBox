# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   ThirdPackage |User    Pfolg
# 2024/7/20   21:55
import json
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import os

listCommand = [
    "pip config unset global.index-url",
    "pip config set global.index-url ",
    "pip freeze > "
]

dictUrl = {
    "阿里镜像": "https://mirrors.aliyun.com/pypi/simple/",
    "百度镜像": "https://mirror.baidu.com/pypi/simple/",
    "清华镜像(推荐)": "https://pypi.tuna.tsinghua.edu.cn/simple/",
    "中科大镜像": "https://pypi.mirrors.ustc.edu.cn/simple/",
    "豆瓣镜像": "http://pypi.douban.com/simple/",
    "搜狐镜像": "http://mirrors.sohu.com/Python/",
    "华中科大镜像": "https://pypi.hustunique.com/",
    "山东理工大学镜像": "https://pypi.hustunique.com/"
}

listUrl = [*dictUrl.keys()]


def osRun():
    os.system(".\\run.bat")
    time.sleep(0.5)
    os.remove(".\\run.bat")


def process(vl: int):
    try:
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            path = myDict.get("ThirdPackageOutputFile")
    except BaseException:
        pass
    if vl == 4:
        text = listCommand[0]
    elif vl == 3:
        if c1.get():
            text = listCommand[1] + dictUrl.get(c1.get())
        else:
            messagebox.showerror(title="Error", message="请选择镜像源!")
            return False
    elif vl == 6:
        if path:
            text = listCommand[2] + f"{path}"
            messagebox.showinfo(title="提示信息", message=f"将导出至[{path}]")
        else:
            messagebox.showerror(title="Error", message="请设置导出文件夹!")
            return False
    elif vl == 1:
        if packageName.get():
            text = f"pip install {packageName.get()}"
        else:
            messagebox.showerror(title="Error", message="请输入包名!")
            return False
    elif vl == 2:
        if packageName.get():
            text = f"pip uninstall {packageName.get()}"
        else:
            messagebox.showerror(title="Error", message="请输入包名!")
            return False
    elif vl == 5:
        if packageName.get() and c1.get():
            text = f"pip install {packageName.get()} -i {dictUrl.get(c1.get())}"
        else:
            messagebox.showerror(title="Error", message="请输入包名!\n或者\n请选择镜像源!")
            return False
    elif vl == 7:
        text = "pip install pip-review\npip-review --interactive"
    elif vl == 8:
        text = "pip install pip-review\npip-review --a"
    else:
        return False

    with open(".\\run.bat", "w", encoding="utf-8") as file:
        file.write(text + "\npause")
    x = threading.Thread(target=osRun)
    x.start()
    x = None


def ThirdPackage(frame):
    ttk.Label(frame, text="专为Python懒人打造的交互版pip程序(大概吧)").place(relx=.32, rely=.005)
    flag = tk.IntVar()
    r0 = ttk.Button(frame, text="安装包", width=18, command=lambda: nextStep(1))
    r1 = ttk.Button(frame, text="卸载包", width=18, command=lambda: nextStep(2))
    r2 = ttk.Button(frame, text="添加镜像源", width=18, command=lambda: nextStep(3))
    r3 = ttk.Button(frame, text="移除镜像源", width=18, command=lambda: nextStep(4))
    r4 = ttk.Button(frame, text="使用镜像源安装某包", width=18, command=lambda: nextStep(5))
    r5 = ttk.Button(frame, text="导出已安装包信息", width=18, command=lambda: nextStep(6))
    r6 = ttk.Button(frame, text="升级包(不推荐)", width=18, command=lambda: nextStep(7))
    r7 = ttk.Button(frame, text="自动升级包(极不推荐)", width=18, command=lambda: nextStep(8))

    listRadiobutton = [r0, r1, r2, r3, r4, r5, r6, r7]
    for i in range(len(listRadiobutton)):
        listRadiobutton[i].place(relx=.02, rely=(i + 1) / 10)

    global packageName, c1
    packageName = tk.StringVar()
    l1 = ttk.Label(frame, text="输入包名:")
    e1 = ttk.Entry(frame, width=12, textvariable=packageName)
    b1 = ttk.Button(frame, width=8, text="确定", command=lambda: process(value))
    b2 = ttk.Button(frame, width=16, text="移除镜像源", command=lambda: process(4))
    c1 = ttk.Combobox(frame, width=16, values=listUrl)
    b3 = ttk.Button(frame, text="添加镜像源", width=16, command=lambda: process(3))
    b4 = ttk.Button(frame, text="导出已安装包信息", width=16, command=lambda: process(6))
    b5 = ttk.Button(frame, text="升级包", width=16, command=lambda: process(7))
    b6 = ttk.Button(frame, text="自动升级包", width=16, command=lambda: process(8))

    def forgetAll():
        for bt in [l1, e1, b1, b2, b3, c1, b4, b5, b6]:
            bt.place_forget()

    def nextStep(x):
        global value
        value = x
        if value == 1 or value == 2:
            forgetAll()
            l1.place(relx=.22, rely=.1)
            e1.place(relx=.22, rely=.2)
            b1.place(relx=.4, rely=.2)
        elif value == 3:
            forgetAll()
            c1.place(relx=.22, rely=.3)
            b3.place(relx=.42, rely=.3)
        elif value == 4:
            forgetAll()
            b2.place(relx=.22, rely=.4)
        elif value == 5:
            forgetAll()
            l1.place(relx=.22, rely=.1)
            e1.place(relx=.22, rely=.2)
            b1.place(relx=.4, rely=.2)
            c1.place(relx=.22, rely=.3)
        elif value == 6:
            forgetAll()
            b4.place(relx=.22, rely=.6)
        elif value == 7:
            forgetAll()
            b5.place(relx=.22, rely=.7)
        elif value == 8:
            forgetAll()
            b6.place(relx=.22, rely=.8)
        else:
            forgetAll()

    msg = ("注意事项:\n"
           "0、没有Python解释器的请勿使用!\n"
           "1、安装和卸载包都必须填入包名;\n"
           "2、添加镜像源可以选择一个添加;\n"
           "3、移除镜像源是一次性全部移除;\n"
           "4、使用镜像源安装某包需要包名和镜像源;\n"
           "5、导出已安装包信息需要提前设置路径;\n"
           "6、两种升级包程序都是基于pip-review使用的,\n"
           "    程序会自动安装这个库,\n"
           "    没有Python环境就无法使用;\n"
           "7、本插件基于os库实现,会有一个命令行窗口;\n"
           "8、同时空条件下一次只能安装或卸载一个包,\n"
           "    否则会导致pip的异常。")

    ttk.Button(frame, text="注意事项", width=8,
               command=lambda: messagebox.showinfo(title="注意事项", message=msg)).place(relx=.9, rely=.8)
