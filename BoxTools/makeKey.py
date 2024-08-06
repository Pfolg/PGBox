# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   makeKey |User    Pfolg
# 2024/7/15   22:31
import hashlib
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random

PWD_Dict = {"纯数字": "1234567890",  # 纯数字
            "数字+小写字母": "1234567890abcdefghijklmnopqrstuvwxyz",  # 数字+小写字母
            "数字+大写字母": "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # 数字+大写字母
            "纯小写字母": "abcdefghijklmnopqrstuvwxyz",  # 纯小写字母
            "纯大写字母": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # 纯大写字母
            "数字+小写字母+符号": "1234567890abcdefghijklmnopqrstuvwxyz!@#$%&*?.",  # 数字+小写字母+符号
            "数字+大写字母+符号": "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?.",  # 数字+大写字母+符号
            "数字+字母": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",  # 数字+字母
            "终极奥义": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?."  # 终极奥义
            }

pwdListKeys = list(PWD_Dict.keys())


def ConSha256(original_string):
    if original_string:  # 假设我们有一个字符串
        # 选择一个哈希算法，比如sha256
        hash_object = hashlib.sha256(original_string.encode())

        # 获取十六进制格式的哈希值
        hex_dig = hash_object.hexdigest()

        print(hex_dig, type(hex_dig))  # 输出哈希值

        scText["state"] = "normal"
        scText.insert("end", "sha256：" + hex_dig + "\n")
        scText["state"] = "disabled"


def ConMD5(x):
    if x:
        # 选择一个哈希算法，比如MD5
        hash_object = hashlib.md5(x.encode())

        # 获取十六进制格式的哈希值
        hex_dig = hash_object.hexdigest()
        scText["state"] = "normal"
        scText.insert("end", "md5：" + hex_dig + "\n")
        scText["state"] = "disabled"


def makeKey(key, num):
    if key and num.isdigit():
        x = PWD_Dict.get(key)
        y = int(num)
        if x and y:
            pwd = ""
            for i in range(y):
                j = random.randint(0, len(x) - 1)
                pwd += x[j]
            scText["state"] = "normal"
            scText.insert("end", f"{key}：{pwd}\n")
            scText["state"] = "disabled"


def keyFrame(frame):
    ttk.Label(
        frame, text="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?.", font=("微软雅黑", 10),
    ).place(relx=.02, rely=.02)
    # sha256
    sha256 = tk.StringVar()
    ttk.Label(frame, text="生成Sha256码").place(relx=.02, rely=.2)
    ttk.Entry(frame, width=30, textvariable=sha256).place(relx=.2, rely=.2)
    ttk.Button(frame, width=8, text="生成", command=lambda: ConSha256(sha256.get())).place(relx=.62, rely=.2)

    # md5
    md5 = tk.StringVar()
    ttk.Label(frame, text="生成md5码").place(relx=.02, rely=.3)
    ttk.Entry(frame, width=30, textvariable=md5).place(relx=.2, rely=.3)
    ttk.Button(frame, width=8, text="生成", command=lambda: ConMD5(md5.get())).place(relx=.62, rely=.3)

    # 一般
    choice = tk.StringVar()
    ttk.Label(frame, text="生成一般密码").place(relx=.02, rely=.4)
    ttk.Combobox(frame, values=pwdListKeys, width=20, textvariable=choice).place(relx=.2, rely=.4)
    ttk.Label(frame, text="密码长度", width=8).place(relx=.5, rely=.4)
    pwdNum = tk.StringVar()
    ttk.Entry(frame, width=8, textvariable=pwdNum).place(relx=.62, rely=.4)
    ttk.Button(
        frame, width=8, text="生成", command=lambda: makeKey(choice.get(), pwdNum.get())
    ).place(relx=.72, rely=.4)

    # 结果输出框
    global scText
    scText = ScrolledText(frame, width=60, height=5, state="disabled")
    scText.place(relx=.1, rely=.5)

    def deleteContent():
        scText.config(state="normal")
        scText.delete("1.0", "end")
        scText.config(state="disabled")

    ttk.Button(frame, text="Clear", width=8, command=deleteContent).place(relx=.58, rely=.7)
