# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   FrameSetting |User    Pfolg
# 2024/7/20   12:09
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os


def find_directory(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askdirectory()
    if file_path:
        x.set(file_path)
    win.destroy()


def find_file(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        x.set(file_path)
    win.destroy()


def openAPI():
    if not os.path.isfile(".\\setting\\Setting-APIuse.txt"):
        with open(".\\setting\\Setting-APIuse.txt", "w", encoding="utf-8") as g4:
            g4.write("")
            messagebox.showinfo("Information", "Can't find the file and create one.")
    os.system(r"start .\setting\Setting-APIuse.txt")


def save():
    tkcbx.config(state="normal")
    # if not os.path.exists(".\\setting\\Config.json"):
    #     if not os.path.exists(".\\setting"):
    #         os.mkdir(".\\setting")
    #     with open(".\\setting\\Config.json", "w", encoding="utf-8") as startFile:
    #         json.dump({}, startFile, ensure_ascii=False, indent=4)
    with open(".\\setting\\Config.json", "r", encoding="utf-8") as originFile:
        originDict = json.load(originFile)
    # if not os.path.isdir(".\\setting"):
    #     os.mkdir(".\\setting")
    SettingInfor = {
        "musicPlayerDirectory": directoryPath.get(),
        "RandomNameDirectory": excelPath.get(),
        "ThirdPackageOutputFile": TDpath.get(),
        "mail": mail.get(),
        "mailCode": mailCode.get(),
        "city": city.get(),
        "openweatherAPI": opwAPI.get(),
        "browser": browser.get(),
        "XHide": XHide.get(),
        "nircmd_path": nircmd_path.get(),
    }
    for i in SettingInfor:
        originDict[i] = SettingInfor.get(i)
    tkcbx.config(state="readonly")
    with open(".\\setting\\Config.json", "w", encoding="utf-8") as file:
        json.dump(originDict, file, ensure_ascii=False, indent=4)

    messagebox.showinfo(title="提示信息", message="保存成功!\n重启后生效!")


def openConfig(e):
    os.system("start .\\setting\\Config.json")


def frameSetting(window):
    # 设置默认字体
    # defaultFont = "Segoe UI"

    global directoryPath, excelPath, TDpath, mail, mailCode, city, opwAPI, browser, tkcbx, XHide, nircmd_path
    (
        directoryPath, excelPath, TDpath, mail, mailCode, city, opwAPI, browser, XHide, nircmd_path
    ) = \
        (
            tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(),
            tk.StringVar(), tk.StringVar(), tk.BooleanVar(), tk.StringVar()
        )

    # 音乐文件夹设置
    ttk.Label(window, text="设置[音乐播放器]的音乐文件夹").place(relx=.02, rely=.02)
    ttk.Entry(window, textvariable=directoryPath, width=14).place(relx=.25, rely=.018)
    ttk.Button(window, text="选择", command=lambda: find_directory(directoryPath)).place(relx=.4, rely=.015)

    # 随机点名文件设置
    ttk.Label(window, text="设置[随机点名]的默认文件").place(relx=.02, rely=.12)
    ttk.Entry(window, textvariable=excelPath, width=14).place(relx=.25, rely=.118)
    ttk.Button(window, text="选择", command=lambda: find_file(excelPath)).place(relx=.4, rely=.115)

    # 快捷方式
    # C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
    # C:\ProgramData\Microsoft\Windows\Start Menu\Programs
    ttk.Button(
        window, text="开机自启动，添加到开始菜单，创建桌面快捷方式",
        command=lambda:
        messagebox.showinfo(
            title="设置指南",
            message="自己动手，~~~~!"
                    "\n设置开机自启动:将主文件的快捷方式放到[C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup]"
                    "\n添加到开始菜单:主文件的快捷方式放到[C:\ProgramData\Microsoft\Windows\Start Menu\Programs]"
                    "\n创建桌面快捷方式:\n快捷方式放到桌面就可以了")
    ).place(relx=.07, rely=.2)

    ttk.Label(window, text="设置[Python第三方库工具]导出路径(必须是.txt文件结尾)").place(relx=.02, rely=.32)
    ttk.Entry(window, textvariable=TDpath, width=14).place(relx=.05, rely=.418)
    ttk.Button(window, text="选择", command=lambda: find_file(TDpath)).place(relx=.2, rely=.415)

    # 设置首页美文
    instruction = (
        "当你自定义了美文，原有的API(30s获取一次)将不会生效，\n"
        "你可以定义多个，但要分行列出，\n"
        "使用此功能可以在一定程度上加速程序打开，\n"
        "并且会取消首页美文对互联网的依赖，建议使用;\n"
        "当你清空文件或者移动删除了该文件，API生效。")
    ttk.Button(window, text="自定义首页美文", command=openAPI).place(relx=.06, rely=.52)
    ttk.Button(
        window, text="该项说明",
        command=lambda: messagebox.showinfo(title="提示信息", message=instruction)
    ).place(relx=.22, rely=.52)

    # 设置邮箱，配置授权码
    ttk.Label(window, text="配置邮箱").place(relx=.02, rely=.6)
    ttk.Entry(window, width=20, textvariable=mail).place(relx=.1, rely=.6)
    # ttk.Button(window, width=8).place(relx=.28, rely=.598)
    ttk.Label(window, text="配置邮箱授权码").place(relx=.02, rely=.7)
    ttk.Entry(window, width=20, textvariable=mailCode).place(relx=.15, rely=.7)

    # 天气设置
    ttk.Label(window, text="城市(市的拼音)").place(relx=.02, rely=.8)
    ttk.Entry(window, width=20, textvariable=city).place(relx=.15, rely=.8)
    ttk.Label(window, text="openWeather API").place(relx=.02, rely=.9)
    ttk.Entry(window, width=20, textvariable=opwAPI).place(relx=.2, rely=.9)

    # 设置主页浏览器
    browsers = [
        'google', 'bing', 'duckduckgo', 'baidu', 'yahoo', 'yandex', 'blekko', 'ecosia', 'lycos', 'searx',
        'swisscows', 'sogou', 'bing_china'
    ]
    ttk.Label(window, text="搜索引擎").place(relx=.6, rely=.1)
    browser.set("bing")
    tkcbx = ttk.Combobox(window, values=browsers, textvariable=browser, state="readonly", width=10)
    tkcbx.place(relx=.7, rely=.1)

    # 点X直接退出的设置
    ttk.Checkbutton(window, variable=XHide, text="点击X最小化窗口").place(relx=.6, rely=.2)

    # NirCmd路径设置
    ttk.Entry(window, textvariable=nircmd_path).place(relx=.6, rely=.4)
    ttk.Label(window, text="NirCmd路径设置").place(relx=.6, rely=.3)
    ttk.Button(window, text="选择", command=lambda: find_file(nircmd_path)).place(relx=.8, rely=.4)

    try:
        with open(".\\setting\\Config.json", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            directoryPath.set(myDict.get("musicPlayerDirectory"))
            excelPath.set(myDict.get("RandomNameDirectory"))
            TDpath.set(myDict.get("ThirdPackageOutputFile"))
            mail.set(myDict.get("mail"))
            mailCode.set(myDict.get("mailCode"))
            city.set(myDict.get("city"))
            opwAPI.set(myDict.get("openweatherAPI"))
            browser.set(myDict.get("browser"))
            XHide.set(myDict.get("XHide"))
            nircmd_path.set(myDict.get("nircmd_path"))
    except BaseException:
        pass

    tk.Button(window, text="SAVE", command=save, width=8, background="red").place(relx=.9, rely=.02)
    bottomLabel = ttk.Label(window, text="Open the config file", foreground="blue", cursor="hand2")
    bottomLabel.place(relx=.7, rely=.02)
    bottomLabel.bind("<Button-1>", openConfig)
