# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   name |User    Pfolg
# 2024/7/31   17:02
# If you can't recognize the words,ignore them.
import os
import subprocess
import threading
import time
from tkinter import ttk, messagebox
import tkinter as tk
import random


def openurl(e):
    os.system("start https://www.sysgeek.cn/windows-11-view-wi-fi-password/")


def wifiFrame(frame):
    ttk.Label(frame, text="WIFI_Information").place(relx=.02, rely=.02)
    tk.Button(
        frame, text="Break Into", width=8, command=lambda: messagebox.showinfo(
            title="Information", message=
            "I failed in this way, and it's illegal.\n"
            "GIVE UP\n"
            "OR find someone who can do the easy thing."
        ), background="red"
    ).place(relx=.46, rely=.3)

    tk.Button(
        frame, text="Get Now WIFI", command=lambda: messagebox.showinfo(
            title="Information", message="Some badly error happened, this function has been deleted."
        ), background="red"
    ).place(relx=.445, rely=.4)

    tk.Button(
        frame, text="Get Others", command=lambda: os.system("start .\\BoxTools\\questionWifi.py"), background="green"
    ).place(relx=.445, rely=.5)

    l1 = ttk.Label(
        frame, text="How to view it on your Windows", foreground="blue", cursor="hand2"
    )
    l1.place(relx=.02, rely=.9)
    l1.bind("<Button-1>", openurl)
