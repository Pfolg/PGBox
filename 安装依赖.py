# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   安装依赖 |User    Pfolg
# 2024/11/01 14:12
import os
import sys

p = os.getcwd()
print("当前路径：", p)
os.system(f"cd {p}")
os.chdir(p)
if input("写入镜像源？[Y/N]") == "Y":
    print("写入镜像源……")
    os.system("pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple")
print("更新pip……")
try:
    os.system("python.exe -m pip install --upgrade pip")
except BaseException:
    input("您可能没有合适的环境，执行pip命令出错！")
    sys.exit()

print("开始安装依赖……")
os.system(r"pip install -r .\resource\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple")
input("[回车退出]")
