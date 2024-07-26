# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   FrameSetting |User    Pfolg
# 2024/7/20   12:09
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def find_directory(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askdirectory()
    x.delete(0, 'end')
    x.insert(0, file_path)
    win.destroy()


def find_file(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.delete(0, 'end')
    x.insert(0, file_path)
    win.destroy()


def saveMusicDirectory():
    with open(".\\setting\\Setting-musicPlayer.txt", "w", encoding="utf-8") as g1:
        g1.write(directoryPath.get())


def saveRandomName():
    with open(".\\setting\\Setting-RandomName.txt", "w", encoding="utf-8") as g2:
        g2.write(excelPath.get())


def openAPI():
    if not os.path.isfile(".\\setting\\Setting-APIuse.txt"):  # 判断文件是否存在
        with open(".\\setting\\Setting-APIuse.txt", "w", encoding="utf-8") as f4:
            f4.write("")
    else:
        with open(".\\run.bat", "w", encoding="utf-8") as file:
            file.write(r"start .\setting\Setting-APIuse.txt")
        os.system(".\\run.bat")
        os.remove(".\\run.bat")


def saveThirdPackage():
    with open(".\\setting\\Setting-ThirdPackage.txt", "w", encoding="utf-8") as g3:
        g3.write(TDpath.get())


def saveMail():
    if mailCode.get() and mail.get():
        with open(".\\setting\\Setting-mail.txt", "w", encoding="utf-8") as g5:
            g5.write(str([mail.get(), mailCode.get()]))
    else:
        messagebox.showinfo(title="提示信息", message="未保存邮箱配置!")


def save():
    if not os.path.isdir(".\\setting"):
        os.mkdir(".\\setting")
    saveMusicDirectory()
    saveRandomName()
    saveThirdPackage()
    saveMail()
    messagebox.showinfo(title="提示信息", message="保存成功!\n重启后生效!")


def frameSetting(window):
    # 音乐文件夹设置
    global directoryPath
    directoryPath = tk.StringVar()
    try:
        with open(".\\setting\\Setting-musicPlayer.txt", "r", encoding="utf-8") as f1:
            c1 = f1.readline()
        directoryPath.set(c1)
    except FileNotFoundError:
        pass
    ttk.Label(window, text="设置[音乐播放器]的音乐文件夹").place(relx=.02, rely=.02)
    fp = ttk.Entry(window, textvariable=directoryPath, width=14)
    fp.place(relx=.25, rely=.018)
    ttk.Button(window, text="选择", command=lambda: find_directory(fp)).place(relx=.4, rely=.015)

    # 随机点名文件设置
    global excelPath
    excelPath = tk.StringVar()
    try:
        with open(".\\setting\\Setting-RandomName.txt", "r", encoding="utf-8") as f2:
            c2 = f2.readline()
        excelPath.set(c2)
    except FileNotFoundError:
        pass
    ttk.Label(window, text="设置[随机点名]的默认文件").place(relx=.02, rely=.12)
    ep = ttk.Entry(window, textvariable=excelPath, width=14)
    ep.place(relx=.25, rely=.118)
    ttk.Button(window, text="选择", command=lambda: find_file(ep)).place(relx=.4, rely=.115)

    # 快捷方式
    # C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
    # C:\ProgramData\Microsoft\Windows\Start Menu\Programs
    ttk.Button(window, text="开机自启动，添加到开始菜单，创建桌面快捷方式",
               command=lambda:
               messagebox.showinfo(
                   title="设置指南",
                   message="自己动手，~~~~!"
                           "\n设置开机自启动:将主文件的快捷方式放到[C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup]"
                           "\n添加到开始菜单:主文件的快捷方式放到[C:\ProgramData\Microsoft\Windows\Start Menu\Programs]"
                           "\n创建桌面快捷方式:\n快捷方式放到桌面就可以了")).place(relx=.07, rely=.2)

    global TDpath
    TDpath = tk.StringVar()
    try:
        with open(".\\setting\\Setting-ThirdPackage.txt", "r", encoding="utf-8") as f3:
            c3 = f3.readline()
        TDpath.set(c3)
    except FileNotFoundError:
        pass
    ttk.Label(window, text="设置[Python第三方库工具]导出路径(必须是.txt文件结尾)").place(relx=.02, rely=.32)
    tp = ttk.Entry(window, textvariable=TDpath, width=14)
    tp.place(relx=.05, rely=.418)
    ttk.Button(window, text="选择", command=lambda: find_file(tp)).place(relx=.2, rely=.415)

    # 设置首页美文
    instruction = ("当你自定义了美文，原有的API将不会生效，\n"
                   "你可以定义多个，但要分行列出，\n"
                   "使用此功能可以在一定程度上加速程序打开，\n"
                   "并且会取消首页美文对互联网的依赖，建议使用;\n"
                   "当你清空文件或者移动删除了该文件，API生效。")
    ttk.Button(window, text="自定义首页美文", command=openAPI).place(relx=.06, rely=.52)
    ttk.Button(window, text="该项说明",
               command=lambda: messagebox.showinfo(title="提示信息", message=instruction)).place(relx=.22, rely=.52)

    # 设置邮箱，配置授权码
    global mail, mailCode

    mail, mailCode = tk.StringVar(), tk.StringVar()
    ttk.Label(window, text="配置邮箱").place(relx=.02, rely=.6)
    ttk.Entry(window, width=20, textvariable=mail).place(relx=.1, rely=.6)
    # ttk.Button(window, width=8).place(relx=.28, rely=.598)
    ttk.Label(window, text="配置邮箱授权码").place(relx=.02, rely=.7)
    ttk.Entry(window, width=20, textvariable=mailCode).place(relx=.15, rely=.7)
    try:
        with open(".\\setting\\Setting-mail.txt", "r", encoding="utf-8") as f5:
            c5 = eval(f5.readline())
            mail.set(c5[0])
            mailCode.set(c5[1])
    except BaseException:
        pass

    # 独立按钮
    ttk.Button(window, text="保存", command=save, width=8).place(relx=.8, rely=.9)
