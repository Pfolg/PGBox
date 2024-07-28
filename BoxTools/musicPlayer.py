import tkinter as tk
import pygame
from tkinter import filedialog
import os
from tkinter import messagebox
from tkinter import ttk
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggopus import OggOpus
from mutagen.oggvorbis import OggVorbis
import re

DefaultFont = r"C:\Windows\Fonts\calibril.ttf"


def find_files(x):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.delete(0, 'end')
    x.insert(0, file_path)
    win.destroy()


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
        with open(r".\setting\Setting-musicPlayer.txt", "r", encoding="utf-8") as file:
            DefaultPath = file.readline()
            if DefaultPath == "":
                messagebox.showerror(title="Error",
                                     message="读取音乐文件夹设置生错误，\n请在[../setting/Setting-musicPlayer.txt]内填入音乐文件夹路径\n"
                                             "或者使用设置工具")
    except FileNotFoundError:
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


if __name__ == '__main__':
    pass
