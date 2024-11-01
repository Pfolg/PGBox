# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   openWeather |User    Pfolg
# 2024/7/31   23:58
from tkinter import ttk
import requests
import json


def openWeather(frame):
    try:
        with open(".\\setting\\Config.json", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            city = myDict.get("city")
            opwAPI = myDict.get("openweatherAPI")
            if city and opwAPI:
                pass  # 如果没有城市和API就终止函数
            else:
                return
    except BaseException:
        return
    language = 'zh_cn'  # 简体中文  &lang={language}

    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={opwAPI}&lang={language}'

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
    except BaseException:
        return


if __name__ == '__main__':
    pass
