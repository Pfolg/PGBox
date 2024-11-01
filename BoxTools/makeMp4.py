import os


def start_question():
    print('\033[38;2;0;255;0m' + '请确认已下载ffmpeg，并已将其的bin文件夹添加至环境变量' + '\033[0m')
    print("您可以在此获取 https://www.gyan.dev/ffmpeg/builds/")
    confirm1 = input("Y/N?[Y]")
    if confirm1 == "N":
        input("[回车退出]")
        return False
    print('\033[38;2;0;255;0m' + '请确认您已知晓本程序的基本原理：' + '\033[0m')
    print('\033[38;2;255;0;0m' + 'ffmpeg -i video.mp4 -vf subtitles=srt_file.srt output.mp4' + '\033[0m')
    confirm2 = input("Y/N?[Y]")
    if confirm2 == "N":
        input("[回车退出]")
        return False
    return True


def out_mp4_file():
    print("您可以使用相对路径，三条路径均不能包含中文字符！")
    mp4_file = input('\033[36m' + "请输入mp4文件路径:" + '\033[0m')
    srt_file = input('\033[36m' + "请输入srt文件路径:" + '\033[0m')
    out_file = input('\033[36m' + "请输入输出文件路径:" + '\033[0m')
    if mp4_file and srt_file and out_file:
        os.system("ffmpeg -i {0} -vf subtitles={1} {2}".format(mp4_file, srt_file, out_file))
    else:
        print('\033[38;2;255;0;0m' + "您的输入好像有问题，请检查后再试" + '\033[0m')


flag = False

while True:
    if not flag:
        flag = start_question()
    if not flag:
        break
    out_mp4_file()
    confirm3 = input("[回车继续/q 退出]")
    if confirm3 == "q":
        break
