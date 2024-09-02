# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   questionWifi |User    Pfolg
# 2024/8/24   11:50
import subprocess
import os

output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True)
# 将输出转换为字符串
output_str = output.decode("gbk")
# 分割输出以获取各个WiFi网络的名称
networks = output_str.split('\n')
for i in networks:
    print(i)
name = input("请选择用户配置文件：")


def question(ssid):
    with open(".\\run.bat", "w", encoding="utf-8") as file:
        file.write(f"netsh wlan show profile name=\"{ssid}\" key=clear\npause")
    os.system(".\\run.bat")
    os.remove(".\\run.bat")


question(name)
