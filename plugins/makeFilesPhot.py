import os
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


def create_files(name, content):
    with open(name, 'w', encoding='utf-8') as file:
        file.write(content)


def create():
    # print('***批量创建文件(文件夹)***\n')
    # print('注意:此程序在创建文件方面有一定的局限性!\n')
    try:
        while True:
            path = v_path.get()
            if not path:
                tk.messagebox.showerror(title='Error!', message='请输入工作路径')
                return False
            else:
                break
        os.chdir(path)
    except FileNotFoundError:
        tk.messagebox.showinfo(title='Infor', message='找不到该目录，将创建一个新目录')
        os.mkdir(path)
    except OSError:
        return False
    finally:
        os.chdir(path)
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


if __name__ == '__main__':
    pass
