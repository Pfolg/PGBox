# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   otherFunction |User    Pfolg
# 2024/7/20   16:02
import os
from tkinter import ttk


def otherFunction(frame):
    ttk.Label(frame, text="功能正在开发中……").place(relx=.4, rely=.9)
    btuComDict = {
        "限制应用启动": lambda: os.system("start .\\manageAPP\\mainWindow.pyw")
    }

    ttk.Label(frame, text="其他功能").place(relx=.02, rely=.02)
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
