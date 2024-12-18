# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   frame0 |User    Pfolg
# 2024/7/20   13:23
import json
import os
import random
import tkinter
import requests
import threading
import time
from tkinter import ttk
import win32com.client
import webbrowser
import urllib.parse
from BoxTools import makeFilesPhot, musicPlayer, QRCodeMaker, randomName, ThirdPackage, keyWordsAnalysis, FrameWin, \
    singleDouble, BoxMails, findLocation, frameTranslate, FBWM, FrameSetting, moneyConvert, makeKey, \
    frameEntertainment, openWeather, aboutPG, frameString

globalColor = "#c7dddd"
listSentence = ""


def findSentencesFile():
    global listSentence
    if os.path.exists(".\\setting\\Setting-APIuse.txt"):
        with open(".\\setting\\Setting-APIuse.txt", 'r', encoding="utf-8") as file:
            listSentence = file.readlines()
            # print(listSentence)


threading.Thread(target=findSentencesFile).start()
# def openFile(path=".\\README.md"):


#     kk = threading.Thread(target=lambda: os.system(path))
#     kk.start()
#     kk = None


browsers = {
    # 有些链接可能失效，请自行更新
    "google": "https://www.google.com/search?q={}",
    "bing": "https://www.bing.com/search?q={}",
    "duckduckgo": "https://duckduckgo.com/?q={}",
    "baidu": "https://www.baidu.com/s?wd={}",
    "yahoo": "https://search.yahoo.com/search?p={}",
    "yandex": "https://yandex.ru/search/?text={}",
    "blekko": "https://www.blekko.com/?q={}",
    "ecosia": "https://www.ecosia.org/search?q={}",
    "lycos": "https://www.lycos.com/search?q={}",
    "searx": "https://searx.me/?q={}",
    "swisscows": "https://swisscows.com/search?q={}",
    "sogou": "https://www.sogou.com/web?query={}",
    "bing_china": "https://cn.bing.com/search?q={}",
}


def findBrowser():
    global browser
    try:
        browserFile = open(".\\setting\\Config.json", "r", encoding="utf-8")
        brDict = json.load(browserFile)
        browser = brDict.get("browser")
        browserFile.close()
        if not browser:
            browser = "bing"
    except BaseException:
        browser = "bing"

    return browser


threading.Thread(target=findBrowser).start()


def search_in_browser(query):
    broUrl = browsers.get(browser)
    # 使用bing搜索指定的查询
    search_url = broUrl.format(urllib.parse.quote(query))

    # 打开默认浏览器并导航到搜索URL
    webbrowser.open_new_tab(search_url)


def basicFrame0(w, h, window):
    userName = win32com.client.Dispatch('WScript.Network').UserName
    # 初始窗口
    frame0 = ttk.Frame(window)
    frame0.place(relx=0, rely=0, width=w, height=h)

    urlContent = tkinter.StringVar()

    def on_enter(e):
        search_in_browser(urlContent.get())

    uc_enter = ttk.Entry(frame0, width=60, textvariable=urlContent)
    uc_enter.place(relx=.2, rely=.2)
    ttk.Label(frame0, text=browser, background="#61afef", foreground="#ffffff").place(relx=.1, rely=.2)
    ttk.Button(
        frame0, text="🔍 Search...", width=10, command=lambda: search_in_browser(urlContent.get())
    ).place(relx=.8, rely=.2)
    uc_enter.bind('<Return>', on_enter)
    ttk.Label(frame0, width=w, background=globalColor, compound="center").place(relx=0, rely=.02, height=70)

    # def beautifulSentence():
    #     # 获取首页美文内容
    #     try:
    #         with open(".\\setting\\Setting-APIuse.txt", 'r', encoding="utf-8") as file:
    #             listSentence = file.readlines()
    #             print(listSentence)
    #     except BaseException:
    #         listSentence = ""
    #
    #         if listSentence:
    #             newList = [s.rstrip() for s in listSentence]
    #             try:
    #                 sentence.set(f"    {newList[random.randint(a=0, b=(len(newList) - 1))]}")
    #             except BaseException:
    #                 print("error")
    #             # print(var.get())
    #         else:
    #             "WAY1"
    #             # url = "https://v1.hitokoto.cn/"
    #             # content = requests.get(url)
    #             # sentence.set("    " + eval(content.text).get("hitokoto"))
    #             # print(eval(content.text).get("hitokoto"))
    #
    #             "WAY2"
    #             url = "https://tenapi.cn/v2/yiyan"
    #             content = requests.get(url)
    #             try:
    #                 sentence.set(f"    {content.text}")
    #             except BaseException:
    #                 print("error")
    #                 # print(content.text)
    #                 sentence.set("    Can't show sentence, please check your network or the Setting file...")
    #     # 30秒刷新一次，多了会被网站列入黑名单
    #     window.after(30000, beautifulSentence)

    def headSentence():
        if listSentence:
            sentence = listSentence[random.randint(a=0, b=(len(listSentence) - 1))].strip()
        else:
            try:
                "WAY1"
                # url = "https://v1.hitokoto.cn/"
                # content = requests.get(url)
                # sentence.set("    " + eval(content.text).get("hitokoto"))
                # print(eval(content.text).get("hitokoto"))

                "WAY2"
                url = "https://tenapi.cn/v2/yiyan"
                content = requests.get(url)
                sentence = content.text
            except BaseException:
                sentence = "啊咧！获取不了美句，检查一下设置或网络连接状态哦！"
        # 打印一下sentence
        print(sentence)

        # 设定标签
        beautifulSentence = ttk.Label(
            frame0, text=sentence, font=("微软雅黑", 10), background=globalColor,
            compound="center", width=w, foreground="#706b67"
        )
        beautifulSentence.place(relx=.03, rely=.02, height=70)
        # 30秒更新一次，多了会被网站列入黑名单
        if len(sentence) > 50:
            beautifulSentence.after(0, headSentence)
        else:
            beautifulSentence.after(30000, headSentence)

    # 显示天气
    openWeather.openWeather(frame0)

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
        ttk.Label(frame0, text=f"{text} {userName}", foreground="#000000").place(relx=.25, rely=.95)
        clock.after(1000, get_time)  # 1000ms=1s

    # frame切换
    def convertFrame(f1, f2):
        f1.place_forget()
        f2.place(relx=0, rely=0, width=w, height=h)

    def buttons(targetFrame: ttk.Frame, text: str, rx, ry, width=16):
        ttk.Button(
            frame0, text=text, width=width,
            command=lambda: convertFrame(frame0, targetFrame)
        ).place(relx=rx, rely=ry)  # 进入该frame的按钮
        ttk.Button(
            targetFrame, width=8, text='返回',
            command=lambda: convertFrame(targetFrame, frame0)
        ).place(relx=.9, rely=.9)

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
    frameM = ttk.Frame(window)
    frameStr = ttk.Frame(window)

    # 最多34个，不能再多了，多了就要重构一下了
    # 由于循环的关系，每隔5个按钮就会跳过一个
    dictFrame = {
        "批量创建": frameMakeFiles,
        "音乐播放器": frameMusicPlayer,
        "二维码": frameQR,
        "随机点名": frameRandomName,
        "Python第三方库工具": framePythonPackage,

        "Bug-1": 1,

        "PDF关键词分析": frameKeyWord,
        "电脑功能(Win11)": frameWin,
        "自动点击": frameClick,
        "邮件": frameMail,
        "中国经纬度": frameLonLat,

        "Bug-2": 2,

        "文本翻译": frameFT,
        "盲水印工具": frameBlindWaterMark,
        "货币转换器": frameMoneyConvert,
        "密码生成": framePassword,
        "字符串运算": frameStr,

        "Bug-3": 3,

        "Entertainment": frameM,

    }

    "主功能设定"
    # 批量创建文件（文件夹）
    makeFilesPhot.makeFilesPhot(frameMakeFiles)
    # 音乐播放器
    musicPlayer.musicPlayer(frameMusicPlayer)
    # 二维码生成器
    QRCodeMaker.QRCodeMaker(frameQR)
    # 随机点名
    randomName.randomName(frameRandomName)
    # Python第三方库
    ThirdPackage.ThirdPackage(framePythonPackage)
    # 关键词分析
    keyWordsAnalysis.analysisWindow(frameKeyWord)
    # 电脑功能
    FrameWin.winFunction(frameWin)
    # 自动点击
    singleDouble.singleDouble(frameClick)
    # 邮件
    BoxMails.mainMail(frameMail)
    # 经纬度
    findLocation.flFrame(frameLonLat)
    # 文本翻译
    frameTranslate.translateFrame(frameFT)
    # 盲水印
    FBWM.getFileFrame(frameBlindWaterMark)
    # 货币转换
    moneyConvert.moneyConvert(frameMoneyConvert)
    # 密码生成
    makeKey.keyFrame(framePassword)
    # 二刺猿
    frameEntertainment.EntertainmentFrame(frameM)
    # 字符串运算
    frameString.frameString(frameStr)

    # 4行7列
    i = 0
    j = 3
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
    frameSetting = ttk.Frame(window)
    FrameSetting.frameSetting(frameSetting)
    buttons(frameSetting, "设置", .9, .9, 8)

    # 其他功能(私有功能)
    # frameOtherFunctions = ttk.Frame(window)
    # otherFunction.otherFunction(frameOtherFunctions)
    # buttons(frameOtherFunctions, "其他功能", .82, .8)

    # frameAuthor = ttk.Frame(window)
    # authorInfor.authorInfor(frameAuthor)
    # buttons(frameAuthor, "关于作者", .65, .9, 8)
    #
    # frameLICENSE = ttk.Frame(window)
    # readLICENSE.readLICENSE(frameLICENSE)
    # buttons(frameLICENSE, "LICENSE", .54, .9, 8)
    #
    # ttk.Button(frame0, text="关于PGBox", command=openFile).place(relx=.76, rely=.9)

    frameAbout = ttk.Frame(window)
    aboutPG.PGAbout(frameAbout)
    buttons(frameAbout, "关于", .8, .9, 8)

    threading.Thread(target=headSentence, daemon=True).start()
    threading.Thread(target=get_time, daemon=True).start()
    # headSentence()
    # get_time()
