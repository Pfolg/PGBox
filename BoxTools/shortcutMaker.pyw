# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   shortcutMaker |User    Pfolg
# 2024/8/23   12:49
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import win32com.client


def find_files(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.set(file_path)
    win.destroy()


def findDirectory(x):
    win = tk.Tk()
    win.withdraw()
    Directory_path = filedialog.askdirectory()
    x.set(Directory_path)
    win.destroy()


WindowStyle = {
    "正常窗口（程序正常运行，窗口可见）": 1,
    "最小化窗口（程序运行，窗口最小化到任务栏）": 3,
    "最大化窗口（程序运行，窗口最大化）": 7
}


# 定义创建的函数
def makeShortcut(pathName, apppath, icoPath, style, arguments, description, workingDirectory):
    try:
        # 创建WScript.Shell对象
        shell = win32com.client.Dispatch("WScript.Shell")

        # 指定快捷方式保存的位置和名称
        shortcut_path = pathName

        # 创建快捷方式
        shortcut = shell.CreateShortcut(shortcut_path)

        # 设置快捷方式的属性
        shortcut.TargetPath = apppath  # 应用程序路径
        shortcut.IconLocation = icoPath  # 图标路径
        shortcut.WindowStyle = style  # 1 表示正常窗口，其他值根据需要设置
        shortcut.Arguments = arguments  # 程序启动参数
        shortcut.Description = description  # 快捷方式描述
        shortcut.WorkingDirectory = workingDirectory  # 工作目录

        # 保存快捷方式
        shortcut.Save()
    except BaseException:
        pass

    if os.path.exists(pathName):
        messagebox.showinfo(title="快捷方式脚本", message="快捷方式创建成功！")
    else:
        messagebox.showerror(title="快捷方式脚本", message="快捷方式创建失败！")


def deleteShortcut(shortcut_path):
    # 删除快捷方式文件
    if os.path.exists(shortcut_path):
        os.remove(shortcut_path)
        print("快捷方式已删除。")
        messagebox.showinfo(title="快捷方式脚本", message="快捷方式已删除！")
    else:
        print("快捷方式不存在。")
        messagebox.showinfo(title="快捷方式脚本", message="快捷方式不存在！")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("快捷方式脚本")
    screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
    w, h = int(screen_w / 2), int(screen_h / 2)
    root.geometry(f'{w}x{h}+{int(screen_w / 4)}+{int(screen_h / 4)}')
    root.resizable(False, False)
    root.iconbitmap(".\\resource\\pg.ico")
    root.attributes('-alpha', 0.9)

    # 创建一个Notebook控件
    notebook = ttk.Notebook(root)

    # 添加两个标签页到Notebook
    tab1 = ttk.Frame(notebook, width=w, height=h)
    tab2 = ttk.Frame(notebook, width=w, height=h)
    tab3 = ttk.Frame(notebook, width=w, height=h)

    # 向标签页添加内容
    ttk.Label(tab1, text="创建&修改快捷方式").place(relx=.8, rely=.02)
    ttk.Label(tab2, text="删除快捷方式").place(relx=.85, rely=.02)
    ttk.Label(tab3, text="帮助").place(relx=.9, rely=.02)

    my_pathName, my_appPath, my_icoPath, my_arguments, my_description, my_workingDirectory, my_style = \
        [tk.StringVar() for _ in range(7)]
    my_styleList = list(WindowStyle.keys())
    my_style.set(my_styleList[0])

    partDict = {
        "指定快捷方式保存的位置和名称": my_pathName,
        "应用程序/文件夹/文件路径": my_appPath,
        "图标路径": my_icoPath,
        "程序运行时窗口状态设定": my_style,
        "程序启动参数": my_arguments,
        "快捷方式描述": my_description,
        "程序工作目录": my_workingDirectory
    }

    for i in range(len(partDict.keys())):
        ttk.Label(tab1, text=list(partDict.keys())[i]).place(relx=.1, rely=.1 + i * .1)
        if i == 3:
            ttk.Combobox(
                tab1, width=28, values=my_styleList, textvariable=list(partDict.values())[i]
            ).place(relx=.35, rely=.1 + i * .1)
        else:
            ttk.Entry(tab1, width=30, textvariable=list(partDict.values())[i]).place(relx=.35, rely=.1 + i * .1)

    ttk.Button(
        tab1, text="选择", width=8, command=lambda: findDirectory(my_pathName)
    ).place(relx=.65, rely=.1 - .005)
    ttk.Button(
        tab1, text="选择文件夹", width=10, command=lambda: findDirectory(my_appPath)
    ).place(relx=.75, rely=.2 - .005)
    ttk.Button(
        tab1, text="选择文件", width=8, command=lambda: find_files(my_appPath)
    ).place(relx=.65, rely=.2 - .005)
    ttk.Button(
        tab1, text="选择", width=8, command=lambda: find_files(my_icoPath)
    ).place(relx=.65, rely=.3 - .005)
    ttk.Button(
        tab1, text="选择", width=8, command=lambda: findDirectory(my_workingDirectory)
    ).place(relx=.65, rely=.7 - .005)

    ttk.Button(
        tab1, text="创建", width=8, command=lambda: makeShortcut(
            my_pathName.get(), my_appPath.get(), my_icoPath.get(), WindowStyle.get(my_style.get()),
            my_arguments.get(), my_description.get(), my_workingDirectory.get())
    ).place(relx=.42, rely=.85)

    deletePath = tk.StringVar()
    ttk.Label(tab2, text="在下方输入文件的路径").place(relx=.1, rely=.02)
    ttk.Entry(tab2, textvariable=deletePath, width=50).place(relx=.1, rely=.12)
    ttk.Button(
        tab2, text="选择", width=8, command=lambda: find_files(deletePath)
    ).place(relx=.7, rely=.12)
    ttk.Button(tab2, text="删除", command=lambda: deleteShortcut(deletePath.get())).place(relx=.1, rely=.22)

    ttk.Label(
        tab3, text=
        "# 创建&修改快捷方式\n"
        "\t[必填] 指定快捷方式保存的位置和名称：选择按钮只能选择文件夹，当文件夹选择后，\n\t请在输入框后加上[\\shortcut_name.lnk]，例：["
        "D:\\PycharmProjects\\pythonProject\\Pz.lnk]"
        "\n\t[必填] 应用程序/文件夹/文件路径：这个输入框有两个选项，请根据自身情况使用"
        "\n\t[非必填] 图标路径：请选择[.ico]文件"
        "\n\t[必填] 程序运行时窗口状态设定：下拉选择，请勿更改选择框中的任何一个字符"
        "\n\t[非必填] 程序启动参数：没有或不懂请不必填"
        "\n\t[非必填] 快捷方式描述"
        "\n\t[非必填] 程序工作目录：指定程序在哪个文件夹内运行"
        "\n# 删除快捷方式\n"
        "\t这里不仅仅可以删快捷方式，还可以删文件，谨慎操作，一旦删除，不可在回收站找回"
        "\n# 总结\n"
        "\t本程序是作者拿来练手的，使用前还是好好读到这儿，不当使用本程序产生的后果由使用者自负。\n\t不如鼠标右键直接创建一个快捷方式来得快。"
        "\n\t如果您想将快捷方式放到[开始]或[启动]之类的文件夹，可能会创建失败，那么请以管理员身份运行程序。"
    ).place(relx=.02, rely=.02)

    # 将标签页添加到Notebook
    notebook.add(tab1, text='创建&修改')
    notebook.add(tab2, text='删除')
    notebook.add(tab3, text="帮助")

    notebook.pack(fill='both', expand=True)

    ttk.Button(root, width=8, text="关闭", command=lambda: root.destroy()).place(relx=.9, rely=.9)

    root.mainloop()
