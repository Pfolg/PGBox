# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   frameTranslate |User    Pfolg
# 2024/7/27   23:24
from translate import Translator
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import pyperclip

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
