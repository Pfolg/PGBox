# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   recordKeyboard |User    Pfolg
# 2024/8/16   17:38
# 记录的同时并显示
import time
import tkinter as tk
from tkinter import ttk
from pynput import keyboard
from plyer import notification
import threading


def on_press(key):
    try:
        print(f'Alphanumeric key {key.char} pressed')  # 字母按键
        nowKey.set(key.char.upper())
    except AttributeError:
        print(f'Special key {key} pressed')  # 特殊按键按下
        laterKey.set(key)
    clearKeys()


def on_release(key):
    try:
        print(f'Alphanumeric key {key.char} released')  # 字母按键
        nowKey.set(key.char.upper())
    except AttributeError:
        print(f'Special key {key} released')  # 特殊按键按下
        laterKey.set(key)
    clearKeys()


def re_release(key):
    try:
        print(f'Alphanumeric key {key.char} released')  # 字母按键
        nowKey.set(key.char.upper())
    except AttributeError:
        print(f'Special key {key} released')  # 特殊按键按下
        laterKey.set(key)
    with open(".\\resource\\recordKeyboard.txt", "a", encoding="utf-8") as f:
        f.write(key)
    clearKeys()


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
lisNew = keyboard.Listener(on_press=on_press, on_release=re_release)


def changeModel():
    listener.stop()
    lisNew.start()
    notification.notify(
        title='键盘记录',
        message="键盘记录功能已开启，\n请在[.\\resource\\recordKeyboard.txt]查看结果",
        timeout=3,  # 通知显示时间，单位为秒
    )


def clearKeys():
    def clearKey1():
        x = nowKey.get()
        if x:
            time.sleep(5)
            if nowKey.get() == x:
                nowKey.set("")
            else:
                clearKey1()

    def clearKey2():
        y = laterKey.get()
        if y:
            time.sleep(5)
            if laterKey.get() == y:
                laterKey.set("")
            else:
                clearKey2()

    def clearKey3():
        z = lastKey.get()
        if z:
            time.sleep(5)
            if lastKey.get() == z:
                lastKey.set("")
            else:
                clearKey3()

    t1 = threading.Thread(target=clearKey1)
    t2 = threading.Thread(target=clearKey2)
    t3 = threading.Thread(target=clearKey3)
    t1.start()
    t2.start()
    # t3.start()
    t1, t2, t3 = None, None, None


def changColor():
    lo.place(relx=.1, rely=0)
    while True:
        time.sleep(1)
        try:  # 这个bug修了两三次吧
            nowColor = str(lo['foreground'])
            # print(nowColor,type(nowColor))
            if nowColor == "#ffffff":
                lo.configure(foreground='#ff0000')
            else:
                lo.configure(foreground='#ffffff')
        except RuntimeError:
            break


if __name__ == '__main__':
    window = tk.Tk()
    window.title("键盘记录")
    window.config(background="#000000")
    window.overrideredirect(True)
    screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
    w, h = int(screen_w / 6), int(screen_h / 6)
    window.geometry(f'{w}x{h}+{int(screen_w / 1.3)}+{int(screen_h / 12)}')
    window.resizable(False, False)
    window.attributes('-topmost', True)  # 顶置窗口
    window.attributes('-alpha', 0.9)
    window.attributes("-transparent", "#000000")  # 对黑色透明

    tk.Button(
        window, text="X", foreground="#ED1C24", command=lambda: window.destroy(), background="#000000", width=2
    ).place(relx=.9, rely=0)

    tk.Button(
        window, text="记录", command=changeModel, width=5,
        foreground="#ffffff", background="#000000"
    ).place(relx=.8, rely=.8)

    lo = ttk.Label(
        window, text="●", foreground="#ffffff", background="#000000",
        font=("微软雅黑", 16)
    )

    threading.Thread(target=changColor).start()

    nowKey, laterKey, lastKey = tk.StringVar(), tk.StringVar(), tk.StringVar()
    myVars = [nowKey, laterKey, lastKey]
    for i in range(len(myVars)):
        ttk.Label(
            window, textvariable=myVars[i], foreground="#ffffff", background="#000000",
            font=("微软雅黑", 16)
        ).place(relx=.2, rely=.6 - i * .3)

    notification.notify(
        title='键盘记录',
        message="正在运行",
        timeout=3,  # 通知显示时间，单位为秒
    )

    # 监听键盘事件
    listener.start()  # 启动监听器

    # with open("recordKeyboard.txt", "a", encoding="utf-8") as retime:  # 记录启动日志
    #     retime.write(f'{time.strftime("%Y/%m/%d-%H:%M:%S", time.localtime())}\n')
    window.mainloop()
    listener.stop()
    lisNew.stop()
    notification.notify(
        title='键盘记录',
        message="停止运行",
        timeout=3,  # 通知显示时间，单位为秒
    )
