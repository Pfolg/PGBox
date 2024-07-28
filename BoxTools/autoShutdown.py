# -*- coding: utf-8 -*-
# Project >>> make_pie.py   ||    Environment >>> PyCharm
# FileName >>> auto_shutdown    ||    Author >>> Pfolg
# Date >>> 2024/6/22 and Time >>> 1:05
import os


def show(ti):
    if ti == '':
        input('定时关机已取消\n回车关闭程序:')
    else:
        input(f'已设置，您的系统将在{ti}分钟后自动关闭!\n回车关闭程序:')


try:
    time = int(input('计划在多少分钟后关机(整数) 或者 回车取消定时关机:'))
    basic_time = time * 60
    text = f'shutdown -a\nshutdown -s -t {basic_time}'
except ValueError:
    time = ''
    text = 'shutdown -a'

with open(r".\auto_shutdown.bat", 'w', encoding='utf-8') as file:
    file.write(text)

input('.bat文件已生成，回车执行，现在可关闭程序终止运行')
os.system(r".\auto_shutdown.bat")
os.remove(r".\auto_shutdown.bat")

show(time)
