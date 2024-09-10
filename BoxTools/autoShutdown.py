# -*- coding: utf-8 -*-
# Project >>> make_pie.py   ||    Environment >>> PyCharm
# FileName >>> auto_shutdown    ||    Author >>> Pfolg
# Date >>> 2024/6/22 and Time >>> 1:05
import os

os.system("shutdown -a")
print("程序开始运行时会取消已设置的定时关机")

try:
    time = int(input('计划在多少分钟后关机(整数) 或者 回车取消定时关机:'))
    basic_time = time * 60
    text = f'shutdown -s -t {basic_time}'
    os.system(text)
    input(f"已设置，您的系统将于{basic_time}秒后关闭\n回车开始：")
except ValueError:
    input("回车退出：")



