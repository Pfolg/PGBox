# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   runwin |User    Pfolg
# 2024/10/31 22:17
import os
import time
import pyautogui
import pyperclip
from win10toast import ToastNotifier

# 创建一个通知对象
toaster = ToastNotifier()

os.system("start powershell")
time.sleep(3)
pyperclip.copy("irm https://get.activated.win | iex")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
toaster.show_toast(
    title="激活脚本",
    msg="请在新页面按 1 激活Windows",
    threaded=True,
    duration=30,
)
