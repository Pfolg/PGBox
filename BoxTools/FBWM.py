# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   FBWM |User    Pfolg
# 2024/7/28   3:23
import time
from blind_watermark import WaterMark
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


#  仅供admin使用
# 执行
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


def find_files(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.delete(0, 'end')
    x.insert(0, file_path)
    win.destroy()


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

    def forgetAll():
        for i in [l1, l2, l3, b1, b2, b3, e1, e2, e4, s1]:
            i.place_forget()

    def showBut(f):
        forgetAll()
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


if __name__ == '__main__':
    pass
