# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   singleDouble |User    Pfolg
# 2024/7/23   12:46
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import threading


def writeClick():
    x = targetFile.get()
    with open(".\\run.bat", "w", encoding="utf-8") as file:
        file.write(f"start .\\BoxTools\\{x}\npause")


def runClick():
    x = targetFile.get()
    if x:
        os.startfile(f".\\BoxTools\\{x}")
        time.sleep(.5)


"singleClick.py"
"doubleClick.py"


def singleDouble(frame):
    global targetFile
    targetFile = tk.StringVar()
    ttk.Radiobutton(
        frame, text="自动单击", value="singleClick.py", variable=targetFile, width=10
    ).place(relx=.02, rely=.1)
    ttk.Radiobutton(
        frame, text="自动双击", value="doubleClick.py", variable=targetFile, width=10
    ).place(relx=.22, rely=.1)
    ttk.Button(
        frame, text="启动", command=lambda: threading.Thread(target=runClick).start()
    ).place(relx=.12, rely=.2)
    # ttk.Label(frame, text="请输入点击间隔").place(relx=.02, rely=.1)
    # ttk.Entry(frame, width=8, textvariable=delta).place(relx=.22, rely=.1)
    ttk.Button(
        frame, width=8, text="帮助",
        command=lambda: messagebox.showinfo(title="提示信息",
                                            message="此程序有一个极大的bug没修，暂无法使用!\n"
                                                    "基于pyautogui实现，鼠标移至左上角停止。\n"
                                                    "由于石粒有限，主程序关闭后子程序仍然会运行，\n"
                                                    "使用时请注意。\n"
                                                    "2.0也有相同Bug"
                                            )
    ).place(relx=.9, rely=.8)

    ttk.Button(
        frame, text="连点器2.0", width=8, command=lambda: os.system("start .\\BoxTools\\ClickDS.pyw")
    ).place(relx=.5, rely=.1)
