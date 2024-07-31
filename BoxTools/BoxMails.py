# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   BoxMails |User    Pfolg
# 2024/7/24   13:24
import imaplib
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header
from tkinter.scrolledtext import ScrolledText


def readMailInfo():
    try:
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            mailConfig = [myDict.get("mail"), myDict.get("mailCode")]
            return mailConfig
    except BaseException:
        pass


def sendMail(inf):
    if inf:
        # SMTP服务器,这里使用163邮箱
        mail_host = "smtp." + inf[0].split("@")[1]  #"smtp.qq.com"
        # 发件人邮箱
        mail_sender = inf[0]
        # 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
        mail_license = inf[1]
        # 收件人邮箱，可以为多个收件人
        mail_receivers = vTo.get()

        mm = MIMEMultipart('related')

        # 邮件主题
        subject_content = subject.get()
        # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
        mm["From"] = mail_sender
        # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
        mm["To"] = mail_receivers
        # 设置邮件主题
        mm["Subject"] = Header(subject_content, 'utf-8')

        # 邮件正文内容
        body_content = writeMail.get("1.0", "end")
        # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
        message_text = MIMEText(body_content, "plain", "utf-8")
        # 向MIMEMultipart对象中添加文本对象
        mm.attach(message_text)

        # 创建SMTP对象
        stp = smtplib.SMTP()
        # 设置发件人邮箱的域名和端口，端口地址为25
        stp.connect(mail_host, 25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        stp.set_debuglevel(1)
        # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
        stp.login(mail_sender, mail_license)
        # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
        stp.sendmail(mail_sender, mail_receivers, mm.as_string())
        print("邮件发送成功")
        messagebox.showinfo(title="提示信息", message="邮件发送成功!")
        # 关闭SMTP对象
        stp.quit()


def showHistory(inf):
    if inf:
        showMail["state"] = "normal"
        showMail.delete("1.0", "end")

        # 配置IMAP服务器信息
        imap_host = "smtp." + inf[0].split("@")[1]
        username = inf[0]  # pfolg@foxmail.com
        password = inf[1]  # 或者使用授权码

        # 连接到IMAP服务器
        mail = imaplib.IMAP4_SSL(imap_host)
        mail.login(username, password)

        # 选择邮箱中的收件箱
        mail.select('inbox')

        # 搜索所有邮件
        status, messages = mail.search(None, 'ALL')

        msgList = messages[0].split()
        i = -1
        # listSubject = []
        # listContent = []
        while True:
            num = msgList[i]
            # 遍历邮件
            print()
            showMail.insert(tk.END, f"<{abs(i)}>" + "-" * 50 + "\n")
            # 获取邮件的详细信息
            status, data = mail.fetch(num, '(RFC822)')
            # 解析邮件内容
            msg = email.message_from_bytes(data[0][1])
            # 打印邮件主题
            try:
                print("~~~\n")
                showMail.insert(tk.END, "~~~\n")
                subject = (email.header.decode_header(msg['Subject'])[0][0]).decode()
                print('Subject:', subject)
                showMail.insert(tk.END, 'Subject:    ' + subject)
            except BaseException:
                showMail.insert(tk.END, 'Subject:    None')

            try:
                from_header = email.utils.getaddresses([msg['From']])  # [0][1]
                showMail.insert(tk.END, "\nFrom:   ")
                for j in from_header:
                    showMail.insert(tk.END, j[1])
            except BaseException:
                showMail.insert(tk.END, "\nFrom:   None")

            try:
                to_header = email.utils.getaddresses([msg['To']])  # [0][1]
                showMail.insert(tk.END, "\nTo:   ")
                for k in to_header:
                    showMail.insert(tk.END, k[1] + " ")
            except BaseException:
                showMail.insert(tk.END, "\nTo:   None")
            showMail.insert(tk.END, "\n~~~\n")
            print("~~~")
            # 如果需要读取邮件正文
            if msg.is_multipart():
                # 多部分邮件
                for part in msg.walk():
                    # 获取邮件内容类型
                    content_type = part.get_content_type()
                    # 获取邮件内容编码
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # 获取邮件内容
                        body = part.get_payload(decode=True)  # .decode()
                    except:
                        # 如果邮件内容是二进制类型
                        body = part.get_payload(decode=True)
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # 如果是纯文本内容
                        print(body.decode())
                        showMail.insert(tk.END, body.decode() + "\n")
            else:
                # 单部分邮件
                if msg.get_content_type() == "text/plain":
                    # 如果是纯文本内容
                    print(msg.get_payload(decode=True).decode())
            i -= 1
            if i == -6:
                break

        # 关闭连接
        mail.close()
        mail.logout()
        showMail["state"] = "disabled"


def mainMail(frame):
    # 写邮件内容的文本框
    global vFrom, vTo, writeMail, subject
    writeMail = ScrolledText(frame, height=16, width=70)
    writeMail.insert(tk.END, "在此键入邮件内容")

    vFrom, vTo, subject = tk.StringVar(), tk.StringVar(), tk.StringVar()
    fromAddrLabel = ttk.Label(frame, text="From")
    fromAddrEntry = ttk.Entry(frame, width=35, textvariable=vFrom)
    toAddrLabel = ttk.Label(frame, text="To")
    toAddrEntry = ttk.Entry(frame, width=35, textvariable=vTo)
    subjectLabel = ttk.Label(frame, text="主题")
    subjectEntry = ttk.Entry(frame, width=35, textvariable=subject)
    try:
        myMail = readMailInfo()
        vFrom.set(myMail[0])
        mailNum = ttk.Label(frame, text=myMail[0], font=("微软雅黑", 16))
    except BaseException:
        vFrom.set("发生了错误，请先配置相关设置!")

    global showMail

    sendButton = ttk.Button(frame, width=8, text="SEND", command=lambda: sendMail(myMail))

    # 只读文本框，查看邮件
    showMail = ScrolledText(frame, height=20, width=70, state="normal")
    showMail.insert(tk.END, "目前啥都没有")
    showMail.config(state="disabled")

    mailRefresh = ttk.Button(frame, text="查询", width=8, command=lambda: showHistory(myMail))

    def forgetAll():
        showMail.place_forget()
        writeMail.place_forget()
        fromAddrLabel.place_forget()
        fromAddrEntry.place_forget()
        toAddrLabel.place_forget()
        toAddrEntry.place_forget()
        sendButton.place_forget()
        mailNum.place_forget()
        mailRefresh.place_forget()
        subjectLabel.place_forget()
        subjectEntry.place_forget()

    def showView():
        forgetAll()
        showMail.place(relx=.22, rely=.3)
        mailNum.place(relx=.22, rely=.1)
        mailRefresh.place(relx=.75, rely=.15)

    def showWrite():
        forgetAll()
        fromAddrLabel.place(relx=.22, rely=.1)
        fromAddrEntry.place(relx=.32, rely=.1)
        toAddrLabel.place(relx=.22, rely=.2)
        toAddrEntry.place(relx=.32, rely=.2)
        writeMail.place(relx=.22, rely=.4)
        sendButton.place(relx=.75, rely=.15)
        subjectLabel.place(relx=.22, rely=.3)
        subjectEntry.place(relx=.32, rely=.3)

    ttk.Button(frame, text="查邮件", width=8, command=showView).place(relx=.02, rely=.1)
    ttk.Button(frame, text="写邮件", width=8, command=showWrite).place(relx=.02, rely=.2)
    ttk.Button(
        frame, text="帮助",
        command=lambda: messagebox.showinfo(title="提示信息", message="记得配置邮箱和授权码!\n"
                                                                      "只能查看最近5封邮件，可以自己改代码，\n"
                                                                      "以实现查看多封。\n"
                                                                      "要使用发信功能得配置邮箱授权码。\n"
                                                                      "<To>可以添加多个邮箱地址，以半角逗号分开。\n"
                                                                      "<主题>可不填"),
        width=8
    ).place(relx=.9, rely=.8)
