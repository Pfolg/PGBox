# -*- coding: utf-8 -*-
import sys
import time
import tkinter as tk
import qrcode as cd
import tkinter.messagebox as tkm
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image
from tkinter import filedialog
from pyzbar.pyzbar import decode
import cv2


def QRCodeMaker(frame):
    # 生成二维码
    def main_pro(txt, l2, l1, gl):
        print("a", txt, "a")
        if (not txt) or txt == "\n":
            tkm.showwarning(title="提示信息", message="您不能什么也不输入，否则这个二维码将没有意义。")
        else:
            try:
                code = cd.QRCode(
                    version=1,
                    error_correction=cd.constants.ERROR_CORRECT_H,  # 容错率为高
                    box_size=10,
                    border=4,
                )
            except UnicodeEncodeError:
                tkm.showwarning(title='UnicodeEncodeError',
                                message=f'UnicodeEncodeError: '
                                        f'\n\'latin-1\' codec can\'t encode characters in position 0-{len(txt)}'
                                        f'\nClick \"确定\" and QUIT')
                sys.exit()
            try:
                code.add_data(txt)
                code.make(fit=True)
                code_img = code.make_image(fill_color=l2, back_color=l1)
            except ValueError:
                tkm.showwarning(title='ValueError',
                                message=f'ValueError: \n'
                                        f'unknown color specifier: {l2} or {l1}\n'
                                        f'Click \"确定\" and QUIT')
                return
            # show()
            code_size_w, code_size_h = code_img.size
            ratio = 6
            if gl == '':
                pass
            else:  # 粘贴图片
                logo = Image.open(gl)
                logo_w, logo_h = int(code_size_w / ratio), int(code_size_h / ratio)
                icon = logo.resize(
                    (logo_w, logo_h),
                    5)  # Use Image.Resampling.NEAREST (0), Image.Resampling.LANCZOS (1),
                # Image.Resampling.BILINEAR (2), Image.Resampling.BICUBIC (3), Image.Resampling.BOX (4) or
                # Image.Resampling.HAMMING (5)
                x, y = int((code_size_w - logo_w) / 2), int((code_size_h - logo_h) / 2)
                code_img.paste(icon, (x, y))
            time.sleep(2)
            code_img.show()
            # tkm.showinfo(message='二维码已生成，请在程序所在目录查找\n\"code.png\"', title='提示信息')
            # with open('.\\code.png', 'wb') as file:
            #     code_img.save(file)
            print('Done')

    def part1():
        print('Loading......')
        a, b, c, d = inputBox.get("1.0", "end").strip(), choose_color2.get(), choose_color1.get(), get_logo.get()
        main_pro(a, b, c, d)

    def part0():
        main_label = ttk.Label(
            frame, text='二维码生成',
            font=(r'C:\Windows\Fonts\msyh.ttc', 20), background="#b3baba",
            compound='center')
        main_label.place(relx=0.5, rely=0.05, anchor='center')

    def find_picture(x):
        win = tk.Tk()
        win.withdraw()
        file_path = filedialog.askopenfilename()
        x.set(file_path)
        win.destroy()

    part0()
    # 标签
    ttk.Label(
        frame,
        text='输入内容',
        font=(r'C:\Windows\Fonts\msyh.ttc', 15),
        compound='center'
    ).place(relx=0.05, rely=0.2)
    # 输入框
    # url = tk.StringVar()
    # input_ing = ttk.Entry(frame, width=30, textvariable=url)
    # input_ing.delete(0, 0)
    # # input_ing.insert(0, "默认文本...")
    # input_ing.place(relx=0.35, rely=0.2)
    inputBox = ScrolledText(frame, width=50, height=8)
    inputBox.place(relx=.05, rely=.3)

    # 背景颜色
    choose_color1 = tk.StringVar()
    choose_color1.set('#FFFFFF')
    cc1 = ttk.Entry(frame, width=10, textvariable=choose_color1)
    cc1.place(relx=0.8, rely=0.2)

    ttk.Label(
        frame,
        text='背景颜色',
        font=(r'C:\Windows\Fonts\msyh.ttc', 15),
        compound='center').place(relx=0.65, rely=0.2)

    # 前景颜色
    choose_color2 = tk.StringVar()
    choose_color2.set('#000000')
    cc2 = ttk.Entry(frame, width=10, textvariable=choose_color2)
    cc2.place(relx=0.8, rely=0.3)

    ttk.Label(
        frame,
        text='前景颜色',
        font=(r'C:\Windows\Fonts\msyh.ttc', 15),
        compound='center').place(relx=0.65, rely=0.3)

    # 获取中部图片
    ttk.Label(
        frame,
        text='LOGO',
        font=(r'C:\Windows\Fonts\msyh.ttc', 15),
        compound='center').place(relx=0.65, rely=0.4)
    get_logo = tk.StringVar()
    tl = ttk.Entry(frame, width=15, textvariable=get_logo)
    # tl.delete(0, 'end')
    # tl.insert(0, '*.png')
    tl.place(relx=0.75, rely=0.4)

    ttk.Button(
        frame,
        text='生成',
        width=7,
        compound='center',
        command=part1).place(relx=0.75, rely=0.5)
    # 把部件贴上去

    ttk.Button(
        frame,
        text='导入',
        width=7,
        compound='top',
        command=lambda: find_picture(get_logo)).place(relx=0.65, rely=0.5)

    # 二维码识别
    sBox = ScrolledText(frame, width=30, height=5, state="disabled")
    sBox.place(relx=.4, rely=.65)

    def recognizeCode(x):
        sBox.config(state="normal")
        if x:
            try:
                # 读取图像文件
                image = cv2.imread(x)

                # 使用pyzbar库识别图像中的二维码
                decoded_objects = decode(image)
                print(decoded_objects)

                # 打印识别到的数据
                for obj in decoded_objects:
                    # print('Type:', obj.type)
                    # print('Data:', obj.data.decode('utf-8'))
                    sBox.insert(tk.END, obj.data.decode('utf-8') + "\n")
                if not decoded_objects:
                    sBox.insert(tk.END, "识别失败\n")
            except BaseException:
                sBox.insert(tk.END, "识别失败\n")
        sBox.config(state="disabled")

    def clearsBox():
        sBox.config(state="normal")
        sBox.delete(1.0, "end")
        sBox.config(state="disabled")

    ttk.Label(
        frame, text="识别二维码", font=(r'C:\Windows\Fonts\msyh.ttc', 15),
        background="#b3baba"
    ).place(relx=.1, rely=.6)

    codePath = tk.StringVar()

    ttk.Entry(frame, textvariable=codePath, width=16).place(relx=.1, rely=.7)
    ttk.Button(frame, text="选择", width=8, command=lambda: find_picture(codePath)).place(relx=.26, rely=.698)
    ttk.Button(
        frame, text="识别", width=8, command=lambda: recognizeCode(codePath.get())
    ).place(relx=.1, rely=.8)

    tk.Button(
        frame, width=5, text="Clear", command=clearsBox
    ).place(relx=.63, rely=.82)
