# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   findLocation |User    Pfolg
# 2024/7/26   13:18
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


def findLocation(loc: str):
    if loc:
        cities = {}
        with open(".\\resource\\CN.txt", "r", encoding="utf-8") as file:
            basicData = file.readlines()
            for i in basicData:
                j = i.split("\t")
                cities[j[2]] = {"lon": float(j[-3]), "lat": float(j[-2]), "main": i}

        pos = cities.get(loc)
        if not pos:
            messagebox.showinfo(title="提示信息", message="未查询到该地址的经纬度!\n"
                                                          "请检查输入，或者[.\\resource\\CN.txt]不存在该值。")
            print("未查询到该地址的经纬度")
        else:
            inforLocation.config(state="normal")
            inforLocation.insert(
                "end",
                f"{loc} >>> 经度: {pos.get('lon')}, 纬度: {pos.get('lat')}\n"
                f"{pos.get('main')}"
            )
            inforLocation.config(state="disabled")
            print(pos)


def flFrame(frame):
    ttk.Label(frame, text="中国地理信息查询", font=("微软雅黑", 16)).place(relx=.375, rely=.05)
    location = tk.StringVar()
    ttk.Entry(frame, textvariable=location, width=16).place(relx=.42, rely=.2)
    ttk.Button(
        frame, text="帮助", width=8,
        command=lambda: messagebox.showinfo(title="提示信息", message="输入地名以查询地理信息，示例：\n"
                                                                      "Shuangliu District\n"
                                                                      "Xinjin County\n"
                                                                      "Chengdu\n"
                                                                      "Yan'an\n"
                                                                      "结果示例:"
                                                                      "CN\t100000\tBeijing\tBeijing\t22\tBeijing\t39.9075\t116.3972\t4\n"
                                                                      "数据来源于:https://www.geonames.org/\n"
                                                                      "数据获取日期:2024年7月26日")
    ).place(relx=.9, rely=.8)

    ttk.Button(frame, text="查询", width=8, command=lambda: findLocation(location.get())).place(relx=.45, rely=.3)

    global inforLocation
    inforLocation = ScrolledText(frame, width=40, height=8, state="disabled")
    inforLocation.place(relx=.32, rely=.5)
    ttk.Label(frame, text="查询结果").place(relx=.63, rely=.76)
