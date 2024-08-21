# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   autoSend |User    Pfolg
# 2024/8/15   11:36
# 发送的内容：单个消息，多条在文件中的内容，随机消息
# 轰炸某社交软件——q | wx，它们都可以用Alt+S发送消息
# 但是随机消息要怎么实现你呢？其实没有意义吧，轰炸了已经，那就改一下列表吧
import sys
import time
from pynput import keyboard
import pyautogui
import os
import pyperclip
import random

position = ""


def on_pressF8(key):
    global position
    if key == keyboard.Key.f8:
        position = pyautogui.position()
        return False


def sendMessage(p, m, t):
    pyperclip.copy(m)  # 复制
    pyautogui.click(p)
    pyautogui.hotkey("ctrl", "v")  # 粘贴
    pyautogui.hotkey("alt", "s")  # 发送 快捷键
    time.sleep(t)


print("你可以根据自己使用的聊天软件的发送快捷键来更改程序中的快捷键\n获取聊天框位置，请将鼠标至于聊天框中部，然后按下F8键")
# 监听键盘事件
with keyboard.Listener(on_press=on_pressF8) as listener:
    listener.join()

if position:
    print("position:", *position)
    pyautogui.click(position)
else:
    input("未获取到鼠标位置")
    sys.exit()

content = input("请输入文件路径（格式化后的.txt文档），也可以直接输入要发送的单条内容：")
deltaTime = float(input("请输入发送间隔时间："))
num = int(input("要发送多少条（>=1）："))

is_file = os.path.isfile(content)
print('\033[31m' + '强制退出请将鼠标迅速往左上角拖\n或者焦点在命令行界面时按下Ctrl+C' + '\033[0m')

if is_file:
    print("file")
    try:
        with open(content, "r", encoding="utf-8") as file:
            c = file.readlines()
            contentList = [s.rstrip() for s in c]
    except FileNotFoundError:
        input("找不到文件")
        sys.exit()
    i = 0
    while True:
        # 打乱列表顺序
        random.shuffle(contentList)
        for item in contentList:
            i += 1
            sendMessage(position, item, deltaTime)
            print(f"第{i}条已发送")
            if i == num:
                break
        if i >= num:
            break
else:
    print("单条消息")
    for i in range(num):
        sendMessage(position, content, deltaTime)
        print(f"第{i + 1}条已发送")

input("程序执行完毕，回车退出……")
