import pdfplumber
import pyecharts.options as opts
from pyecharts.charts import WordCloud
import jieba
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

study_url = 'https://gallery.pyecharts.org/#/WordCloud/basic_wordcloud'

information = ("特殊的PDF文件，如图片生成的PDF不可读取;\n"
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


def find_files(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.delete(0, 'end')
    x.insert(0, file_path)
    win.destroy()


def analysisWindow(frame):
    ttk.Label(frame, text="PDF关键词分析").place(relx=.03, rely=0)

    filePath = tk.StringVar()
    ttk.Label(frame, text="请选择PDF文件", font=("微软雅黑", 20)).place(relx=.35, rely=.2)
    file = ttk.Entry(frame, textvariable=filePath, width=40)
    file.place(relx=.3, rely=.4)
    ttk.Button(frame, text="选择", command=lambda: find_files(file)).place(relx=.6, rely=.398)
    ttk.Button(frame, text="开始", command=lambda: analysis(filePath.get())).place(relx=.43, rely=.6)

    ttk.Button(frame, text="帮助", command=lambda: messagebox.showinfo(title="帮助", message=information),
               width=8).place(relx=.8, rely=.9)
