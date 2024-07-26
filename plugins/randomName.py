import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import random

information = ("您的名单最好为.xlsx格式;\n"
               "您的名单应位于文件的Sheet1内;\n"
               "名字只能位于“姓名”之下的单元格;\n"
               "本程序基于Python-tkinter&pandas&random实现。")


def find_files(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.delete(0, 'end')
    x.insert(0, file_path)
    win.destroy()


def gainData(path):
    if path:
        book = pd.read_excel(path, index_col=None, header=None)
        work = book.to_numpy()
        for i in range(len(work)):
            for j in range(len(work[0])):
                if work[i][j] == "姓名":
                    startRow, startColumn = i, j
        nameList = work[startRow + 1:, startColumn]
        return nameList
    else:
        messagebox.showerror(title="Error", message="请选择文件!")


def showName():
    nl = gainData(filePath.get())
    name = nl[random.randint(0, len(nl) - 1)]
    return name


def window(text):
    w = tk.Tk()
    w.overrideredirect(1)
    screen_w, screen_h = w.winfo_screenwidth(), w.winfo_screenheight()
    ww, wh = int(screen_w / 5), int(screen_h / 5)
    w.geometry(f'{ww}x{wh}+{int(screen_w / 3)}+{int(screen_h / 3)}')
    w.resizable(False, False)
    w.config(background="#66bdff")

    ttk.Label(w, text="恭喜:", font=("微软雅黑", 20), background="#66bdff",
              foreground="#FFFFFF").place(relx=.1, rely=.1)
    ttk.Label(w, text=text + " 同学", font=("微软雅黑", 30), compound="center",
              foreground="#FFFFFF", background="#66bdff").place(relx=.3, rely=.2)
    ttk.Button(w, text="确定", command=lambda: w.destroy(), width=8).place(relx=.4, rely=.7)

    w.mainloop()


def randomName(frame):
    ttk.Label(frame, text="随机点名").place(relx=.03, rely=0)

    global filePath
    filePath = tk.StringVar()
    try:
        with open(".\\setting\\Setting-RandomName.txt", "r", encoding="utf-8") as f2:
            c2 = f2.readline()
        filePath.set(c2)
    except FileNotFoundError:
        pass
    ttk.Label(frame, text="请选择表格文件", font=("微软雅黑", 20)).place(relx=.35, rely=.2)
    file = ttk.Entry(frame, textvariable=filePath, width=40)
    file.place(relx=.3, rely=.4)
    ttk.Button(frame, text="选择", command=lambda: find_files(file)).place(relx=.6, rely=.398)
    ttk.Button(frame, text="开始", command=lambda: window(showName())).place(relx=.43, rely=.6)

    ttk.Button(frame, text="帮助", command=lambda: messagebox.showinfo(title="帮助", message=information),
               width=8).place(relx=.8, rely=.9)

    ttk.Label(frame, text="你不能怪作者，作者也是被**毒害了的人，肯定要回馈一下**啊(手动狗头)",
              font=("Segoe UI", 8)).place(relx=.03, rely=.95)
