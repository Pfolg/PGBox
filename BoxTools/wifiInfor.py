# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   name |User    Pfolg
# 2024/7/31   17:02
# 这个程序会报很多错，过很正常，注释掉最后一行就好了
import os
import subprocess
import threading
import time
from tkinter import ttk
from tkinter import messagebox
import random


def getInfor():
    # 执行命令获取当前连接的WiFi名称
    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 检查命令是否执行成功
    if result.returncode == 0:
        # 将命令输出转换为字符串
        output = result.stdout.decode("gbk")  # 我的系统编码是gbk
        # print(output)
        # 分割输出的每一行
        lines = output.split('\n')

        # 遍历每一行，寻找包含"SSID"的行
        for line in lines:
            if "SSID" in line:
                # 提取WiFi名称
                ssid = line.split(":")[1].strip()
                # print(f"当前连接的WiFi名称是: {ssid}")
                with open(".\\run.bat", "w", encoding="utf-8") as file:
                    file.write(f"netsh wlan show profile name=\"{ssid}\" key=clear\npause")
                os.system(".\\run.bat")
                os.remove(".\\run.bat")
    else:
        messagebox.showerror(title="提示信息", message="获取失败")


def wifiFrame(frame):
    ttk.Label(frame, text="获取WiFi信息").place(relx=.02, rely=.02)
    ttk.Button(
        frame, text="暴力破解", width=8, command=lambda: messagebox.showinfo(
            title="提示信息", message=
            "省省吧，这玩意费时费力，\n"
            "作者的电脑差点没了，\n"
            "你自己搞搞没问题，我搞了放在这可是要进局子的。\n"
            "顺便说一句，我失败了的哦。")
    ).place(relx=.46, rely=.3)

    ttk.Button(
        frame, text="获取当前WiFi信息", command=lambda: threading.Thread(target=getInfor).start()
    ).place(relx=.445, rely=.4)

    ttk.Button(
        frame, text="获取其他WiFi信息", command=lambda: os.system("start .\\BoxTools\\questionWifi.py")
    ).place(relx=.445, rely=.5)

    ttk.Button(
        frame,
        command=lambda: messagebox.showinfo(
            title="提示信息", message=
            "如何关闭这些弹幕：\n"
            "在[BoxTools]文件夹里找到[wifiInfor.py]文件，\n"
            "然后注释掉最后一行代码。"),
        width=8, text="帮助",)
    # ).place(relx=.8, rely=.9)

    keyDict = {"富强": [.08, .3], "民主": [.08, .45], "文明": [.08, .6], "和谐": [.08, .75], "爱国": [.18, .15],
               "敬业": [.38, .15], "诚信": [.58, .15], "友善": [.78, .15], "自由": [.88, .3], "平等": [.88, .45],
               "公正": [.88, .6], "法治": [.88, .75]}
    keyList = list(keyDict.keys())
    labelList = []
    for i in range(len(keyList)):
        labelList.append(ttk.Label(frame, text=keyList[i], font=("微软雅黑", 14), width=8))

    def forgetAll():
        for j in labelList:
            j.place_forget()

    def showLabel():
        while True:
            forgetAll()
            random.shuffle(labelList)
            for k in range(len(labelList)):
                forgetAll()
                lKey = labelList[k]["text"]
                x, y = keyDict.get(lKey)[0], keyDict.get(lKey)[1]
                labelList[k].place(relx=x, rely=y)
                time.sleep(1)
            for _ in range(3):
                forgetAll()
                time.sleep(1)
                for m in range(len(labelList)):
                    lKey = labelList[m]["text"]
                    x, y = keyDict.get(lKey)[0], keyDict.get(lKey)[1]
                    labelList[m].place(relx=x, rely=y)

                time.sleep(2)

    # 想要关闭正能量弹窗，请注释掉下面这行代码
    # threading.Thread(target=showLabel).start()
