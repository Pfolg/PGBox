# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   NirCmd-Gui-Chinese |User    Pfolg
# 2024/10/11 11:42
# 基于nircmd v2.87
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
import subprocess

url = "http://nircmd.nirsoft.net/"
defaultFont = ("Segoe UI", 10)
"请将这个程序与nircmd.exe放到同一父目录下，或者将nircmd.exe添加到环境变量"


# path = r"D:\PycharmProjects\pythonProject\Practice_project\NirCmd-Chinese\nircmd.exe"
def setConfig():
    try:
        with open(".\\setting\\Config.json", "r", encoding="utf-8") as setFile:
            setDict = json.load(setFile)
            p = setDict.get("nircmd_path")
            return p
    except BaseException:
        messagebox.showerror("NirCmd-Gui-Chinese", "无法获取nircmd.exe的路径！")
        return None


path = setConfig()


def MakeSetting(key, p):
    with open(".\\setting\\Config.json", "r", encoding="utf-8") as setfile:
        setDict = json.load(setfile)
    setDict[key] = p
    try:
        with open(".\\setting\\Config.json", "w", encoding="utf-8") as setFile:
            json.dump(setDict, setFile, ensure_ascii=False, indent=4)
    except BaseException:
        messagebox.showerror("写入失败", "写入失败！")  # 完美的代码是不会执行这一步的


def find_files(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.set(file_path)
    win.destroy()


def find_directory(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askdirectory()
    x.set(file_path)
    win.destroy()


# 复用率最高的函数！！！
def SecondRun(args=None, program=path, timeout=None):
    if not args:
        args = []
    if program:
        threading.Thread(target=lambda: subprocess.run([program] + args, timeout=timeout)).start()
    else:
        messagebox.showerror("路径错误！", "请先指定NirCmd.exe的路径！")


# 默认
funcTab1_1 = {
    "蜂鸣声": lambda: SecondRun(args=["beep", "500", "2000"]),
    "标准蜂鸣声": lambda: SecondRun(["stdbeep"]),
    "终止关机": lambda: SecondRun(args=["abortshutdown"]),
    "清空回收站": lambda: SecondRun(args=["emptybin"]),
    "重启": lambda: SecondRun(args=["exitwin", "reboot"]),
    "注销": lambda: SecondRun(["exitwin", "logoff"]),
    "PowerOff": lambda: SecondRun(["exitwin", "poweroff"]),
    "简单关机": lambda: SecondRun(["exitwin", "shutdown"]),
    "在60秒内关闭系统": lambda: SecondRun(
        ["initshutdown", "Shut down the system within 60 seconds", "60", "reboot"]),
    "锁定": lambda: SecondRun(["lockws"]),
    "重启资源管理器1": lambda: os.system("taskkill /f /im explorer.exe && start explorer.exe"),
    "重启资源管理器2": lambda: SecondRun(["restartexplorer"]),
    "屏幕保护程序": lambda: SecondRun(["screensaver"]),

}

# 声音
funcTab1_2 = {
    # changeappvolume iexplore.exe -0.2
    # changeappvolume wmplayer.exe 0.55 Speakers
    # changeappvolume /1275 -0.25 1
    # changeappvolume Firefox.exe 0.5
    "音量+2": lambda: SecondRun(["changesysvolume", "2000"]),
    "音量-2": lambda: SecondRun(["changesysvolume", "-2000"]),
    # Similar to changesysvolume, but instead of changing the whole sound volume, changesysvolume2 changes the left
    # channel and the right channel separately. Examples: changesysvolume2 1000 -1000 changesysvolume2 -3000 0
    # changesysvolume2 0 -5000 waveout changesysvolume2 -3000 0 master 1
    "左音+2，右音-2": lambda: SecondRun(["changesysvolume2", "2000", "-2000"]),
    "左音-2，右音+2": lambda: SecondRun(["changesysvolume2", "-2000", "2000"]),
    "重置左右声道": lambda: SecondRun(["setvolume", "0", "0", "0"]),  # http://nircmd.nirsoft.net/setvolume.html
    # https://zh.101-help.com/7263afc0c3-windows-10zhong-left-and-right-channel-adjust-audio-balance/
}
# 显示
funcTab1_3 = {
    "增加亮度": lambda: SecondRun(["changebrightness", "10"]),
    "减小亮度": lambda: SecondRun(["changebrightness", "-10"]),
    "关闭显示器": lambda: SecondRun(["monitor", "off"]),
    "关闭显示器2": lambda: SecondRun(["monitor", "async_off"]),
    "60秒后关闭显示器": lambda: SecondRun(["cmdwait", "60000", "monitor", "off"]),
    "显示器低功耗": lambda: SecondRun(["monitor", "low"]),
}

# 粘贴板
funcTab1_4 = {
    "清除粘贴板": lambda: SecondRun(["clipboard", "clear"]),
    "打开Windows粘贴板": lambda: messagebox.showinfo("clipboard", "按win键+V键，即可呼出Windows粘贴板"),
    "其他": lambda: messagebox.showinfo(
        "clipboard", (
            "set - 将指定文本设置到剪贴板。\n"
            "readfile - 将指定文本文件的内容设置到剪贴板。\n"
            "clear - 清除剪贴板。\n"
            "writefile - 将剪贴板的内容写入到文件。（仅文本）\n"
            "writeufile - 将剪贴板的内容写入到Unicode文件。（仅文本）\n"
            "addfile - 将剪贴板的内容添加到文件。（仅文本）\n"
            "addufile - 将剪贴板的内容添加到Unicode文件。（仅文本）\n"
            "saveimage - 将剪贴板中的当前图像保存到文件。\n"
            "copyimage - 将指定图像文件的内容复制到剪贴板。\n"
            "saveclp - 将当前剪贴板数据保存到Windows .clp文件。\n"
            "loadclp - 将Windows .clp文件加载到剪贴板。")

    ),

    # set - 将指定文本设置到剪贴板。
    # readfile - 将指定文本文件的内容设置到剪贴板。
    # clear - 清除剪贴板。
    # writefile - 将剪贴板的内容写入到文件。（仅文本）
    # writeufile - 将剪贴板的内容写入到Unicode文件。（仅文本）
    # addfile - 将剪贴板的内容添加到文件。（仅文本）
    # addufile - 将剪贴板的内容添加到Unicode文件。（仅文本）
    # saveimage - 将剪贴板中的当前图像保存到文件。
    # copyimage - 将指定图像文件的内容复制到剪贴板。
    # saveclp - 将当前剪贴板数据保存到Windows .clp文件。
    # loadclp - 将Windows .clp文件加载到剪贴板。
}


# VIP程序专属！复制一个文件的创建/修改/访问时间到一个或多个文件。
def funcTab1_5(tab1_5_func):
    # 标签
    ttk.Label(tab1_5_func, text=(
        "复制一个文件的创建/修改/访问时间到一个或多个文件。创建/修改/访问时间是从 [源文件名] 参数指定的文件中获取，并设置到 [通配符] 参数指定的文件或通配符匹配的文件中。\n"
        "示例：\n"
        "clonefiletime \"c:\\temp\\file1.txt\" \"c:\\files\\*.txt\"\n"
        "clonefiletime \"c:\\temp\\file1.txt\" \"c:\\temp\\file2.txt\"\n\n"
        "Clone the Created / Modified / Accessed time of one file into one or more files.\n"
        "The Created / Modified / Accessed time is taken from the file specified in[source filename] parameter\n"
        "and set into the file or wildcard specified in[Wildcard] parameter.\n"
        "Examples:\n"
        "clonefiletime \"c:\\temp\\file1.txt\" \"c:\\files\\*.txt\"\n"
        "clonefiletime \"c:\\temp\\file1.txt\" \"c:\\temp\\file2.txt\"\n"
    )).place(relx=.02, rely=.02)
    # 控件
    originFileT5F, targetFileT5F = tk.StringVar(), tk.StringVar()

    ttk.Label(tab1_5_func, text="源文件路径").place(relx=.1, rely=.5)
    tk.Entry(tab1_5_func, textvariable=originFileT5F).place(relx=.1, rely=.6)
    ttk.Button(tab1_5_func, text="浏览", width=8, command=lambda: find_files(originFileT5F)).place(relx=.3, rely=.6)

    ttk.Label(tab1_5_func, text="目标文件路径").place(relx=.5, rely=.5)
    tk.Entry(tab1_5_func, textvariable=targetFileT5F).place(relx=.5, rely=.6)
    ttk.Button(tab1_5_func, text="浏览", width=8, command=lambda: find_files(targetFileT5F)).place(relx=.7, rely=.6)

    def clonefiletime(x, y):
        if x and y:
            SecondRun(["clonefiletime", x, y])
        else:
            messagebox.showerror("Error", "请指定文件路径")

    ttk.Button(
        tab1_5_func, text="导出", width=8,
        command=lambda: clonefiletime(originFileT5F.get(), targetFileT5F.get())
    ).place(relx=.8, rely=.8)


# 朗读
def funcTab1_6(frame):
    t6_font = ("Segoe UI bold", 12)
    ttk.Label(
        frame,
        text=r"speak [type] [text/Filename] {rate} {volume} {.wav Output Filename [c:\temp\speak.wav]} {Output Format}",
        font=t6_font
    ).place(relx=.02, rely=.02)
    ttk.Label(frame, text="朗读文本", font=t6_font).place(relx=.02, rely=.2)
    ttk.Label(frame, text="朗读文件 [路径中不要包含中文]", font=t6_font).place(relx=.02, rely=.5)
    ttk.Label(frame, text="导出.wav [路径中不要包含中文]", font=t6_font).place(relx=.02, rely=.7)
    s_text = scrolledtext.ScrolledText(frame, width=60, height=4)
    s_text.place(relx=.02, rely=.3)
    speak_rate, speak_sound = tk.StringVar(), tk.StringVar()
    speak_rate.set("0")
    speak_sound.set("50")
    ttk.Label(frame, text="速率").place(relx=.02, rely=.1)
    ttk.Label(frame, text="音量 [0,100]").place(relx=.32, rely=.1)
    ttk.Combobox(frame, textvariable=speak_rate, values=[str(i) for i in range(-10, 11, 1)]).place(relx=.08, rely=.1)
    ttk.Entry(frame, textvariable=speak_sound).place(relx=.4, rely=.1)
    ttk.Button(
        frame, text="朗读文本", command=lambda: SecondRun(
            ["speak", "text", s_text.get("1.0", "end"), speak_rate.get(), speak_sound.get()])
    ).place(relx=.5, rely=.3)
    speak_file = tk.StringVar()
    ttk.Label(frame, text="指定.txt文件 [编码ANSI]").place(relx=.02, rely=.6)
    ttk.Entry(frame, textvariable=speak_file, width=32).place(rely=.6, relx=.2)
    ttk.Button(frame, text="选择", command=lambda: find_files(speak_file)).place(relx=.45, rely=.6)
    ttk.Button(
        frame, text="朗读文件", command=lambda: SecondRun(
            ["speak", "file", speak_file.get(), speak_rate.get(), speak_sound.get()])
    ).place(relx=.6, rely=.6)
    out_path, speak_type = tk.StringVar(), tk.StringVar()
    out_path.set("D:\\output.wav")
    ttk.Label(frame, text="导出文件路径").place(relx=.02, rely=.8)
    ttk.Label(frame, text="输出格式").place(relx=.52, rely=.8)
    ttk.Entry(frame, width=32, textvariable=out_path).place(relx=.12, rely=.8)
    ttk.Button(frame, text="选择", command=lambda: find_files(out_path)).place(relx=.35, rely=.8)
    ttk.Combobox(frame, textvariable=speak_type, values=[
        "8kHz8BitMono", "8kHz8BitStereo", "8kHz16BitMono", "8kHz16BitStereo", "11kHz8BitMono", "11kHz8BitStereo",
        "11kHz16BitMono", "11kHz16BitStereo", "12kHz8BitMono", "12kHz8BitStereo", "12kHz16BitMono", "12kHz16BitStereo",
        "16kHz8BitMono",
        "16kHz8BitStereo", "16kHz16BitMono", "16kHz16BitStereo", "22kHz8BitMono", "22kHz8BitStereo", "22kHz16BitMono",
        "22kHz16BitStereo", '24kHz8BitMono', '24kHz8BitStereo', '24kHz16BitMono', '24kHz16BitStereo', '32kHz8BitMono',
        '32kHz8BitStereo', '32kHz16BitMono', '32kHz16BitStereo', '44kHz8BitMono', '44kHz8BitStereo', '44kHz16BitMono',
        '44kHz16BitStereo', '48kHz8BitMono', '48kHz8BitStereo', '48kHz16BitMono', '48kHz16BitStereo',
        'TrueSpeech_8kHz1BitMono', 'CCITT_ALaw_8kHzMono', 'CCITT_ALaw_8kHzStereo', 'CCITT_ALaw_11kHzMono',
        'CCITT_ALaw_11kHzStereo',
        'CCITT_ALaw_22kHzMono', 'CCITT_ALaw_22kHzStereo', 'CCITT_ALaw_44kHzMono', 'CCITT_ALaw_44kHzStereo',
        'CCITT_uLaw_8kHzMono',
        'CCITT_uLaw_8kHzStereo', 'CCITT_uLaw_11kHzMono', 'CCITT_uLaw_11kHzStereo', 'CCITT_uLaw_22kHzMono',
        'CCITT_uLaw_22kHzStereo', 'CCITT_uLaw_44kHzMono', 'CCITT_uLaw_44kHzStereo', 'ADPCM_8kHzMono',
        'ADPCM_8kHzStereo', 'ADPCM_11kHzMono', 'ADPCM_11kHzStereo', 'ADPCM_22kHzMono', 'ADPCM_22kHzStereo',
        'ADPCM_44kHzMono',
        'ADPCM_44kHzStereo', 'GSM610_8kHzMono', 'GSM610_11kHzMono', 'GSM610_22kHzMono', 'GSM610_44kHzMono'
    ]).place(relx=.6, rely=.8)

    def out_wav(arg0, arg1, arg2, arg3, arg4, arg5):
        if arg1 and arg4 and arg5:
            SecondRun(["speak", arg0, arg1, arg2, arg3, arg4, arg5])
            messagebox.showinfo("speak", "导出成功！")
        else:
            messagebox.showerror("speak", "请检查参数设置！")

    ttk.Button(frame, text="文本导出音频", command=lambda: out_wav(
        "text", s_text.get("1.0", "end"), speak_rate.get(), speak_sound.get(),
        out_path.get(), speak_type.get())).place(relx=.12, rely=.9)
    ttk.Button(frame, text="文件导出音频", command=lambda: out_wav(
        "file", speak_file.get(), speak_rate.get(), speak_sound.get(),
        out_path.get(), speak_type.get())).place(relx=.32, rely=.9)


#     "结束进程": lambda: messagebox.showinfo(
#         "closeprocess",
#         "结束指定的进程，通过关闭其顶层窗口。与 killprocess 命令不同，closeprocess 命令不会立即强制结束进程。相反，它向指定进程的所有顶层窗口发送 WM_CLOSE 消息。但请注意，此命令不会对没有用户界面的进程有效。\n"
#         r"在 [process] 参数中，你可以指定进程文件的完整路径（例如：'C:\Program Files\Internet Explorer\iexplore.exe'）"
#         "\n或仅指定进程名称，不带路径（例如：iexplore.exe）。你还可以通过在前面加上\'/\' 字符来指定进程ID（例如 /1120）。示例：\n"
#         "closeprocess iexplore.exe\n"
#         "closeprocess \"c:\winnt\system32\calc.exe\"\n"
#         "closeprocess /1830"),
#     "结束进程2": lambda: messagebox.showinfo(
#         "killprocess",
#         "终止指定的进程。在[进程]参数中，你可以填写进程文件的完整路径（例如：\'C:\Program Files\Internet Explorer\iexplore.exe\'）或者仅填写进程名称，不包括路径（例如：iexplore.exe）。你也可以通过在前面加上\'/\'字符来指定进程ID（例如：/1120）。"
#         "\n示例：\n"
#         "killprocess iexplore.exe\n"
#         "killprocess \"c:\winnt\system32\calc.exe\"\n"
#         "killprocess /1830"
#     ),


def funcTab1_7(frame):
    # Windows弹窗
    ttk.Label(frame, text="Windows弹窗").place(relx=.02, rely=.02)
    title_FT17, message_FT17 = tk.StringVar(), tk.StringVar()
    ttk.Label(frame, text="标题\t\t\t\t\t\t\t消息").place(relx=.2, rely=.02)
    tk.Entry(frame, textvariable=title_FT17).place(relx=.3, rely=.02)
    tk.Entry(frame, textvariable=message_FT17).place(relx=.6, rely=.02)
    ttk.Button(
        frame, text="弹一个",
        command=lambda: SecondRun(["infobox", message_FT17.get(), title_FT17.get()])
    ).place(relx=.9, rely=.02)
    # 询问执行程序
    ttk.Label(frame, text="询问执行程序").place(relx=.02, rely=.12)
    exe_FT17, quest_FT17 = tk.StringVar(), tk.StringVar()
    ttk.Label(frame, text="程序\t\t\t\t\t\t\t问题").place(relx=.2, rely=.12)
    tk.Entry(frame, textvariable=exe_FT17).place(relx=.3, rely=.12)
    ttk.Button(frame, text="浏览", width=8, command=lambda: find_files(exe_FT17)).place(relx=.45, rely=.12)
    tk.Entry(frame, textvariable=quest_FT17).place(relx=.6, rely=.12)
    ttk.Button(
        frame, text="执行",
        command=lambda: SecondRun(["qbox", quest_FT17.get(), "Question", exe_FT17.get()])
    ).place(relx=.9, rely=.12)
    # 以“SYSTEM”用户身份运行
    ttk.Label(frame, text="以“SYSTEM”用户身份运行").place(relx=.02, rely=.22)
    Sys_exe_FT17 = tk.StringVar()
    ttk.Label(frame, text="程序\t\t\t\t\t\t\t\t\t请谨慎使用此选项").place(relx=.2, rely=.22)
    tk.Entry(frame, textvariable=Sys_exe_FT17).place(relx=.3, rely=.22)
    ttk.Button(frame, text="浏览", width=8, command=lambda: find_files(Sys_exe_FT17)).place(relx=.45, rely=.22)
    ttk.Button(
        frame, text="执行",
        command=lambda: SecondRun(["elevatecmd", "runassystem", Sys_exe_FT17.get()])
    ).place(relx=.9, rely=.22)
    # 截图
    ttk.Button(frame, text="截图", command=lambda: messagebox.showinfo(
        "savescreenshot",
        "将当前屏幕的截图保存到指定的图像文件名中。支持以下文件格式：.bmp, .gif, .png, .jpg, .tiff。如果你想将截图保存到剪贴板，可以使用*clipboard*代替实际的文件名。\n"

        "此命令仅适用于Windows XP/2003/Vista（需要GDI+）。\n\n"

        "你还可以指定四个可选参数 - x, y, width, 和 height，如果你只想保存屏幕的一部分。\n\n"

        "示例：\n"
        "savescreenshot \"c:\\temp\\shot.png\"\n"
        "savescreenshot \"c:\\temp\\shot.png\" 50 50 300 200\n"
        "savescreenshot *clipboard* 150 150 400 400\n\n"

        "第一个示例将整个屏幕的截图保存为 \"c:\\temp\\shot.png\"。"
        "\n第二个示例将屏幕的一部分（从坐标(50,50)开始，宽度为300像素，高度为200像素）保存到 \"c:\\temp\\shot.png\"。"
        "\n第三个示例将整个屏幕的截图保存到剪贴板中。\n"
        "\n您可以自定义快捷方式+快捷键+命令 执行命令")).place(relx=.02, rely=.32)
    ttk.Button(frame, text="快捷方式+快捷键+命令", command=lambda: messagebox.showinfo(
        "cmdshortcutkey",
        "与cmdshortcut命令类似，但还允许你指定一个热键来激活该命令。\n"

        "\n示例：\n"
        "cmdshortcutkey \"~$folder.desktop$\" \"Open CDROM\" \"Ctrl+Shift+K\" cdrom open k:\n"
        "cmdshortcutkey \"c:\\temp\" \"Turn Monitor Off\" \"Ctrl+Shift+M\" monitor off\n"

        "\n这些示例展示了如何创建带有热键的快捷方式。\n"
        "第一个示例创建了一个快捷方式，当按下Ctrl + Shift + K时，会打开CD - ROM驱动器（假设命令cdrom open k: 是有效的）。\n"
        "第二个示例创建了一个快捷方式，当按下Ctrl + Shift + M时，会关闭显示器（假设命令monitor off是有效的）。\n"
        "注意，实际命令的执行取决于系统环境和命令的有效性。\n"
    )).place(relx=.12, rely=.32)
    ttk.Button(frame, text="批处理", command=lambda: messagebox.showinfo(
        "script",
        "执行存储在指定脚本文件中的命令序列。\n"

        "\n示例：\n"
        "script \"c:\\temp\\msg.ncl\"\n\n"

        "脚本文件（如msg.ncl）可能包含一系列命令，例如：\n"

        "infobox \"Hello !\" \"This is the first message\"\n"
        "infobox \"Hello !\" \"This is the second message\"\n"
        "infobox \"Hello !\" \"This is the third message\"\n\n"
        "当你运行script \"c:\\temp\\msg.ncl\"命令时，它会依次执行脚本文件中的每个命令。在这个例子中，它会依次显示三个信息框，每个信息框都包含一条消息。这种脚本功能允许批量执行一系列操作，非常适合自动化重复任务。"
    )).place(relx=.3, rely=.32)
    ttk.Button(frame, text="模拟按键", command=lambda: os.system(
        "start https://blog.csdn.net/qq_46603846/article/details/142899437?sharetype=blogdetail&sharerId=142899437&sharerefer=PC&sharesource=qq_46603846&spm=1011.2480.3001.8118"
    )).place(relx=.4, rely=.32)
    ttk.Button(frame, text="模拟鼠标", command=lambda: messagebox.showinfo(
        "sendmouse",
        "发送指定的鼠标事件到系统。操作系统将完全模拟用户实际执行了指定的鼠标操作。\n"
        "以下是一些sendmouse命令的例子：\n\n"
        "发送一个右键点击（在大多数应用程序中，会打开一个上下文菜单）：\n"
        "sendmouse right click\n"
        "使用左键进行双击：\n"
        "sendmouse left dblclick"
        "按下左键，将鼠标光标向左移动30像素，向下移动20像素，然后释放按钮：\n"
        "sendmouse left down\n"
        "sendmouse move -30 20\n"
        "sendmouse left up\n"
        "在标准滚轮鼠标上滚动鼠标滚轮10个单位。（在标准滚轮鼠标上，滚轮值应该是120的倍数）。\n"
        "sendmouse wheel 1200"

        "\n\n请注意，这些命令的执行可能需要相应的权限，且在某些系统或应用程序中可能不工作。"
    )).place(relx=.5, rely=.32)
    # setbrightness 60 3
    ttk.Label(frame, text="自定义亮度[笔记本/上网本]").place(relx=.02, rely=.42)
    brightnessLevel_FT17 = tk.StringVar()
    brightnessLevel_FT17.set("50")
    ttk.Label(frame, text="亮度[0,100]").place(relx=.2, rely=.42)
    tk.Entry(frame, textvariable=brightnessLevel_FT17).place(relx=.3, rely=.42)
    ttk.Button(
        frame, text="调整",
        command=lambda: SecondRun(["setbrightness", brightnessLevel_FT17.get(), "3"])
        # 1 = Change the brightness under AC power.交流
        # 2 = Change the brightness under DC power.直流
        # 3 = Change the brightness for both AC power amd DC power (The default).
    ).place(relx=.6, rely=.42)
    # setfilefoldertime [filename, folder or wildcard] [Created Date] {Modified Date} {Accessed Date}
    ttk.Label(frame, text="更改文件/文件夹的三个时间").place(relx=.02, rely=.52)
    time1_FT17, time2_FT17, time3_FT17, fileDate_FT17 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
    ttk.Label(frame, text="文件/文件夹\t\t\t\t\t\t\t\t创建日期").place(relx=.2, rely=.52)
    ttk.Label(frame, text="修改日期\t\t\t\t\t\t\t\t访问日期").place(relx=.2, rely=.62)
    tk.Entry(frame, textvariable=fileDate_FT17).place(relx=.3, rely=.52)
    ttk.Button(frame, text="文件", command=lambda: find_files(fileDate_FT17)).place(relx=.45, rely=.52)
    ttk.Button(frame, text="文件夹", command=lambda: find_directory(fileDate_FT17)).place(relx=.55, rely=.52)
    ttk.Button(frame, text="说明", command=lambda: messagebox.showinfo(
        "无法运行说明",
        "您可以在终端运行\n"
        "nircmd setfilefoldertime [filename, folder or wildcard] [Created Date] {Modified Date} {Accessed Date}\n"
        "示例：\n"
        "nircmd setfilefoldertime \"c:\\temp\myfolder\" \"10-01-2003 11:22:12\" \"12-11-2002 02:34:11\""
    )).place(relx=.9, rely=.52)
    # 格式化  "dd-mm-yyyy hh:nn:ss"
    time1_FT17.set("now")
    time2_FT17.set("now")
    time3_FT17.set("now")
    ttk.Combobox(frame, values=["10-01-2003 11:22:12", ], textvariable=time1_FT17).place(relx=.7, rely=.52)
    ttk.Combobox(frame, values=["10-01-2003 11:22:12", ], textvariable=time2_FT17).place(relx=.3, rely=.62)
    ttk.Combobox(frame, values=["10-01-2003 11:22:12", ], textvariable=time3_FT17).place(relx=.7, rely=.62)
    ttk.Button(
        frame, text="修改",
        command=lambda: SecondRun([
            "setfilefoldertime", f"\"{fileDate_FT17.get()}\"",
            f"\"{time1_FT17.get()}\"", f"\"{time2_FT17.get()}\"", f"\"{time3_FT17.get()}\""])
    ).place(relx=.9, rely=.62)
    # os.system(f"{path} setfilefoldertime {fileDate_FT17.get()} {time1_FT17.get()} {time2_FT17.get()} {time3_FT17.get()}")
    # SecondRun(["setfilefoldertime", fileDate_FT17.get(), time1_FT17.get(), time2_FT17.get(), time3_FT17.get()])

    # win语音输入
    ttk.Button(
        frame, text="语音输入", command=lambda: messagebox.showinfo("语音输入", "Windows11请按\nWin+H")
    ).place(relx=.6, rely=.32)


def Tab3_func(frame: ttk.Notebook):
    def openDownloadUrl(e):
        os.system("start http://nircmd.nirsoft.net/")

    def openIssueUrl(e):
        os.system("start https://github.com/Pfolg/PGBox/issues")

    bg = "#f9f9f9"
    NirCmdPath = tk.StringVar()
    NirCmdPath.set(path)
    ttk.Label(
        frame, text="设置NirCmd.exe程序路径", font=defaultFont, background=bg
    ).place(relx=.02, rely=.02)
    ttk.Entry(frame, width=80, textvariable=NirCmdPath).place(relx=.02, rely=.12)
    ttk.Button(frame, text="浏览", command=lambda: find_files(NirCmdPath)).place(relx=.6, rely=.12)
    ttk.Button(frame, text="保存", command=lambda: MakeSetting("nircmd_path", NirCmdPath.get())).place(relx=.8,
                                                                                                       rely=.12)

    # 下载链接
    ttk.Label(frame, text="还没有这个程序？", background=bg).place(relx=.8, rely=.02)
    downloadLabel = ttk.Label(frame, text="去下载", foreground="#05ACFF", cursor="hand2", background=bg)
    downloadLabel.place(relx=.89, rely=.02)
    downloadLabel.bind("<Button-1>", openDownloadUrl)
    ttk.Label(
        frame,
        text="小杂鱼（尊敬的用户大人），\n你（您）还想有什么别的设置吗？\n没有啦！（Doge x 10087\n当然，如果你想加的话，那就请提",
        font=("Times New Roman", 32),
        foreground="#3e8fbf", background=bg
    ).place(relx=.2, rely=.5)
    issueLabel = ttk.Label(
        frame, text="  New Issue  ", cursor="hand2", foreground=bg, background="#1c8139", font=("Segoe UI bold", 32)
    )
    issueLabel.place(relx=.38, rely=.88)
    issueLabel.bind("<Button-1>", openIssueUrl)


def TabLastAbout(frame: ttk.Frame):
    def open_url1(event):
        os.system(f"start {url}")

    def open_url2(e):
        os.system("start https://github.com/Pfolg/PGBox/blob/main/LICENSE.txt")

    def open_url3(e):
        os.system("start https://github.com/Pfolg/PGBox")

    def open_url4(e):
        os.system("start https://github.com/Pfolg/Pfolg_Source/releases/tag/v.max_NirCmd-Gui-Chinese")

    information = "你好"
    text = tk.Text(frame, height=10, width=50)
    text.tag_configure("bold", font=('Helvetica', 14, 'bold'))  # 加粗格式
    text.tag_configure("header", font=('Helvetica', 20, 'bold'))  # 加粗格式
    text.tag_configure("italic", font=('Helvetica', 14, 'italic'))  # 斜体格式
    text.tag_configure("underline", underline=True)  # 下划线格式
    text.tag_configure("link1", foreground="blue", underline=True)
    text.tag_bind("link1", "<Button-1>", open_url1)  # 绑定鼠标左键点击事件
    text.tag_configure("link2", foreground="blue", underline=True)
    text.tag_bind("link2", "<Button-1>", open_url2)  # 绑定鼠标左键点击事件
    text.tag_configure("link3", foreground="blue", underline=True)
    text.tag_bind("link3", "<Button-1>", open_url3)  # 绑定鼠标左键点击事件
    text.tag_configure("link4", foreground="blue", underline=True)
    text.tag_bind("link4", "<Button-1>", open_url4)  # 绑定鼠标左键点击事件
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)
    text.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    # 插入文本并应用格式
    text.insert("end", "简介\n", "header")
    text.insert(
        "end", "\n此程序是我的一个练习作品，单纯是为了提升编程水平，次要是为了做一个NirCmd的Gui，其实主要成分还是Gui，核心代码就两三行。\n"
               "主要是Gui，功能基于 [nircmd v2.87] 实现，程序本身不提供一些重要的功能。\n\n")
    text.insert("end", "关于NirCmd\n", "header")
    text.insert("end", "\nhttp://nircmd.nirsoft.net/\n\n", "link1")
    text.insert("end", "关于此程序\n", "header")
    text.insert("end",
                "\n看源码就行了，基于Python，使用tkinter制作Gui。\n我只是选择性的对一些命令进行了Gui化，如果你还想要完全释放NirCmd的能力，你可以阅读官方文档进一步学习。\n\n")
    text.insert("end", "Licence\n", "header")
    text.insert("end", "\nhttps://github.com/Pfolg/PGBox/blob/main/LICENSE\n\n", "link2")
    text.insert("end", "项目地址\n", "header")
    text.insert("end", "\n集成：")
    text.insert("end", "https://github.com/Pfolg/PGBox\n\n", "link3")
    text.insert("end", "单发布：")
    text.insert("end", "https://github.com/Pfolg/Pfolg_Source/releases/tag/v.max_NirCmd-Gui-Chinese\n\n", "link4")
    text.insert("end", "作者\n", "header")
    text.insert("end", "\nPfolg")

    text.config(state="disabled")


def functionTab(tab: ttk.Frame, funcDict: dict):
    # label.pack(fill="both", expand=False)  # fill x,y,both
    i, j = .02, .02
    for item in funcDict:
        if j < .95:
            ttk.Button(tab, text=item, command=funcDict.get(item)).place(relx=i, rely=j)
            j += .075
        else:
            j = .02
            i += .2
            ttk.Button(tab, text=item, command=funcDict.get(item)).place(relx=i, rely=j)


def pin(mainTab: ttk.Notebook, frameDict: dict):
    for item in frameDict:
        mainTab.add(frameDict.get(item), text=item)
    mainTab.pack(fill='both', expand=True)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("NirCmd-Gui-Chinese")
    screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
    w, h = int(screen_w / 1.5), int(screen_h / 1.5)
    root.geometry(f'{w}x{h}+{int(screen_w / 6)}+{int(screen_h / 6)}')
    # root.state("zoomed")
    # root.resizable(False, False)
    # root.attributes('-alpha', 0.9)

    # 创建一个Notebook控件
    notebook = ttk.Notebook(root)

    # 添加两个标签页到Notebook
    tab1 = ttk.Notebook(notebook, width=w, height=h)
    # tab2 = ttk.Notebook(notebook, width=w, height=h)
    tab3 = ttk.Notebook(notebook, width=w, height=h)
    tabLast = ttk.Frame(notebook, width=w, height=h)

    # 子标签页
    tab1_1 = ttk.Frame(tab1, width=w, height=h)
    tab1_2 = ttk.Frame(tab1, width=w, height=h)
    tab1_3 = ttk.Frame(tab1, width=w, height=h)
    tab1_4 = ttk.Frame(tab1, width=w, height=h)
    tab1_5 = ttk.Frame(tab1, width=w, height=h)
    tab1_6 = ttk.Frame(tab1, width=w, height=h)
    tab1_7 = ttk.Frame(tab1, width=w, height=h)
    # tab1_8 = ttk.Frame(tab1, width=w, height=h)
    # 子标签功能添加
    functionTab(tab1_1, funcTab1_1)
    functionTab(tab1_2, funcTab1_2)
    functionTab(tab1_3, funcTab1_3)
    functionTab(tab1_4, funcTab1_4)
    funcTab1_5(tab1_5)
    funcTab1_6(tab1_6)
    funcTab1_7(tab1_7)
    # funcTab1_8()
    # 加入父标签页
    tab1Dict = {
        "默认": tab1_1,
        "声音": tab1_2,
        "显示": tab1_3,
        "粘贴板": tab1_4,
        "文件记录": tab1_5,
        "朗读": tab1_6,
        "其他": tab1_7,
    }
    pin(tab1, tab1Dict)

    # tab2_1 = ttk.Frame(tab2, width=w, height=h)
    # tab2_2 = ttk.Frame(tab2, width=w, height=h)

    # 向标签页添加内容
    # ttk.Label(tab1, text="系统", font=defaultFont).place(relx=.9, rely=.02)
    # ttk.Label(tab2, text="", font=defaultFont).place(relx=.9, rely=.02)
    # ttk.Label(tab3, text="", font=defaultFont).place(relx=.9, rely=.02)

    # functionTab(tab1, funcTab1)
    Tab3_func(tab3)
    TabLastAbout(tabLast)

    # 将标签页添加至notebook
    notebookDict = {
        "系统": tab1,
        # "TAB2": tab2,
        "设置": tab3,
        "关于": tabLast,
    }
    pin(notebook, notebookDict)

    root.mainloop()
# 就这样了吧，乏啦
