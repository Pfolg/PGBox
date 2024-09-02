# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   moneyConvert |User    Pfolg
# 2024/7/28   20:41
import os
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
import re

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

    ttk.Button(
        frame, text="web 打开货币转换工具", command=lambda: os.system(f"start {moneyUrl}")
    ).place(relx=.42, rely=.9)

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
        frame, text="Converter", command=lambda: conMon(sbox.get(), tbox.get(), num.get())
    ).place(relx=.44, rely=.5)
