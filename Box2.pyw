# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   Box2 |User    Pfolg
# 2024/8/1   10:02
# 此代码仅做过往尝试的参考，不再更新
import hashlib
import json
import os
import random
import re
import subprocess
import sys
import threading
import time
import turtle
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pyautogui
import pygame
import pyperclip
import requests
import win32com.client
import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from tkinter.scrolledtext import ScrolledText
from blind_watermark import WaterMark
from translate import Translator
import pdfplumber
import pyecharts.options as opts
from pyecharts.charts import WordCloud
import jieba
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggopus import OggOpus
from mutagen.oggvorbis import OggVorbis
import qrcode as cd
from PIL import Image
import pandas as pd


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
        frame, text="暴力破解", width=8, command=lambda: messagebox.showinfo(title="提示信息", message="省省吧，这玩意费时费力，\n"
                                                                                                       "作者的电脑差点没了，\n"
                                                                                                       "你自己搞搞没问题，我搞了放在这可是要进局子的。\n"
                                                                                                       "顺便说一句，我失败了的哦。")
    ).place(relx=.46, rely=.3)

    ttk.Button(
        frame, text="获取WiFi信息", command=lambda: threading.Thread(target=getInfor).start()
    ).place(relx=.445, rely=.4)

    ttk.Button(frame,
               command=lambda: messagebox.showinfo(title="提示信息", message="如何关闭这些弹窗：\n"
                                                                             "在[BoxTools]文件夹里找到[wifiInfor.py]文件，\n"
                                                                             "然后注释掉最后一行代码。"),
               width=8, text="帮助",
               ).place(relx=.8, rely=.9)

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
    threading.Thread(target=showLabel).start()


listCommand = [
    "pip config unset global.index-url",
    "pip config set global.index-url ",
    "pip freeze > "
]

dictUrl = {
    "阿里镜像": "https://mirrors.aliyun.com/pypi/simple/",
    "百度镜像": "https://mirror.baidu.com/pypi/simple/",
    "清华镜像(推荐)": "https://pypi.tuna.tsinghua.edu.cn/simple/",
    "中科大镜像": "https://pypi.mirrors.ustc.edu.cn/simple/",
    "豆瓣镜像": "http://pypi.douban.com/simple/",
    "搜狐镜像": "http://mirrors.sohu.com/Python/",
    "华中科大镜像": "https://pypi.hustunique.com/",
    "山东理工大学镜像": "https://pypi.hustunique.com/"
}

listUrl = [*dictUrl.keys()]


def osRun():
    os.system(".\\run.bat")
    time.sleep(0.5)
    os.remove(".\\run.bat")


def process(vl: int):
    try:
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            path = myDict.get("ThirdPackageOutputFile")
    except BaseException:
        pass
    if vl == 4:
        text = listCommand[0]
    elif vl == 3:
        if tpc1.get():
            text = listCommand[1] + dictUrl.get(tpc1.get())
        else:
            messagebox.showerror(title="Error", message="请选择镜像源!")
            return False
    elif vl == 6:
        if path:
            text = listCommand[2] + f"{path}"
            messagebox.showinfo(title="提示信息", message=f"将导出至[{path}]")
        else:
            messagebox.showerror(title="Error", message="请设置导出文件夹!")
            return False
    elif vl == 1:
        if packageName.get():
            text = f"pip install {packageName.get()}"
        else:
            messagebox.showerror(title="Error", message="请输入包名!")
            return False
    elif vl == 2:
        if packageName.get():
            text = f"pip uninstall {packageName.get()}"
        else:
            messagebox.showerror(title="Error", message="请输入包名!")
            return False
    elif vl == 5:
        if packageName.get() and tpc1.get():
            text = f"pip install {packageName.get()} -i {dictUrl.get(tpc1.get())}"
        else:
            messagebox.showerror(title="Error", message="请输入包名!\n或者\n请选择镜像源!")
            return False
    elif vl == 7:
        text = "pip install pip-review\npip-review --interactive"
    elif vl == 8:
        text = "pip install pip-review\npip-review --a"
    else:
        return False

    with open(".\\run.bat", "w", encoding="utf-8") as file:
        file.write(text + "\npause")
    x = threading.Thread(target=osRun)
    x.start()
    x = None


def ThirdPackage(frame):
    ttk.Label(frame, text="专为Python懒人打造的交互版pip程序(大概吧)").place(relx=.32, rely=.005)
    flag = tk.IntVar()
    tpr0 = ttk.Button(frame, text="安装包", width=18, command=lambda: nextStep(1))
    tpr1 = ttk.Button(frame, text="卸载包", width=18, command=lambda: nextStep(2))
    tpr2 = ttk.Button(frame, text="添加镜像源", width=18, command=lambda: nextStep(3))
    tpr3 = ttk.Button(frame, text="移除镜像源", width=18, command=lambda: nextStep(4))
    tpr4 = ttk.Button(frame, text="使用镜像源安装某包", width=18, command=lambda: nextStep(5))
    tpr5 = ttk.Button(frame, text="导出已安装包信息", width=18, command=lambda: nextStep(6))
    tpr6 = ttk.Button(frame, text="升级包(不推荐)", width=18, command=lambda: nextStep(7))
    tpr7 = ttk.Button(frame, text="自动升级包(极不推荐)", width=18, command=lambda: nextStep(8))

    listRadiobutton = [tpr0, tpr1, tpr2, tpr3, tpr4, tpr5, tpr6, tpr7]
    for i in range(len(listRadiobutton)):
        listRadiobutton[i].place(relx=.02, rely=(i + 1) / 10)

    global packageName, tpc1
    packageName = tk.StringVar()
    tpl1 = ttk.Label(frame, text="输入包名:")
    tpe1 = ttk.Entry(frame, width=12, textvariable=packageName)
    tpb1 = ttk.Button(frame, width=8, text="确定", command=lambda: process(value))
    tpb2 = ttk.Button(frame, width=16, text="移除镜像源", command=lambda: process(4))
    tpc1 = ttk.Combobox(frame, width=16, values=listUrl)
    tpb3 = ttk.Button(frame, text="添加镜像源", width=16, command=lambda: process(3))
    tpb4 = ttk.Button(frame, text="导出已安装包信息", width=16, command=lambda: process(6))
    tpb5 = ttk.Button(frame, text="升级包", width=16, command=lambda: process(7))
    tpb6 = ttk.Button(frame, text="自动升级包", width=16, command=lambda: process(8))

    def package3_forgetAll():
        for bt in [tpl1, tpe1, tpb1, tpb2, tpb3, tpc1, tpb4, tpb5, tpb6]:
            bt.place_forget()

    def nextStep(x):
        global value
        value = x
        if value == 1 or value == 2:
            package3_forgetAll()
            tpl1.place(relx=.22, rely=.1)
            tpe1.place(relx=.22, rely=.2)
            tpb1.place(relx=.4, rely=.2)
        elif value == 3:
            package3_forgetAll()
            tpc1.place(relx=.22, rely=.3)
            tpb3.place(relx=.42, rely=.3)
        elif value == 4:
            package3_forgetAll()
            tpb2.place(relx=.22, rely=.4)
        elif value == 5:
            package3_forgetAll()
            tpl1.place(relx=.22, rely=.1)
            tpe1.place(relx=.22, rely=.2)
            tpb1.place(relx=.4, rely=.2)
            tpc1.place(relx=.22, rely=.3)
        elif value == 6:
            package3_forgetAll()
            tpb4.place(relx=.22, rely=.6)
        elif value == 7:
            package3_forgetAll()
            tpb5.place(relx=.22, rely=.7)
        elif value == 8:
            package3_forgetAll()
            tpb6.place(relx=.22, rely=.8)
        else:
            package3_forgetAll()

    msg = ("注意事项:\n"
           "0、没有Python解释器的请勿使用!\n"
           "1、安装和卸载包都必须填入包名;\n"
           "2、添加镜像源可以选择一个添加;\n"
           "3、移除镜像源是一次性全部移除;\n"
           "4、使用镜像源安装某包需要包名和镜像源;\n"
           "5、导出已安装包信息需要提前设置路径;\n"
           "6、两种升级包程序都是基于pip-review使用的,\n"
           "    程序会自动安装这个库,\n"
           "    没有Python环境就无法使用;\n"
           "7、本插件基于os库实现,会有一个命令行窗口;\n"
           "8、同时空条件下一次只能安装或卸载一个包,\n"
           "    否则会导致pip的异常。")

    ttk.Button(frame, text="注意事项", width=8,
               command=lambda: messagebox.showinfo(title="注意事项", message=msg)).place(relx=.9, rely=.8)


def writeClick():
    x = targetFile.get()
    with open(".\\run.bat", "w", encoding="utf-8") as file:
        file.write(f"start .\\BoxTools\\{x}\npause")


def runClick():
    x = targetFile.get()
    os.system(f".\\BoxTools\\{x}")
    time.sleep(.5)


def myClickRun():
    x = threading.Thread(target=runClick)
    x.start()
    x = None


"singleClick.py"
"doubleClick.py"


def singleDouble(frame):
    global targetFile
    targetFile = tk.StringVar()
    ttk.Radiobutton(
        frame, text="自动单击", value="singleClick.py", variable=targetFile, width=10
    ).place(relx=.02, rely=.1)
    ttk.Radiobutton(
        frame, text="自动双击", value="doubleClick.py", variable=targetFile, width=10
    ).place(relx=.22, rely=.1)
    ttk.Button(frame, text="启动", command=myClickRun).place(relx=.12, rely=.2)
    # ttk.Label(frame, text="请输入点击间隔").place(relx=.02, rely=.1)
    # ttk.Entry(frame, width=8, textvariable=delta).place(relx=.22, rely=.1)
    ttk.Button(frame, width=8, text="帮助",
               command=lambda: messagebox.showinfo(title="提示信息",
                                                   message="此程序有一个极大的bug没修，暂无法使用!\n"
                                                           "基于pyautogui实现，鼠标移至左上角停止。\n"
                                                           "由于石粒有限，主程序关闭后子程序仍然会运行，\n"
                                                           "使用时请注意。"
                                                   )
               ).place(relx=.9, rely=.8)


def readLICENSE(frame):
    ttk.Label(frame, text=("By continuing to use this software, you agree to this LCENSE\n"
                           "继续使用本软件，即表示您同意本LCENSE"), font=("微软雅黑 bold", 12)
              ).place(relx=.1, rely=.02)
    LicScroText = ScrolledText(frame, width=80, height=20)
    LicScroText.place(relx=.1, rely=.18)

    try:
        with open(".\\LICENSE.txt", "r", encoding="utf-8") as fg:
            c = fg.readlines()
        for i in c:
            LicScroText.insert("end", i)
    except FileNotFoundError:
        pass
    finally:
        LicScroText["state"] = "disabled"


randomName_information = ("您的名单最好为.xlsx格式;\n"
                          "您的名单应位于文件的Sheet1内;\n"
                          "名字只能位于“姓名”之下的单元格;\n"
                          "本程序基于Python-tkinter&pandas&random实现。")


def find_files(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.delete(0, 'end')
    x.insert(0, file_path)
    win.destroy()


def gainData(path):
    if path:
        book = pd.read_excel(path, index_col=None, header=None)
        work = book.to_numpy()
        for i in range(len(work)):
            for j in range(len(work[0])):
                if work[i][j] == "姓名":
                    startRow, startColumn = i, j
        nameList = work[startRow + 1:, startColumn]
        return nameList
    else:
        messagebox.showerror(title="Error", message="请选择文件!")


def showName():
    nl = gainData(filePath.get())
    name = nl[random.randint(0, len(nl) - 1)]
    return name


def new_window(text):
    w = tk.Tk()
    w.overrideredirect(1)
    screen_w, screen_h = w.winfo_screenwidth(), w.winfo_screenheight()
    ww, wh = int(screen_w / 5), int(screen_h / 5)
    w.geometry(f'{ww}x{wh}+{int(screen_w / 3)}+{int(screen_h / 3)}')
    w.resizable(False, False)
    w.config(background="#66bdff")

    ttk.Label(w, text="恭喜:", font=("微软雅黑", 20), background="#66bdff",
              foreground="#FFFFFF").place(relx=.1, rely=.1)
    ttk.Label(w, text=text + " 同学", font=("微软雅黑", 30), compound="center",
              foreground="#FFFFFF", background="#66bdff").place(relx=.3, rely=.2)
    ttk.Button(w, text="确定", command=lambda: w.destroy(), width=8).place(relx=.4, rely=.7)

    w.mainloop()


def randomName(frame):
    ttk.Label(frame, text="随机点名").place(relx=.03, rely=0)

    global filePath
    filePath = tk.StringVar()
    try:
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            filePath.set(myDict.get("RandomNameDirectory"))
    except BaseException:
        pass
    ttk.Label(frame, text="请选择表格文件", font=("微软雅黑", 20)).place(relx=.35, rely=.2)
    file = ttk.Entry(frame, textvariable=filePath, width=40)
    file.place(relx=.3, rely=.4)
    ttk.Button(frame, text="选择", command=lambda: find_files(file)).place(relx=.6, rely=.398)
    ttk.Button(frame, text="开始", command=lambda: new_window(showName())).place(relx=.43, rely=.6)

    ttk.Button(frame, text="帮助", command=lambda: messagebox.showinfo(title="帮助", message=randomName_information),
               width=8).place(relx=.8, rely=.9)

    ttk.Label(frame, text="你不能怪作者，作者也是被**毒害了的人，肯定要回馈一下**啊(手动狗头)",
              font=("Segoe UI", 8)).place(relx=.03, rely=.95)


def QRCodeMaker(frame):
    # 生成二维码
    def main_pro(txt, l2, l1, gl):
        try:
            code = cd.QRCode(
                version=1,
                error_correction=cd.constants.ERROR_CORRECT_H,  # 容错率为高
                box_size=10,
                border=4,
            )
        except UnicodeEncodeError:
            messagebox.showwarning(title='UnicodeEncodeError',
                                   message=f'UnicodeEncodeError: '
                                           f'\n\'latin-1\' codec can\'t encode characters in position 0-{len(txt)}'
                                           f'\nClick \"确定\" and QUIT')
            sys.exit()
        try:
            code.add_data(txt)
            code.make(fit=True)
            code_img = code.make_image(fill_color=l2, back_color=l1)
        except ValueError:
            messagebox.showwarning(title='ValueError',
                                   message=f'ValueError: \n'
                                           f'unknown color specifier: {l2} or {l1}\n'
                                           f'Click \"确定\" and QUIT')
            sys.exit()
        # show()
        code_size_w, code_size_h = code_img.size
        ratio = 6
        if gl == '':
            pass
        else:  # 粘贴图片
            logo = Image.open(gl)
            logo_w, logo_h = int(code_size_w / ratio), int(code_size_h / ratio)
            icon = logo.resize((logo_w, logo_h), 5)  # Use Image.Resampling.NEAREST (0), Image.Resampling.LANCZOS (1),
            # Image.Resampling.BILINEAR (2), Image.Resampling.BICUBIC (3), Image.Resampling.BOX (4) or
            # Image.Resampling.HAMMING (5)
            x, y = int((code_size_w - logo_w) / 2), int((code_size_h - logo_h) / 2)
            code_img.paste(icon, (x, y))
        time.sleep(2)
        # code_img.show()
        messagebox.showinfo(message='二维码已生成，请在程序所在目录查找\n\"code.png\"', title='提示信息')
        with open('.\\code.png', 'wb') as file:
            code_img.save(file)
        print('Done')

    def part1():
        print('Loading......')
        a, b, c, d = url.get(), choose_color2.get(), choose_color1.get(), get_logo.get()
        main_pro(a, b, c, d)

    def part0():
        main_label = ttk.Label(frame, text='QR-Code Maker',
                               font=(r'C:\Windows\Fonts\msyh.ttc', 20),
                               compound='center')
        main_label.place(relx=0.5, rely=0.05, anchor='center')

    def find_picture():
        win = tk.Tk()
        win.withdraw()
        file_path = filedialog.askopenfilename()
        tl.delete(0, 'end')
        tl.insert(0, file_path)
        win.destroy()

    part0()
    # 标签
    label = ttk.Label(frame,
                      text='输入内容',
                      font=(r'C:\Windows\Fonts\msyh.ttc', 15),
                      compound='center'
                      )
    # 输入框
    url = tk.StringVar()
    input_ing = ttk.Entry(frame, width=30, textvariable=url)
    input_ing.delete(0, 0)
    # input_ing.insert(0, "默认文本...")
    label.place(relx=0.15, rely=0.2)
    input_ing.place(relx=0.35, rely=0.2)

    # 背景颜色
    choose_color1 = tk.StringVar()
    cc1 = ttk.Entry(frame, width=30, textvariable=choose_color1)
    cc1.delete(0, 'end')
    cc1.insert(0, '#FFFFFF')

    label1 = ttk.Label(frame,
                       text='背景颜色',
                       font=(r'C:\Windows\Fonts\msyh.ttc', 15),
                       compound='center')
    label1.place(relx=0.15, rely=0.3)
    cc1.place(relx=0.35, rely=0.3)

    # 前景颜色
    choose_color2 = tk.StringVar()
    cc2 = ttk.Entry(frame, width=30, textvariable=choose_color2)
    cc2.delete(0, 'end')
    cc2.insert(0, '#000000')

    label2 = ttk.Label(frame,
                       text='前景颜色',
                       font=(r'C:\Windows\Fonts\msyh.ttc', 15),
                       compound='center')
    label2.place(relx=0.15, rely=0.4)
    cc2.place(relx=0.35, rely=0.4)

    # 获取中部图片
    label3 = ttk.Label(frame,
                       text='LOGO',
                       font=(r'C:\Windows\Fonts\msyh.ttc', 15),
                       compound='center')
    get_logo = tk.StringVar()
    tl = ttk.Entry(frame, width=30, textvariable=get_logo)
    # tl.delete(0, 'end')
    # tl.insert(0, '*.png')
    label3.place(relx=0.15, rely=0.5)
    tl.place(relx=0.35, rely=0.5)

    func = ttk.Button(frame,
                      text='生成',
                      width=7,
                      compound='center',
                      command=part1)
    # 把部件贴上去
    func.place(anchor='center', relx=0.5, rely=0.7)

    insert = ttk.Button(frame,
                        text='导入',
                        width=7,
                        compound='top',
                        command=find_picture)
    insert.place(relx=0.65, rely=0.5)


def otherFunction(frame):
    ttk.Label(frame, text="功能正在开发中……").place(relx=.4, rely=.9)


def openWeather(frame):
    try:
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            opw_city = myDict.get("city")
            opw_API = myDict.get("openweatherAPI")
    except BaseException:
        return False
    language = 'zh_cn'  # 简体中文  &lang={language}

    url = f'http://api.openweathermap.org/data/2.5/weather?q={opw_city}&units=metric&appid={opw_API}&lang={language}'

    target = requests.get(url)
    content = target.json()
    s = json.dumps(content, ensure_ascii=False, indent=2)
    data = json.loads(s)

    if data["cod"] == 200:
        mycity = data["name"]
        weather_description = data["weather"][0]["description"]  # 多云
        temp = data['main']['temp']  # ℃
        humidity = data['main']['humidity']  # %

        weatherInformation = f"{mycity}    {weather_description}    {temp}℃    {humidity}%"

        ttk.Label(frame, text=weatherInformation).place(relx=.5, rely=.95)


DefaultFont = r"C:\Windows\Fonts\calibril.ttf"


def get_audio_duration(file_path):
    # 根据文件扩展名选择合适的mutagen类
    if file_path.endswith('.mp3'):
        audio = MP3(file_path)
    elif file_path.endswith('.flac'):
        audio = FLAC(file_path)
    elif file_path.endswith('.opus'):
        audio = OggOpus(file_path)
    elif file_path.endswith('.ogg'):
        audio = OggVorbis(file_path)
    else:
        return 0
    # 获取音频时长（以秒为单位）
    md_duration = audio.info.length
    return md_duration


def musicPlayer(window):
    try:
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            DefaultPath = myDict.get("musicPlayerDirectory")
            if not DefaultPath:
                messagebox.showerror(title="Error",
                                     message="读取音乐文件夹设置生错误，\n请在[../setting/Setting-musicPlayer.txt]内填入音乐文件夹路径\n"
                                             "或者使用设置工具")
    except BaseException:
        DefaultPath = r"C:\Users\Default\Music"

    def pause_music():
        try:
            pygame.mixer.music.pause()
            music_state("播放暂停")
        except pygame.error:
            pass

    def unpouse_music():
        try:
            pygame.mixer.music.unpause()
            music_state("正在播放")
        except pygame.error:
            pass

    def stop_music():
        try:
            pygame.mixer.music.stop()
            music_state("等待输入")
            pygame.quit()  # 退出pygame以修复前面两个键的bug
        except pygame.error:
            pass
        finally:
            show_current_music("None")
            show_music_length("")

    def show_current_music(txt: str):
        tk.Label(window, text=txt, foreground="#FFFFFF", background="#c6c8cd", width=70).place(relx=.2, rely=.07)

    def music_state(txt: str):
        tk.Label(window, text=txt, foreground="#000000", font=("微软雅黑", 16), width=8, compound="center"
                 ).place(relx=.05, rely=.05)

    def show_music_length(txt: str):
        tk.Label(window, text=txt, width=6).place(relx=.85, rely=.07)

    global volume_change, loop, choose_music, listbox
    # 正在播放的音乐
    music_state("等待输入")
    ttk.Button(window, text="暂停播放", command=lambda: pause_music(), width=8).place(relx=.125, rely=.2)
    ttk.Button(window, text="继续播放", command=lambda: unpouse_music(), width=8).place(relx=.225, rely=.2)
    ttk.Button(window, text="停止播放", command=lambda: stop_music(), width=8).place(relx=.325, rely=.2)
    show_current_music("None")

    # 添加音乐文件
    choose_music = tk.StringVar()
    choose_music.set("输入文件地址")
    ttk.Label(window, text="选择音乐文件", font=(DefaultFont, 10)).place(relx=.05, rely=.705)
    c_m = ttk.Entry(window, textvariable=choose_music, width=20)
    c_m.place(relx=.16, rely=.7)
    ttk.Button(window, text="浏览", command=lambda: find_files(c_m)).place(relx=.36, rely=.695)
    ttk.Button(window, text="播放所选音乐", command=lambda: play_music1()).place(relx=.2, rely=.8)

    # 播放设置
    loop = tk.StringVar()
    loop.set(-1)
    ttk.Radiobutton(window, text='单曲循环', variable=loop, value=-1).place(relx=.12, rely=.3)
    ttk.Radiobutton(window, text='播放一次', variable=loop, value=1).place(relx=.3, rely=.3)

    # 音量调节
    ttk.Label(window, text="音量调节", font=(DefaultFont, 10)).place(relx=.15, rely=.4)
    list_volume = []
    for i in range(101):
        if i % 5 == 0:
            list_volume.append(i)
    volume_change = ttk.Combobox(window, values=list_volume, width=5)
    volume_change.set(80)
    volume_change.place(relx=.3, rely=.4)

    # 显示.\\playlist中的音乐文件
    ttk.Label(window, text="可播放音乐列表", font=("Microsoft YaHei", 12)).place(relx=.6, rely=.2)
    listbox = tk.Listbox(window, width=35, height=10)
    listbox.place(relx=.6, rely=.3)

    # ttk.Label(window, text="在设置中指定音乐文件夹").place(relx=.6, rely=.73)

    # try:
    #     os.mkdir('Playlist')  # 二次运行报错，因为文件存在
    # except FileExistsError:
    #     print("文件夹[Playlist]存在")
    def play(path):
        try:
            if path:
                pygame.mixer.init()  # 初始化混音器模块（pygame库的通用做法，每一个模块在使用时都要初始化pygame.init(
                # )为初始化所有的pygame模块，可以使用它也可以单初始化这一个模块）
                pygame.mixer.music.load(path)  # 加载音乐
                pygame.mixer.music.set_volume(int(volume_change.get()) / 100)  # 设置音量大小0~1的浮点数
                pygame.mixer.music.play(int(loop.get()))  # 播放音频
                current_music = re.split(r"[\\|/]", path)[-1]
                show_current_music(current_music)
                music_time = get_audio_duration(path)
                txt = f"{str(int(music_time // 60))}分{str(int(music_time % 60))}秒"
                if music_time == 0:
                    txt = "未知时长"
                show_music_length(txt)
                music_state("正在播放")
        except BaseException:
            show_current_music("None")
            show_music_length("")
            messagebox.showerror(title="Error", message="发生了一个错误!")

    def play_music2():
        stop_music()
        try:
            num = listbox.curselection()[0]
            music = list(listbox.get(0, tk.END))[num]
            path = f"{DefaultPath}\\{music}"
            play(path)
        except IndexError:
            messagebox.showerror(title="Error", message="发生了一个错误!")

    def play_music1():
        stop_music()
        path = choose_music.get()
        play(path)

    for i, j, k in os.walk(DefaultPath):
        for mzk in range(len(k)):
            listbox.insert(tk.END, k[mzk])
        ttk.Button(window, text="播放选中", command=lambda: play_music2()).place(relx=.73, rely=.8)

    # 说明播放器局限
    # ttk.Label(window, text="不支持某些特殊格式").place(relx=.4, rely=.95)
    ttk.Button(
        window, text="帮助", width=8,
        command=lambda: messagebox.showinfo(title="提示信息", message="[bug]完整运行“播放一次”后程序会终止运行！\n"
                                                                      "不支持某些特殊格式，如音乐软件的会员格式，\n"
                                                                      "请在设置中指定音乐文件夹。")
    ).place(relx=.9, rely=.8)


moneyUrl = "https://themoneyconverter.com/zh-CN"

moneyDict = {'阿联酋迪拉姆': 'AED', '阿根廷比索': 'ARS', '澳元': 'AUD', '阿魯巴弗羅林': 'AWG',
             '波斯尼亚和黑塞哥维那可兑换马克': 'BAM', '巴巴多斯元': 'BBD', '孟加拉塔卡': 'BDT', '保加利亞列弗': 'BGN',
             '巴林第纳尔': 'BHD', '百慕達元': 'BMD', '玻利維亞諾': 'BOB', '巴西雷亚尔': 'BRL', '巴哈馬元': 'BSD',
             '波札那普拉': 'BWP', '加元': 'CAD', '瑞士法郎': 'CHF', '智利比索': 'CLP', "人民币": "CNY",
             '哥伦比亚比索': 'COP', '捷克克朗': 'CZK', '丹麦克朗': 'DKK', '多明尼加比索': 'DOP', '埃及鎊': 'EGP',
             '欧元': 'EUR', '斐濟元': 'FJD', '英镑': 'GBP', '迦納塞地': 'GHS', '甘比亞達拉西': 'GMD',
             '瓜地馬拉格查爾': 'GTQ', '港元': 'HKD', '匈牙利福林': 'HUF', '印尼盾': 'IDR', '以色列谢克尔': 'ILS',
             '印度卢比': 'INR', '伊朗里亞爾': 'IRR', '冰岛克朗': 'ISK', '牙买加元': 'JMD', '约旦第纳尔': 'JOD',
             '日元': 'JPY', '肯尼亚先令': 'KES', '柬埔寨瑞爾': 'KHR', '韩元': 'KRW', '科威特第纳尔': 'KWD',
             '寮國基普': 'LAK', '黎巴嫩镑': 'LBP', '斯里兰卡卢比': 'LKR', '摩洛哥迪拉姆': 'MAD', '摩爾多瓦列伊': 'MDL',
             '阿里亞里': 'MGA', '馬其頓代納爾': 'MKD', '模里西斯盧比': 'MUR', '馬爾地夫拉菲亞': 'MVR',
             '墨西哥比索': 'MXN', '马来西亚林吉特': 'MYR', '纳米比亚元': 'NAD', '奈及利亞奈拉': 'NGN',
             '挪威克朗': 'NOK', '尼泊尔卢比': 'NPR', '新西兰元': 'NZD', '阿曼里亚尔': 'OMR', '巴拿马波亚': 'PAB',
             '秘鲁索尔': 'PEN', '菲律宾比索': 'PHP', '巴基斯坦卢比': 'PKR', '波兰兹罗提': 'PLN', '巴拉圭瓜拉尼': 'PYG',
             '卡塔尔里亚尔': 'QAR', '罗马尼亚列伊': 'RON', '塞爾維亞第納爾': 'RSD', '俄罗斯卢布': 'RUB',
             '沙特里亚尔': 'SAR', '塞席爾盧比': 'SCR', '瑞典克朗': 'SEK', '新加坡元': 'SGD', '泰铢': 'THB',
             '突尼斯第納爾': 'TND', '土耳其里拉': 'TRY', '特立尼达和多巴哥元': 'TTD', '新臺幣': 'TWD',
             '乌克兰格里夫纳': 'UAH', '烏干達先令': 'UGX', '美元': 'USD', '烏拉圭比索': 'UYU',
             '委内瑞拉玻利瓦尔': 'VES', '越南盾': 'VND', '中非法郎': 'XAF', '东加勒比海元': 'XCD', '西非法郎': 'XOF',
             '太平洋法郎': 'XPF', '南非南特': 'ZAR'}

moneyList = list(moneyDict.keys())


def openBrowse():
    with open(".\\run.bat", "w", encoding="utf-8") as file:
        file.write(f"start {moneyUrl}")
    os.system(".\\run.bat")
    os.remove(".\\run.bat")


def conMon(source, target, m):
    if source and target and m:
        url = f"https://themoneyconverter.com/zh-CN/{moneyDict.get(source)}/{moneyDict.get(target)}?amount=1"
        c = requests.get(url)
        c.encoding = "utf-8"
        pattern = r'1 (\w{3}) = ([\d.]+) (\w{3})'
        x = re.findall(pattern, c.text)
        rate = x[-1][1]
        out = eval(m) * eval(rate)

        e1.delete(0, "end")
        e1.insert("end", out)


def moneyConvert(frame):
    ttk.Label(frame, text="名存实亡的货币转换器（bushi", font=("微软雅黑 bold", 16)).place(relx=.3, rely=.1)
    box = ScrolledText(frame, width=40, height=0.01)
    box.place(relx=.3, rely=.2)
    box.insert("end", "你可以复制这个链接到浏览器打开：\n" + moneyUrl +
               "\n作者只是把前端做了，后端要一点点技术，拖着一点点完成吧。（上头了，于是做完了）"
               "\n项目灵感来源：https://gitee.com/huacaoye/the-money-converter"
               "\n由于正则表达式的原因，数据有可能会出错。")
    box["state"] = "disabled"
    ttk.Button(frame, text="召唤真正的货币转换工具", command=openBrowse).place(relx=.4, rely=.9)

    ttk.Label(frame, text="From\t\t\t\t\tTo").place(relx=.2, rely=.4)
    sbox = ttk.Combobox(frame, values=moneyList, width=12)
    tbox = ttk.Combobox(frame, values=moneyList, width=12)
    sbox.set("人民币")
    tbox.set("美元")
    sbox.place(relx=.32, rely=.4)
    tbox.place(relx=.65, rely=.4)

    num = tk.StringVar()
    ttk.Entry(frame, textvariable=num, width=16).place(relx=.25, rely=.5)
    global e1
    e1 = ttk.Entry(frame, width=16)
    e1.place(relx=.6, rely=.5)
    # 中部符号按钮
    ttk.Button(
        frame, text=">>>", command=lambda: conMon(sbox.get(), tbox.get(), num.get())
    ).place(relx=.44, rely=.5)


PWD_Dict = {"纯数字": "1234567890",  # 纯数字
            "数字+小写字母": "1234567890abcdefghijklmnopqrstuvwxyz",  # 数字+小写字母
            "数字+大写字母": "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # 数字+大写字母
            "纯小写字母": "abcdefghijklmnopqrstuvwxyz",  # 纯小写字母
            "纯大写字母": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # 纯大写字母
            "数字+小写字母+符号": "1234567890abcdefghijklmnopqrstuvwxyz!@#$%&*?.",  # 数字+小写字母+符号
            "数字+大写字母+符号": "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?.",  # 数字+大写字母+符号
            "数字+字母": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",  # 数字+字母
            "终极奥义": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?."  # 终极奥义
            }

pwdListKeys = list(PWD_Dict.keys())


def ConSha256(original_string):
    if original_string:  # 假设我们有一个字符串
        # 选择一个哈希算法，比如sha256
        hash_object = hashlib.sha256(original_string.encode())

        # 获取十六进制格式的哈希值
        hex_dig = hash_object.hexdigest()

        print(hex_dig, type(hex_dig))  # 输出哈希值

        scText["state"] = "normal"
        scText.insert("end", "sha256：" + hex_dig + "\n")
        scText["state"] = "disabled"


def ConMD5(x):
    if x:
        # 选择一个哈希算法，比如MD5
        hash_object = hashlib.md5(x.encode())

        # 获取十六进制格式的哈希值
        hex_dig = hash_object.hexdigest()
        scText["state"] = "normal"
        scText.insert("end", "md5：" + hex_dig + "\n")
        scText["state"] = "disabled"


def makeKey(key, num):
    if key and num.isdigit():
        x = PWD_Dict.get(key)
        y = int(num)
        if x and y:
            pwd = ""
            for i in range(y):
                j = random.randint(0, len(x) - 1)
                pwd += x[j]
            scText["state"] = "normal"
            scText.insert("end", f"{key}：{pwd}\n")
            scText["state"] = "disabled"


def keyFrame(frame):
    ttk.Label(
        frame, text="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?.", font=("微软雅黑", 10),
    ).place(relx=.02, rely=.02)
    # sha256
    sha256 = tk.StringVar()
    ttk.Label(frame, text="生成Sha256码").place(relx=.02, rely=.2)
    ttk.Entry(frame, width=30, textvariable=sha256).place(relx=.2, rely=.2)
    ttk.Button(frame, width=8, text="生成", command=lambda: ConSha256(sha256.get())).place(relx=.62, rely=.2)

    # md5
    md5 = tk.StringVar()
    ttk.Label(frame, text="生成md5码").place(relx=.02, rely=.3)
    ttk.Entry(frame, width=30, textvariable=md5).place(relx=.2, rely=.3)
    ttk.Button(frame, width=8, text="生成", command=lambda: ConMD5(md5.get())).place(relx=.62, rely=.3)

    # 一般
    choice = tk.StringVar()
    ttk.Label(frame, text="生成一般密码").place(relx=.02, rely=.4)
    ttk.Combobox(frame, values=pwdListKeys, width=20, textvariable=choice).place(relx=.2, rely=.4)
    ttk.Label(frame, text="密码长度", width=8).place(relx=.5, rely=.4)
    pwdNum = tk.StringVar()
    ttk.Entry(frame, width=8, textvariable=pwdNum).place(relx=.62, rely=.4)
    ttk.Button(
        frame, width=8, text="生成", command=lambda: makeKey(choice.get(), pwdNum.get())
    ).place(relx=.72, rely=.4)

    # 结果输出框
    global scText
    scText = ScrolledText(frame, width=60, height=5, state="disabled")
    scText.place(relx=.1, rely=.5)

    def deleteContent():
        scText.config(state="normal")
        scText.delete("1.0", "end")
        scText.config(state="disabled")

    ttk.Button(frame, text="Clear", width=8, command=deleteContent).place(relx=.58, rely=.7)


def create_files(name, content):
    with open(name, 'w', encoding='utf-8') as file:
        file.write(content)


def create():
    # print('***批量创建文件(文件夹)***\n')
    # print('注意:此程序在创建文件方面有一定的局限性!\n')
    try:
        while True:
            tgt_path = v_path.get()
            if not tgt_path:
                tk.messagebox.showerror(title='Error!', message='请输入工作路径')
                return False
            else:
                break
        os.chdir(tgt_path)
    except FileNotFoundError:
        tk.messagebox.showinfo(title='Infor', message='找不到该目录，将创建一个新目录')
        os.mkdir(tgt_path)
    except OSError:
        return False
    finally:
        os.chdir(tgt_path)
        print('\n当前工作路径：', os.getcwd())

    try:
        global formats, first_name, last_name, file_content, start_num, file_num
        formats = v_formats.get()
        first_name = v_first_name.get()
        last_name = v_last_name.get()
        file_content = v_content.get()
        start_num = eval(v_start.get())
        file_num = eval(v_num.get())
    except SyntaxError:
        tk.messagebox.showerror(title='SyntaxError', message=' 请确认参数是否设置正确!')

    # print('\n' + '-' * 5 + '开始创建' + '-' * 5 + '\n')
    try:
        if not last_name:
            if formats == 1:
                for i in range(file_num):
                    os.makedirs(f'.\\{first_name}{start_num + i}')
            else:
                for i in range(file_num):
                    os.makedirs(f'.\\{start_num + i}{first_name}')
        else:
            if formats == 1:
                for i in range(file_num):
                    file_name = f'.\\{first_name}{start_num + i}{last_name}'
                    create_files(file_name, file_content)
            else:
                for i in range(file_num):
                    file_name = f'.\\.\\{start_num + i}{first_name}{last_name}'
                    create_files(file_name, file_content)
        tk.messagebox.showinfo(message='创建完毕', title='Infor')
    except FileExistsError:
        tk.messagebox.showerror(title='FileExistsError', message='文件已存在!')


def makeFilesPhot(window):
    # 窗口属性
    color = None
    # tk.Label(window, text='批量创建文件', font=('微软雅黑', 20), compound='center').place(relx=0.4, rely=0)
    global v_formats, v_first_name, v_last_name, v_content, v_start, v_num, v_path

    # 请输入工作路径(您可以在此输入多级目录，程序会在最终子目录工作:
    v_path = tk.StringVar()
    ttk.Label(window, text='*工作路径:', font=('微软雅黑', 16),
              compound='center').place(relx=.45, rely=0)  #place(relx=0.45, rely=0)
    ttk.Entry(window, width=36, textvariable=v_path).place(relx=.35, rely=.1)

    v_formats, v_first_name, v_last_name, v_content, v_start, v_num \
        = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

    # 文件开头设置按钮
    v_formats.set(0)
    ttk.Label(window, text='*文件开头:', font=('Segoe UI', 10), compound='center').place(relx=0.2, rely=0.2)
    ttk.Radiobutton(window, text='数字开头', variable=v_formats, value=0).place(relx=0.4,
                                                                                rely=0.2)
    ttk.Radiobutton(window, text='文字开头', variable=v_formats, value=1).place(relx=0.6,
                                                                                rely=0.2)
    # 文件文字格式
    ttk.Label(window, text='文件文字:', font=('Segoe UI', 10), compound='center').place(relx=0.2, rely=0.3)
    ttk.Entry(window, width=30, textvariable=v_first_name).place(relx=0.5, rely=0.3)
    # 请输入文件后缀名(eg:.txt):
    ttk.Label(window, text='文件后缀名:', font=('Segoe UI', 10),
              compound='center').place(relx=0.2, rely=0.4)
    ttk.Entry(window, width=30, textvariable=v_last_name).place(relx=0.5, rely=0.4)

    # 请输入文件初始内容(可忽略):
    ttk.Label(window, text='文件内容(可忽略):', font=('Segoe UI', 10), compound='center').place(relx=0.2, rely=0.5)
    ttk.Entry(window, width=30, textvariable=v_content).place(relx=0.5, rely=0.5)

    # 将使用纯数字编号，您希望从哪个数字开始(非负数整数):
    v_start.set(1)
    ttk.Label(window, text='*起始编号:', font=('Segoe UI', 10),
              compound='center').place(relx=0.2, rely=0.6)
    ttk.Entry(window, width=30, textvariable=v_start).place(relx=0.5, rely=0.6)

    # 您希望创建多少个文件(非零自然数):
    ttk.Label(window, text='*文件数量:', font=('Segoe UI', 10),
              compound='center').place(
        relx=0.2, rely=0.7)
    ttk.Entry(window, width=30, textvariable=v_num).place(relx=0.5, rely=0.7)

    # 设置按钮
    ttk.Button(window, text='开始创建', command=create, width=10).place(relx=0.45, rely=0.85)

    # 设置备注
    tk.Label(window, text='注意:此程序在创建文件方面有一定的局限性!', compound='center').place(relx=0.35,
                                                                                               rely=0.95)


study_url = 'https://gallery.pyecharts.org/#/WordCloud/basic_wordcloud'

PDFusage = ("特殊的PDF文件，如图片生成的PDF不可读取;\n"
            "文本生成的PDF为适用对象;\n"
            "本插件目前只能读取PDF其他功能后续拓展;\n"
            "成功运行后会在文件所在目录生成一个.html文件，\n"
            "打开然后右键保存即可获得.png文件。")


def analysis(file_name):
    if file_name:
        f = file_name.split("\\")
        myF = f[-1]

        # 读取文件
        with pdfplumber.open(file_name) as pdf:
            for i in pdf.pages:  # 遍历页——对象
                text = i.extract_text()

        # 拆分文件并分析
        list1 = jieba.lcut(text)
        list2 = []
        for i in list1:
            if len(i) >= 2 and i not in list2 and not i.isdigit() and not i.replace(".", "").isdigit():
                list2.append(i)

        # 进一步分析
        dic1 = {}
        for i in list2:
            dic1[i] = 0

        for i in list1:
            if i in dic1:
                dic1[i] = dic1.get(i) + 1

        # 格式化数据 用于后面词云的生成
        list3 = []
        for i in dic1:
            list3.append([i, dic1[i]])

        list3.sort(key=lambda x: x[1], reverse=True)

        # 这里的代码参考pyecharts的中文资料 上面的链接也可
        (
            WordCloud()
            .add(series_name=myF, data_pair=list3, word_size_range=[6, 66])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title=myF, title_textstyle_opts=opts.TextStyleOpts(font_size=23)
                ),
                tooltip_opts=opts.TooltipOpts(is_show=True),
            )
            .render(f"{myF}.html")
        )

        messagebox.showinfo(title="提示信息", message="分析完成，请到文件所在目录查找!")


def analysisWindow(frame):
    ttk.Label(frame, text="PDF关键词分析").place(relx=.03, rely=0)

    filePath = tk.StringVar()
    ttk.Label(frame, text="请选择PDF文件", font=("微软雅黑", 20)).place(relx=.35, rely=.2)
    file = ttk.Entry(frame, textvariable=filePath, width=40)
    file.place(relx=.3, rely=.4)
    ttk.Button(frame, text="选择", command=lambda: find_files(file)).place(relx=.6, rely=.398)
    ttk.Button(frame, text="开始", command=lambda: analysis(filePath.get())).place(relx=.43, rely=.6)

    ttk.Button(frame, text="帮助", command=lambda: messagebox.showinfo(title="帮助", message=PDFusage),
               width=8).place(relx=.8, rely=.9)


def autoShutdown():
    os.system(".\\BoxTools\\autoShutdown.py")


def openUrl(url):
    with open(".\\run.bat", "w", encoding="utf-8") as f:
        f.write(f"start {url}")
    os.system(".\\run.bat")
    os.remove(".\\run.bat")
    time.sleep(2)
    pyautogui.press("f11")


def start3process():
    p1 = threading.Thread(target=autoShutdown)
    p1.start()
    p1 = None


lockInfo = ("没有弄懂这个程序怎么运行的请勿使用!\n"
            "BoxTools里有一个[WinLock.py]的文件，\n"
            "将它放到启动文件夹就可以实现掩耳盗铃的电脑锁了，\n"
            "所以极不推荐，\n"
            "可以利用[密码生成]生成密码的sha256值。")

btuComDict = {
    "Windows工具": lambda: os.system("start \"\" \"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Administrative "
                                     "Tools\""),
    "文件资源管理器": lambda: os.system("start explorer.exe"),
    "设置": lambda: os.system("start ms-settings:"),
    "控制面板": lambda: os.system("start control"),
    "Windows安全中心": lambda: os.system("start ms-settings:windowsdefender"),

    "Bug-1": 1,

    "系统信息": lambda: os.system("start msinfo32"),
    "任务管理器": lambda: os.system("start taskmgr"),
    "记事本": lambda: os.system("start notepad"),
    "画图": lambda: os.system("start mspaint"),
    "计算器": lambda: os.system("start calc"),

    "Bug-2": 2,

    "电脑锁": lambda: messagebox.showinfo(title="提示信息", message=lockInfo),
    "定时关机": lambda: start3process(),
    "变身黑客1": lambda: messagebox.showinfo(
        title="你也是闲的", message="这是一个扫盘命令:\n"
                                    "win+r\n"
                                    "cmd\n"
                                    "color a\n"
                                    "dir/s"),
    "变身黑客2": lambda: openUrl("http://geekprank.com/hacker"),
    "关于天文": lambda: openUrl("https://stars.chromeexperiments.com/"),

    "bug-3": 3,

    "打开程序所在目录": lambda: os.system("start .\\")
}


def winFunction(frame):
    ttk.Label(frame, text="电脑功能").place(relx=.02, rely=.02)
    i = 0
    j = 1
    for key in btuComDict:
        if i < 5:
            if j < 9:
                ttk.Button(
                    frame, text=key, command=btuComDict.get(key)
                ).place(relx=(0.02 + (i * 2 / 10)), rely=j / 10)
                i += 1
            else:
                break
        else:
            i = 0
            j += 1


languageDict = {"英语": "en",
                "中文": "zh",
                "繁体中文": "zh-TW",
                "日语": "ja",
                "韩语": "ko",
                "法语": "fr",
                "西班牙语": "es",
                "意大利语": "it",
                "德语": "de",
                "土耳其语": "tr",
                "俄语": "ru",
                "葡萄牙语": "pt",
                "越南语": "vi",
                "印尼语": "id",
                "泰语": "th",
                "马来语": "ms",
                "阿拉伯语": "ar",
                "印地语": "hi"}

languageList = list(languageDict.keys())


# 翻译并展示的函数
def translate(text, sources, target):
    if text and sources and target:
        s = languageDict.get(sources)
        if not s:
            s = sources
        t = languageDict.get(target)
        if not t:
            t = target
        outputBox.config(state="normal")
        translator = Translator(from_lang=s, to_lang=t)
        outText = translator.translate(text)
        outputBox.delete("1.0", "end")
        outputBox.insert(tk.END, outText)
        outputBox.config(state="disabled")


# 复制输出内容的函数
def copyOutPut():
    outputBox.config(state="normal")
    pyperclip.copy(outputBox.get("1.0", "end"))
    outputBox.config(state="disabled")


def translateFrame(frame):
    # 设置标签
    ttk.Label(frame, text="From\t\t\t\tTo", font=("微软雅黑", 16)).place(relx=.02, rely=.2)
    # 设置翻译语言候选框
    sLanguage = ttk.Combobox(frame, values=languageList, width=8)
    tLanguage = ttk.Combobox(frame, values=languageList, width=8)
    sLanguage.set("英语")
    tLanguage.set("中文")
    sLanguage.place(relx=.22, rely=.22)
    tLanguage.place(relx=.65, rely=.22)
    # 设置顶部提示框
    exampleLabel = ScrolledText(frame, height=0.1, width=100)
    exampleLabel.place(relx=0.02, rely=.02)
    exampleLabel.insert(tk.END,
                        "EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES "
                        "SUPPORTED BUT SOME MAY HAVE NO CONTENT.\t"
                        "MAX ALLOWED QUERY : 500 CHARS".lower() +
                        "\n当然，你也可以自己找语言标识符然后翻译。"
                        "\nThe plugin needs network.")
    exampleLabel["state"] = "disabled"
    # 设置输入框
    inputBox = ScrolledText(frame, height=16, width=40)
    inputBox.place(relx=.02, rely=.3)
    # 中部符号
    ttk.Label(frame, text=">>>", font=("微软雅黑 bold", 16), foreground="blue").place(relx=.43, rely=.5)
    # 设置输出框
    global outputBox
    outputBox = ScrolledText(frame, height=16, width=40, state="disabled")
    outputBox.place(relx=.52, rely=.3)

    # 翻译功能按钮
    ttk.Button(frame, width=8, text="Translate",
               command=lambda: translate(
                   inputBox.get("1.0", "end"), sLanguage.get(), tLanguage.get()
               )
               ).place(relx=.15, rely=.9)
    # 清除功能按钮和复制功能按钮
    ttk.Button(frame, text="Clear", width=5, command=lambda: inputBox.delete(1.0, "end")).place(relx=.345, rely=.82)
    ttk.Button(frame, text="Copy", width=5, command=copyOutPut).place(relx=.845, rely=.82)


def tdFrame(frame):
    btuComDict = {
        "Herta_kuru": lambda: os.system("start https://duiqt.github.io/herta_kuru/"),
        "Genshin Impact": lambda: os.system("start https://ys.mihoyo.com/main/"),
        "Honkai：StarRail": lambda: os.system("start https://sr.mihoyo.com/"),
        "Snap.Hutao": lambda: os.system("start https://hut.ao/zh/"),
        "Vilipix": lambda: os.system("start https://www.vilipix.com/"),

        "Bug-1": 1,

    }

    ttk.Label(frame, text="二刺猿\t作者分享的一些网站，点一下就能打开").place(relx=.02, rely=.02)
    i = 0
    j = 1
    for key in btuComDict:
        if i < 5:
            if j < 9:
                ttk.Button(
                    frame, text=key, command=btuComDict.get(key)
                ).place(relx=(0.02 + (i * 2 / 10)), rely=j / 10)
                i += 1
            else:
                break
        else:
            i = 0
            j += 1


def find_directory(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askdirectory()
    x.delete(0, 'end')
    x.insert(0, file_path)
    win.destroy()


def find_file(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.delete(0, 'end')
    x.insert(0, file_path)
    win.destroy()


def openAPI():
    if not os.path.isfile(".\\setting\\Setting-APIuse.txt"):
        with open(".\\setting\\Setting-APIuse.txt", "w", encoding="utf-8") as g4:
            g4.write("")
    else:
        with open(".\\run.bat", "w", encoding="utf-8") as file:
            file.write(r"start .\setting\Setting-APIuse.txt")
        os.system(".\\run.bat")
        os.remove(".\\run.bat")


def save():
    if not os.path.isdir(".\\setting"):
        os.mkdir(".\\setting")
    SettingInfor = {
        "musicPlayerDirectory": directoryPath.get(),
        "RandomNameDirectory": excelPath.get(),
        "ThirdPackageOutputFile": TDpath.get(),
        "mail": mail.get(),
        "mailCode": mailCode.get(),
    }
    with open(".\\setting\\Config.txt", "w", encoding="utf-8") as file:
        json.dump(SettingInfor, file, ensure_ascii=False, indent=4)

    messagebox.showinfo(title="提示信息", message="保存成功!\n重启后生效!")


def frameSetting(frame):
    global directoryPath, excelPath, TDpath, mail, mailCode, city, opwAPI
    (
        directoryPath, excelPath, TDpath, mail, mailCode, city, opwAPI
    ) = \
        (
            tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(),
            tk.StringVar()
        )

    # 音乐文件夹设置
    ttk.Label(frame, text="设置[音乐播放器]的音乐文件夹").place(relx=.02, rely=.02)
    fp = ttk.Entry(frame, textvariable=directoryPath, width=14)
    fp.place(relx=.25, rely=.018)
    ttk.Button(frame, text="选择", command=lambda: find_directory(fp)).place(relx=.4, rely=.015)

    # 随机点名文件设置
    ttk.Label(frame, text="设置[随机点名]的默认文件").place(relx=.02, rely=.12)
    ep = ttk.Entry(frame, textvariable=excelPath, width=14)
    ep.place(relx=.25, rely=.118)
    ttk.Button(frame, text="选择", command=lambda: find_file(ep)).place(relx=.4, rely=.115)

    # 快捷方式
    # C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
    # C:\ProgramData\Microsoft\Windows\Start Menu\Programs
    ttk.Button(frame, text="开机自启动，添加到开始菜单，创建桌面快捷方式",
               command=lambda:
               messagebox.showinfo(
                   title="设置指南",
                   message="自己动手，~~~~!"
                           "\n设置开机自启动:将主文件的快捷方式放到[C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup]"
                           "\n添加到开始菜单:主文件的快捷方式放到[C:\ProgramData\Microsoft\Windows\Start Menu\Programs]"
                           "\n创建桌面快捷方式:\n快捷方式放到桌面就可以了")).place(relx=.07, rely=.2)

    ttk.Label(frame, text="设置[Python第三方库工具]导出路径(必须是.txt文件结尾)").place(relx=.02, rely=.32)
    tp = ttk.Entry(frame, textvariable=TDpath, width=14)
    tp.place(relx=.05, rely=.418)
    ttk.Button(frame, text="选择", command=lambda: find_file(tp)).place(relx=.2, rely=.415)

    # 设置首页美文
    instruction = ("当你自定义了美文，原有的API将不会生效，\n"
                   "你可以定义多个，但要分行列出，\n"
                   "使用此功能可以在一定程度上加速程序打开，\n"
                   "并且会取消首页美文对互联网的依赖，建议使用;\n"
                   "当你清空文件或者移动删除了该文件，API生效。")
    ttk.Button(frame, text="自定义首页美文", command=openAPI).place(relx=.06, rely=.52)
    ttk.Button(frame, text="该项说明",
               command=lambda: messagebox.showinfo(title="提示信息", message=instruction)).place(relx=.22, rely=.52)

    # 设置邮箱，配置授权码
    ttk.Label(frame, text="配置邮箱").place(relx=.02, rely=.6)
    ttk.Entry(frame, width=20, textvariable=mail).place(relx=.1, rely=.6)
    # ttk.Button(window, width=8).place(relx=.28, rely=.598)
    ttk.Label(frame, text="配置邮箱授权码").place(relx=.02, rely=.7)
    ttk.Entry(frame, width=20, textvariable=mailCode).place(relx=.15, rely=.7)

    # 天气设置
    ttk.Label(frame, text="城市(市的拼音)").place(relx=.02, rely=.8)
    ttk.Entry(frame, width=20, textvariable=city).place(relx=.15, rely=.8)
    ttk.Label(frame, text="openWeather API").place(relx=.02, rely=.9)
    ttk.Entry(frame, width=20, textvariable=opwAPI).place(relx=.2, rely=.9)

    try:
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            directoryPath.set(myDict.get("musicPlayerDirectory"))
            excelPath.set(myDict.get("RandomNameDirectory"))
            TDpath.set(myDict.get("ThirdPackageOutputFile"))
            mail.set(myDict.get("mail"))
            mailCode.set(myDict.get("mailCode"))
            city.set(myDict.get("city"))
            opwAPI.set(myDict.get("openweatherAPI"))
    except BaseException:
        pass

    # 保存按钮
    ttk.Button(frame, text="保存", command=save, width=8).place(relx=.9, rely=.02)


def findLocation(loc: str):
    if loc:
        cities = {}
        with open(".\\resource\\CN.txt", "r", encoding="utf-8") as file:
            basicData = file.readlines()
            for i in basicData:
                j = i.split("\t")
                cities[j[2]] = {"lon": float(j[-3]), "lat": float(j[-2]), "main": i}

        pos = cities.get(loc)
        if not pos:
            messagebox.showinfo(title="提示信息", message="未查询到该地址的经纬度!\n"
                                                          "请检查输入，或者[.\\resource\\CN.txt]不存在该值。")
            print("未查询到该地址的经纬度")
        else:
            inforLocation.config(state="normal")
            inforLocation.insert(
                "end",
                f"{loc} >>> 经度: {pos.get('lon')}, 纬度: {pos.get('lat')}\n"
                f"{pos.get('main')}"
            )
            inforLocation.config(state="disabled")
            print(pos)


def flFrame(frame):
    ttk.Label(frame, text="中国地理信息查询", font=("微软雅黑", 16)).place(relx=.375, rely=.05)
    location = tk.StringVar()
    ttk.Entry(frame, textvariable=location, width=16).place(relx=.42, rely=.2)
    ttk.Button(
        frame, text="帮助", width=8,
        command=lambda: messagebox.showinfo(title="提示信息", message="输入地名以查询地理信息，示例：\n"
                                                                      "Shuangliu District\n"
                                                                      "Xinjin County\n"
                                                                      "Chengdu\n"
                                                                      "Yan'an\n"
                                                                      "结果示例:"
                                                                      "CN\t100000\tBeijing\tBeijing\t22\tBeijing\t39.9075\t116.3972\t4\n"
                                                                      "数据来源于:https://www.geonames.org/\n"
                                                                      "数据获取日期:2024年7月26日")
    ).place(relx=.9, rely=.8)

    ttk.Button(frame, text="查询", width=8, command=lambda: findLocation(location.get())).place(relx=.45, rely=.3)

    global inforLocation
    inforLocation = ScrolledText(frame, width=40, height=8, state="disabled")
    inforLocation.place(relx=.32, rely=.5)
    ttk.Label(frame, text="查询结果").place(relx=.63, rely=.76)


def makeMark(Fpath, name):
    s1.config(state="normal")
    if Fpath and name:
        s1.delete("1.0", "end")
        s1.insert("end", "文件地址：" + Fpath)
        bwm1 = WaterMark(password_img=1, password_wm=1)
        bwm1.read_img(Fpath)
        s1.insert("end", '\n您的文字水印：' + name)
        bwm1.read_wm(name, mode='str')
        pwd = len(bwm1.wm_bit)
        fp = Fpath.split(".")[0] + "_" + str(pwd) + "." + Fpath.split(".")[1]
        bwm1.embed(fp)
        print('您所需要的图片位于', fp)
        s1.insert("end", f"您所需要的图片位于：{fp}")
        # print(pwd, type(pwd))
        # print(type(bwm1.wm_bit), type(bwm1))
        s1.insert("end", "\n正在验证是否成功添加水印……\n")
        judgeMark(pwd, fp, False)
    s1.config(state="disabled")


# 验证
# print('正在验证是否成功添加水印……')
# bwm1 = WaterMark(password_img=1, password_wm=1)
# wm_extract = bwm1.extract('D:/Blind_watermark/photo_output/embedded.png', wm_shape=pwd, mode='str')
# print('您的水印为：', wm_extract)
# print(wm_extract == wm)
# print('请妥善保存解水印密码 {len_wm}'.format(len_wm=pwd))
def judgeMark(pwd: int, path, x: bool):
    time.sleep(2)  # 卡了
    s1.config(state="normal")
    if x:
        s1.delete("1.0", "end")
    if pwd and path:
        s1.insert("end", "水印识别码：" + str(pwd))
        bwm1 = WaterMark(password_img=1, password_wm=1)
        wm_extract = bwm1.extract(filename=path, wm_shape=pwd, mode='str')
        s1.insert("end", '\n提取到的水印为：' + wm_extract + "\n提取完成！")
    s1.config(state="disabled")


def getFileFrame(frame):
    # 添加水印
    path1, markName = tk.StringVar(), tk.StringVar()
    l1 = ttk.Label(frame, text="输入图片路径")
    e1 = ttk.Entry(frame, width=20, textvariable=path1)
    b3 = ttk.Button(frame, width=8, text="选择", command=lambda: find_files(e1))
    l2 = ttk.Label(frame, text="输入水印名称")
    e2 = ttk.Entry(frame, width=20, textvariable=markName)

    # 查看水印
    pwd = tk.IntVar()
    l3 = ttk.Label(frame, text="输入水印识别码")
    e4 = ttk.Entry(frame, width=20, textvariable=pwd)

    global s1
    s1 = ScrolledText(frame, width=50, height=10, state="disabled")
    b1 = ttk.Button(frame, text="开始", width=8, command=lambda: makeMark(path1.get(), markName.get()))
    b2 = ttk.Button(frame, width=8, text="开始", command=lambda: judgeMark(pwd.get(), path1.get(), True))

    def markForgetAll():
        for i in [l1, l2, l3, b1, b2, b3, e1, e2, e4, s1]:
            i.place_forget()

    def showBut(f):
        markForgetAll()
        path1.set("")
        markName.set("")
        pwd.set(0)
        if f == 1:
            l1.place(relx=.22, rely=.1)
            e1.place(relx=.37, rely=.1)
            b3.place(relx=.62, rely=.1)
            l2.place(relx=.22, rely=.2)
            e2.place(relx=.37, rely=.2)
            b1.place(relx=.55, rely=.3)
            s1.place(relx=.22, rely=.4)
        else:
            l1.place(relx=.22, rely=.1)
            e1.place(relx=.37, rely=.1)
            b3.place(relx=.62, rely=.1)
            l3.place(relx=.22, rely=.2)
            e4.place(relx=.37, rely=.2)
            b2.place(relx=.55, rely=.3)
            s1.place(relx=.22, rely=.4)

    ttk.Button(frame, text="添加水印", command=lambda: showBut(1)).place(relx=.02, rely=.1)
    ttk.Button(frame, text="查看水印", command=lambda: showBut(2)).place(relx=.02, rely=.2)
    ttk.Button(
        frame, text="介绍", width=8, command=lambda: messagebox.showinfo(title="提示信息",
                                                                         message="blind_watermark是一个可以添加、提取图片盲水印的Python工具，支持添加数字、嵌入图片、嵌入文本、嵌入二进制四种方式。可以防止旋转角度、随机截图、多遮挡、纵向裁剪、横向裁剪、缩放攻击等效果。"
                                                                                 "\n项目地址：https://github.com/guofei9987/blind_watermark/"
                                                                                 "\n开源协议：MIT"
                                                                                 "\n工具箱的作者只对文本型盲水印有研究，所以此处功能有限，可见水印另请高明"
                                                                                 "\n图片路径中含有中文字符可能会导致水印添加失败，由于作者实力不济，图片路径中只允许有一个“.”，否则也会导致失败"
                                                                                 "\n运行结果框中未出现“成功”则表示失败"
                                                                                 "\n添加盲水印的图片大小会变大，清晰度会下降"
                                                                         )
    ).place(relx=.9, rely=.8)


def readMailInfo():
    try:
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            mailConfig = [myDict.get("mail"), myDict.get("mailCode")]
            return mailConfig
    except BaseException:
        pass


def sendMail(inf):
    if inf:
        # SMTP服务器,这里使用163邮箱
        mail_host = "smtp." + inf[0].split("@")[1]  #"smtp.qq.com"
        # 发件人邮箱
        mail_sender = inf[0]
        # 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
        mail_license = inf[1]
        # 收件人邮箱，可以为多个收件人
        mail_receivers = vTo.get()

        mm = MIMEMultipart('related')

        # 邮件主题
        subject_content = subject.get()
        # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
        mm["From"] = mail_sender
        # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
        mm["To"] = mail_receivers
        # 设置邮件主题
        mm["Subject"] = Header(subject_content, 'utf-8')

        # 邮件正文内容
        body_content = writeMail.get("1.0", "end")
        # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
        message_text = MIMEText(body_content, "plain", "utf-8")
        # 向MIMEMultipart对象中添加文本对象
        mm.attach(message_text)

        # 创建SMTP对象
        stp = smtplib.SMTP()
        # 设置发件人邮箱的域名和端口，端口地址为25
        stp.connect(mail_host, 25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        stp.set_debuglevel(1)
        # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
        stp.login(mail_sender, mail_license)
        # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
        stp.sendmail(mail_sender, mail_receivers, mm.as_string())
        print("邮件发送成功")
        messagebox.showinfo(title="提示信息", message="邮件发送成功!")
        # 关闭SMTP对象
        stp.quit()


def showHistory(inf):
    if inf:
        showMail["state"] = "normal"
        showMail.delete("1.0", "end")

        # 配置IMAP服务器信息
        imap_host = "smtp." + inf[0].split("@")[1]
        username = inf[0]  # pfolg@foxmail.com
        password = inf[1]  # 或者使用授权码

        # 连接到IMAP服务器
        mail = imaplib.IMAP4_SSL(imap_host)
        mail.login(username, password)

        # 选择邮箱中的收件箱
        mail.select('inbox')

        # 搜索所有邮件
        status, messages = mail.search(None, 'ALL')

        msgList = messages[0].split()
        i = -1
        # listSubject = []
        # listContent = []
        while True:
            num = msgList[i]
            # 遍历邮件
            print()
            showMail.insert(tk.END, f"<{abs(i)}>" + "-" * 50 + "\n")
            # 获取邮件的详细信息
            status, data = mail.fetch(num, '(RFC822)')
            # 解析邮件内容
            msg = email.message_from_bytes(data[0][1])
            # 打印邮件主题
            try:
                print("~~~\n")
                showMail.insert(tk.END, "~~~\n")
                subject = (email.header.decode_header(msg['Subject'])[0][0]).decode()
                print('Subject:', subject)
                showMail.insert(tk.END, 'Subject:    ' + subject)
            except BaseException:
                showMail.insert(tk.END, 'Subject:    None')

            try:
                from_header = email.utils.getaddresses([msg['From']])  # [0][1]
                showMail.insert(tk.END, "\nFrom:   ")
                for j in from_header:
                    showMail.insert(tk.END, j[1])
            except BaseException:
                showMail.insert(tk.END, "\nFrom:   None")

            try:
                to_header = email.utils.getaddresses([msg['To']])  # [0][1]
                showMail.insert(tk.END, "\nTo:   ")
                for k in to_header:
                    showMail.insert(tk.END, k[1] + " ")
            except BaseException:
                showMail.insert(tk.END, "\nTo:   None")
            showMail.insert(tk.END, "\n~~~\n")
            print("~~~")
            # 如果需要读取邮件正文
            if msg.is_multipart():
                # 多部分邮件
                for part in msg.walk():
                    # 获取邮件内容类型
                    content_type = part.get_content_type()
                    # 获取邮件内容编码
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # 获取邮件内容
                        body = part.get_payload(decode=True)  # .decode()
                    except:
                        # 如果邮件内容是二进制类型
                        body = part.get_payload(decode=True)
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # 如果是纯文本内容
                        print(body.decode())
                        showMail.insert(tk.END, body.decode() + "\n")
            else:
                # 单部分邮件
                if msg.get_content_type() == "text/plain":
                    # 如果是纯文本内容
                    print(msg.get_payload(decode=True).decode())
            i -= 1
            if i == -6:
                break

        # 关闭连接
        mail.close()
        mail.logout()
        showMail["state"] = "disabled"


def mainMail(frame):
    # 写邮件内容的文本框
    global vFrom, vTo, writeMail, subject
    writeMail = ScrolledText(frame, height=16, width=70)
    writeMail.insert(tk.END, "在此键入邮件内容")

    vFrom, vTo, subject = tk.StringVar(), tk.StringVar(), tk.StringVar()
    fromAddrLabel = ttk.Label(frame, text="From")
    fromAddrEntry = ttk.Entry(frame, width=35, textvariable=vFrom)
    toAddrLabel = ttk.Label(frame, text="To")
    toAddrEntry = ttk.Entry(frame, width=35, textvariable=vTo)
    subjectLabel = ttk.Label(frame, text="主题")
    subjectEntry = ttk.Entry(frame, width=35, textvariable=subject)
    try:
        myMail = readMailInfo()
        vFrom.set(myMail[0])
        mailNum = ttk.Label(frame, text=myMail[0], font=("微软雅黑", 16))
    except BaseException:
        vFrom.set("发生了错误，请先配置相关设置!")

    global showMail

    sendButton = ttk.Button(frame, width=8, text="SEND", command=lambda: sendMail(myMail))

    # 只读文本框，查看邮件
    showMail = ScrolledText(frame, height=20, width=70, state="normal")
    showMail.insert(tk.END, "目前啥都没有")
    showMail.config(state="disabled")

    mailRefresh = ttk.Button(frame, text="查询", width=8, command=lambda: showHistory(myMail))

    def mailForgetAll():
        showMail.place_forget()
        writeMail.place_forget()
        fromAddrLabel.place_forget()
        fromAddrEntry.place_forget()
        toAddrLabel.place_forget()
        toAddrEntry.place_forget()
        sendButton.place_forget()
        mailNum.place_forget()
        mailRefresh.place_forget()
        subjectLabel.place_forget()
        subjectEntry.place_forget()

    def showView():
        mailForgetAll()
        showMail.place(relx=.22, rely=.3)
        mailNum.place(relx=.22, rely=.1)
        mailRefresh.place(relx=.75, rely=.15)

    def showWrite():
        mailForgetAll()
        fromAddrLabel.place(relx=.22, rely=.1)
        fromAddrEntry.place(relx=.32, rely=.1)
        toAddrLabel.place(relx=.22, rely=.2)
        toAddrEntry.place(relx=.32, rely=.2)
        writeMail.place(relx=.22, rely=.4)
        sendButton.place(relx=.75, rely=.15)
        subjectLabel.place(relx=.22, rely=.3)
        subjectEntry.place(relx=.32, rely=.3)

    ttk.Button(frame, text="查邮件", width=8, command=showView).place(relx=.02, rely=.1)
    ttk.Button(frame, text="写邮件", width=8, command=showWrite).place(relx=.02, rely=.2)
    ttk.Button(
        frame, text="帮助",
        command=lambda: messagebox.showinfo(title="提示信息", message="记得配置邮箱和授权码!\n"
                                                                      "只能查看最近5封邮件，可以自己改代码，\n"
                                                                      "以实现查看多封。\n"
                                                                      "要使用发信功能得配置邮箱授权码。\n"
                                                                      "<To>可以添加多个邮箱地址，以半角逗号分开。\n"
                                                                      "<主题>可不填"),
        width=8
    ).place(relx=.9, rely=.8)


aboutList = ["我是编程路上一个蹒跚学步的婴儿",
             "我是Python新手村的新人",
             "我是学不进Java的废材",
             "我是一个喜欢花里胡哨的普通人",
             "这个程序是我用来练习和进步的",
             "谢谢你的见证！"]


def authorInfor(frame):
    ttk.Label(frame, text="关于作者-Pfolg").place(relx=.02, rely=.02)

    def showLabel():
        i = 0
        while True:
            if i == len(aboutList):
                i = 0
            try:
                a = ttk.Label(frame, text=aboutList[i], font=("微软雅黑", 16), width=40)
                a.place(relx=.3, rely=.1)
            except RuntimeError:
                break
            i += 1
            time.sleep(3)

    # 开辟一个线程使事件循环，建议关闭（注释掉）
    threading.Thread(target=showLabel).start()

    ttk.Button(
        frame, text="Bilibili",
        command=lambda: os.system("start https://space.bilibili.com/515553532")
    ).place(relx=.2, rely=.5)

    ttk.Button(
        frame, text="GitHub",
        command=lambda: os.system("start https://github.com/Pfolg")
    ).place(relx=.3, rely=.6)

    ttk.Button(
        frame, text="CSDN",
        command=lambda: os.system("start https://blog.csdn.net/qq_46603846?spm=1010.2135.3001.5421")
    ).place(relx=.4, rely=.7)

    ttk.Button(
        frame, text="作者的个人网站",
        command=lambda: messagebox.showinfo(title="提示信息", message="作者的个人网站早在24年6月崩啦！")
    ).place(relx=.5, rely=.6)

    ttk.Button(
        frame, text="QQ&微信",
        command=None
    ).place(relx=.6, rely=.5)


def openFile(path=".\\README.md"):
    kk = threading.Thread(target=lambda: os.system(path))
    kk.start()
    kk = None


def beautifulSentence(frame, w):
    while True:
        # 获取首页美文内容
        try:
            with open(".\\setting\\Setting-APIuse.txt", 'r', encoding="utf-8") as file:
                listSentence = file.readlines()
        except FileNotFoundError:
            listSentence = ""

        try:
            if listSentence:
                newList = [s.rstrip('\r\t\n') for s in listSentence]
                sentence = newList[random.randint(0, len(newList) - 1)]
            else:
                url = "https://tenapi.cn/v2/yiyan"
                content = requests.get(url)
                sentence = content.text
        except BaseException:
            sentence = ""
        try:
            ttk.Label(frame, text="    " + sentence, font=("微软雅黑", 10), background="#f0d2dd",
                      compound="center", width=w, foreground="#706b67"
                      ).place(relx=0, rely=.02, height=70)
        except RuntimeError:
            sys.exit()
        # 30秒刷新一次，多了会被网站列入黑名单
        time.sleep(30)


def basicFrame0(w, h, window):
    # 初始窗口
    frame0 = ttk.Frame(window)
    frame0.place(relx=0, rely=0, width=w, height=h)
    ttk.Label(frame0, width=w, background="#f0d2dd", compound="center").place(relx=0, rely=.02, height=70)
    threading.Thread(target=lambda: beautifulSentence(frame0, w)).start()

    # 显示天气
    openWeather(frame0)

    # 获取本地时间并对机主问好
    def get_time():
        time2 = time.strftime('%Y-%m-%d %H:%M:%S')
        clock = ttk.Label(frame0, text=time2, font=10, foreground="#000000")
        time3 = int(time.strftime("%H"))
        if 0 <= time3 < 6:
            text = "凌晨好!"
        elif time3 < 12:
            text = "上午好!"
        elif time3 < 18:
            text = "下午好!"
        else:
            text = "晚上好!"
        clock.place(relx=.01, rely=.95)
        # 获取当前登录的用户名称
        userName = win32com.client.Dispatch('WScript.Network').UserName
        ttk.Label(frame0, text=f"{text} {userName}", foreground="#000000").place(relx=.25, rely=.95)
        clock.after(1000, get_time)  # 1000ms=1s

    # frame切换
    def convertFrame(f1, f2):
        f1.place_forget()
        f2.place(relx=0, rely=0, width=w, height=h)

    def buttons(targetFrame: ttk.Frame, text: str, rx, ry, width=16):
        ttk.Button(frame0, text=text, width=width,
                   command=lambda: convertFrame(frame0, targetFrame)).place(relx=rx, rely=ry)  # 进入该frame的按钮
        ttk.Button(targetFrame, width=8, text='返回',
                   command=lambda: convertFrame(targetFrame, frame0)).place(relx=.9, rely=.9)

    # 产生frame框架
    frameMakeFiles = ttk.Frame(window)
    frameMusicPlayer = ttk.Frame(window)
    frameQR = ttk.Frame(window)
    frameRandomName = ttk.Frame(window)
    framePythonPackage = ttk.Frame(window)
    frameKeyWord = ttk.Frame(window)
    frameWin = ttk.Frame(window)
    frameClick = ttk.Frame(window)
    frameMail = ttk.Frame(window)
    frameLonLat = ttk.Frame(window)
    frameFT = ttk.Frame(window)
    frameBlindWaterMark = ttk.Frame(window)
    frameMoneyConvert = ttk.Frame(window)
    framePassword = ttk.Frame(window)
    frameWiFi = ttk.Frame(window)
    frameM = ttk.Frame(window)

    # 最多34个，不能再多了，多了就要重构一下了
    # 由于循环的关系，每隔5个按钮就会跳过一个
    dictFrame = {
        "批量创建": frameMakeFiles,
        "音乐播放器": frameMusicPlayer,
        "二维码生成器": frameQR,
        "随机点名": frameRandomName,
        "Python第三方库工具": framePythonPackage,

        "Bug-1": 1,

        "PDF关键词分析": frameKeyWord,
        "电脑功能": frameWin,
        "自动点击": frameClick,
        "邮件": frameMail,
        "中国经纬度": frameLonLat,

        "Bug-2": 2,

        "文本翻译": frameFT,
        "盲水印工具": frameBlindWaterMark,
        "货币转换器": frameMoneyConvert,
        "密码生成": framePassword,
        "WiFi": frameWiFi,

        "Bug-3": 3,

        "二刺猿": frameM,

    }

    "主功能设定"
    # 批量创建文件（文件夹）
    makeFilesPhot(frameMakeFiles)
    # 音乐播放器
    musicPlayer(frameMusicPlayer)
    # 二维码生成器
    QRCodeMaker(frameQR)
    # 随机点名
    randomName(frameRandomName)
    # Python第三方库
    ThirdPackage(framePythonPackage)
    # 关键词分析
    analysisWindow(frameKeyWord)
    # 电脑功能
    winFunction(frameWin)
    # 自动点击
    singleDouble(frameClick)
    # 邮件
    mainMail(frameMail)
    # 经纬度
    flFrame(frameLonLat)
    # 文本翻译
    translateFrame(frameFT)
    # 盲水印
    getFileFrame(frameBlindWaterMark)
    # 货币转换
    moneyConvert(frameMoneyConvert)
    # 密码生成
    keyFrame(framePassword)
    # WiFi
    wifiFrame(frameWiFi)
    # 二刺猿
    tdFrame(frameM)

    # 5行7列
    i = 0
    j = 2
    for key in dictFrame:
        if i < 5:
            if j < 9:
                buttons(dictFrame.get(key), key, 0.02 + (i * 2 / 10), j / 10)
                i += 1
            else:
                break
        else:
            i = 0
            j += 1

    # 设置
    frame_setting = ttk.Frame(window)
    frameSetting(frame_setting)
    buttons(frame_setting, "设置", .9, .9, 8)

    # 其他功能(私有功能)
    frameOtherFunctions = ttk.Frame(window)
    otherFunction(frameOtherFunctions)
    buttons(frameOtherFunctions, "其他功能", .82, .8)

    frameAuthor = ttk.Frame(window)
    authorInfor(frameAuthor)
    buttons(frameAuthor, "关于作者", .65, .9, 8)

    frameLICENSE = ttk.Frame(window)
    readLICENSE(frameLICENSE)
    buttons(frameLICENSE, "LICENSE", .54, .9, 8)

    ttk.Button(frame0, text="关于ToolsBox", command=openFile).place(relx=.76, rely=.9)

    get_time()


def drawName(canva, info="ToolsBox"):
    theScreen = turtle.TurtleScreen(canva)
    path = turtle.RawTurtle(theScreen)
    path.hideturtle()
    path.penup()
    path.fd(-300)
    path.pencolor("#f0d2dd")
    for i in info:
        path.write(i, font=('微软雅黑', 40, 'bold'))
        path.fd(80)
    time.sleep(1)


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ToolsBox")
    screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
    w, h = int(screen_w / 2), int(screen_h / 2)
    window.geometry(f'{w}x{h}+{int(screen_w / 4)}+{int(screen_h / 4)}')
    window.resizable(False, False)
    window.iconbitmap(".\\resource\\ico.ico")
    window.attributes('-alpha', 0.9)

    # 启动动画（fake
    # 你说我可不可以拿这个接广子
    canva = tk.Canvas(window, width=w, height=h)
    canva.pack()
    drawName(canva)
    canva.pack_forget()

    basicFrame0(w, h, window)

    window.mainloop()
