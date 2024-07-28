# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   singleClick |User    Pfolg
# 2024/7/23   14:28
import time
import pyautogui

print("<单击>基于pyautogui实现，鼠标移至左上角停止，按Ctrl+C也可。")
delta = int(input("请输入间隔时间:"))

while True:
    pyautogui.click()
    time.sleep(delta)
