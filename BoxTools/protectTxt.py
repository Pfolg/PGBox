import hashlib
import random
import re


# cPPC1 = "定义此种简陋加解密方法为：cPfolgProtectCode1"


def diyIn(targetStr, here_key):
    apbt = "abcdefghijklmnopqrstuvwxyz"
    enStr = ""
    strEncode = targetStr.encode("gbk")
    listCode = []
    for code in strEncode:
        listCode.append(code)
    for lo in range(len(listCode)):
        num, lo = listCode[lo], lo + 1
        if lo % 2 == 0:
            newNum = (num * lo + lo ** 3) * here_key - here_key
        else:
            newNum = (num * lo + lo ** 2) * here_key + here_key
        enStr += f"{apbt[random.randint(0, len(apbt) - 1)]}{str(newNum)}"
    return enStr


def diyOut(item, here_key):
    myStr = b""
    x = re.split(r'[a-z]+', item)
    x.remove("")
    # print(type(x), x)
    for j in range(len(x)):
        a = j + 1
        # print(type(x[j]), x[j])
        b = eval(x[j])
        if a % 2 == 0:
            code = ((b + here_key) / here_key - a ** 3) / a
        else:
            code = ((b - here_key) / here_key - a ** 2) / a
        myStr += bytes([int(code)])
    return myStr.decode("gbk")


def jiaMi():
    pwd = input("定义密码（不能为0或者不输入）：")
    if not pwd:
        input("\t程序抛出了一个异常：淘气~")
        return
    filePath = input("输入.txt文件路径：")
    apwd = hashlib.sha256(pwd.encode("utf-8")).hexdigest()
    # print("apwd=", apwd)
    key = 0
    for i in pwd.encode("utf-8"):
        key += i
        # print("key=", key)

    with open(filePath, "r", encoding="utf-8") as file:
        c = file.readlines()
        content = [in_c.strip() for in_c in c]

    newList = [apwd]
    for i in content:
        newList.append(diyIn(i, key))

    with open(filePath, "w") as f:
        f.writelines([i + "\n" for i in newList])


def jieMi():
    pwd = input("请输入密码：")
    if not pwd:
        input("\t程序抛出了一个异常：淘气~")
        return
    filePath = input("输入.txt文件路径：")
    key = 0
    for i in pwd.encode("utf-8"):
        key += i
    apwd = hashlib.sha256(pwd.encode("utf-8")).hexdigest()

    with open(filePath, "r") as file:
        mic = [k.strip() for k in file.readlines()]
    if apwd != mic[0]:
        input("密码错误，请重新运行程序！[回车退出]")
        return
    listStr = []
    with open(filePath, "w") as f:
        for i in range(1, len(mic)):
            listStr.append(diyOut(mic[i], key) + "\n")
        f.writelines(listStr)


if __name__ == '__main__':
    print(
        '\033[31m' +
        '本程序会覆盖源文件，该过程可能不可逆，请及时备份\n'
        '本程序加密方法（cPPC1）为个人自制，在安全性方面无法提供完全保障\n'
        "本程序为.txt文件设计，其他文件尚未测试"
        + '\033[0m')
    flag = eval(input("1-加密，2-解密："))
    if flag == 1:
        jiaMi()
    elif flag == 2:
        jieMi()
    else:
        input("\t程序抛出了一个异常：呵~")
    input("程序运行结束，若未抛出异常，则可查验结果[回车退出]")
