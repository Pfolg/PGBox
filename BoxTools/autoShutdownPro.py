# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   autoShutdownPro |User    Pfolg
# 2024/10/09 12:44
import os
import tkinter as tk

"""
shutdown -h 休眠
shutdown -r -t 重启
shutdown -s -t 关机
"""


# print("程序开始运行时会取消已设置的定时关机")
#
# try:
#     time = int(input('计划在多少分钟后关机(整数) 或者 回车取消定时关机:'))
#     basic_time = time * 60
#     text = f'shutdown -s -t {basic_time}'
#     os.system(text)
#     input(f"已设置，您的系统将于{basic_time}秒后关闭\n回车开始：")
# except ValueError:
#     input("回车退出：")

def askConfirm(text):
    root = tk.Tk()
    root.title("确认窗口")
    rw, rh = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{int(rw / 6)}x{int(rh / 6)}+{int(rw / 3)}+{int(rh / 3)}")
    root.resizable(False, False)

    # 借助函数实现命令
    def do(order):
        root.destroy()
        os.system(order)
        # print("执行命令")

    tk.Label(root, text=f"确认您的命令:\n{text}", font=("微软雅黑", 16)).pack()
    # 确认，关闭窗口，立刻执行命令
    tk.Button(root, text="确认", width=8, command=lambda: do(text)).pack()
    # 取消 关闭窗口，什么也不做
    tk.Button(root, text="取消", width=8, command=lambda: root.destroy()).pack()
    root.mainloop()


# 执行定时关机
def autoShutdown(time):
    if time:
        os.system(f"shutdown -s -t {time}")
    else:
        askConfirm(f"shutdown -s -t {time}")


# 执行定时重启
def autoRestart(time):
    if time:
        os.system(f"shutdown -r -t {time}")
    else:
        askConfirm(f"shutdown -r -t {time}")


if __name__ == '__main__':
    os.system("shutdown -a")
    # 窗口设置
    window = tk.Tk()
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry(f"{int(w / 4)}x{int(h / 4)}+{int(w / 4)}+{int(h / 4)}")
    window.title("Auto_Shutdown_Pro")
    # 标签
    tk.Label(window, text="Time Setting", font=("微软雅黑 bold", 16)).place(relx=.02, rely=.02)

    # 控件设置
    day, hour, minute, second = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()
    # day
    tk.Entry(window, width=8, textvariable=day).place(relx=.25, rely=.25)
    tk.Label(window, text="Day：").place(relx=.1, rely=.25)
    # hour
    tk.Entry(window, width=8, textvariable=hour).place(relx=.25, rely=.4)
    tk.Label(window, text="Hour：").place(relx=.1, rely=.4)
    # minute
    tk.Entry(window, width=8, textvariable=minute).place(relx=.25, rely=.55)
    tk.Label(window, text="Min：").place(relx=.1, rely=.55)
    # second
    tk.Entry(window, width=8, textvariable=second).place(relx=.25, rely=.7)
    tk.Label(window, text="Second：").place(relx=.1, rely=.7)

    # 标签及按钮
    tk.Label(window, text="shutdown -a\nshutdown -r -t 60\nshutdown -s -t 60\nIt will run \ncommand one at first.").place(relx=.6, rely=.1)
    tk.Button(
        window, text="定时关机", width=8, command=lambda: autoShutdown(
            (
                    (
                            int(day.get()) * 24 + int(hour.get())
                    ) * 60 + int(minute.get())
            ) * 60 + int(second.get())
        )
    ).place(relx=.55, rely=.7)
    tk.Button(
        window, text="定时重启", width=8, command=lambda: autoRestart(
            (
                    (
                            int(day.get()) * 24 + int(hour.get())
                    ) * 60 + int(minute.get())
            ) * 60 + int(second.get())
        )
    ).place(relx=.55, rely=.5)
    tk.Button(window, text="立即休眠", width=8, command=lambda: askConfirm("shutdown -h")).place(relx=.75, rely=.5)
    tk.Button(window, text="取消设置", width=8, command=lambda: os.system("shutdown -a")).place(relx=.75, rely=.7)

    window.mainloop()
