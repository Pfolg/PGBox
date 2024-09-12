# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   frameString |User    Pfolg
# 2024/9/11   15:44
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyperclip

left = .72


def reverseString(original_string="Hello, World!"):
    outst.config(state="normal")
    reversed_string = original_string[::-1]
    print(reversed_string)
    outst.delete("1.0", "end")
    outst.insert("end", reversed_string)
    outst.config(state="disabled")


def calculateString(original_string="Hello, World!"):
    outst.config(state="normal")
    length = len(original_string)
    print(length)
    outst.delete("1.0", "end")
    outst.insert("end", str(length))
    outst.config(state="disabled")


def upperAndLower(original_string="Hello, World!"):
    outst.config(state="normal")
    s = ""
    for i in original_string:
        if i.isupper():
            s += i.lower()
        elif i.islower():
            s += i.upper()
        else:
            s += i

    print(s)
    outst.delete("1.0", "end")
    outst.insert("end", s)
    outst.config(state="disabled")


# 编码
def inCode(s: str):
    outst.config(state="normal")
    ns = s.encode()
    outst.delete("1.0", "end")
    outst.insert("end", str(ns))
    outst.config(state="disabled")


# 解码
def outCode(s: str):
    try:
        ns = eval(s)
        x = ns.decode()
    except BaseException:
        x = "数据错误"
    finally:
        outst.config(state="normal")
        outst.delete("1.0", "end")
        outst.insert("end", x)
        outst.config(state="disabled")


def inCode2(s: str):
    outst.config(state="normal")
    outst.delete("1.0", "end")
    for ns in s.encode():
        outst.insert("end", str(ns) + " ")
    outst.config(state="disabled")


def delete_out():
    outst.config(state="normal")
    outst.delete("1.0", "end")
    outst.config(state="disabled")


def copy_out():
    outst.config(state="normal")
    pyperclip.copy(outst.get("1.0", "end"))
    outst.config(state="disabled")


def paste():
    t = pyperclip.paste()
    st.delete("1.0", "end")
    st.insert("end", t)


def calculateStrs(e):
    outs = st.get("1.0", "end") * ent.get()
    outst.config(state="normal")
    outst.delete("1.0", "end")
    outst.insert("end", outs)
    outst.config(state="disabled")
    # ent.set(2)
    nt.place_forget()


def frameString(frame):
    ttk.Label(frame, text="字符串运算").place(relx=.45, rely=.02)
    ttk.Label(frame, text="IN").place(relx=.1, rely=.05)
    ttk.Label(frame, text="OUT").place(relx=.1, rely=.45)
    ttk.Label(frame, text="灵感来源：刘慈欣《宇宙坍缩》").place(relx=.02, rely=.95)

    global st, outst, nt, ent

    st = scrolledtext.ScrolledText(frame, width=80, height=10)
    st.place(relx=.1, rely=.1)
    outst = scrolledtext.ScrolledText(frame, width=60, height=10, state="disabled")
    outst.place(relx=.1, rely=.5)

    ent = tk.IntVar()
    nt = ttk.Entry(frame, textvariable=ent, width=3)
    ent.set(2)
    nt.bind("<Return>", calculateStrs)

    tk.Button(frame, text="Copy", command=lambda: pyperclip.copy(st.get("1.0", "end"))).place(relx=.9, rely=.1)
    tk.Button(frame, text="Clear", command=lambda: st.delete("1.0", "end")).place(relx=.9, rely=.2)
    tk.Button(frame, text="Paste", command=paste).place(relx=.9, rely=.3)
    tk.Button(frame, text="Copy", command=copy_out).place(relx=.5, rely=.85)
    tk.Button(frame, text="Clear", command=delete_out).place(relx=.6, rely=.85)

    ttk.Button(
        frame, text="反转", command=lambda: reverseString(st.get("1.0", "end")), width=8
    ).place(relx=left, rely=.5)
    ttk.Button(
        frame, text="长度", command=lambda: calculateString(st.get("1.0", "end")), width=8
    ).place(relx=left, rely=.6)
    ttk.Button(
        frame, text="转码", command=lambda: upperAndLower(st.get("1.0", "end")), width=8
    ).place(relx=left, rely=.7)
    ttk.Button(
        frame, text="解码", command=lambda: inCode(st.get("1.0", "end")), width=8
    ).place(relx=left, rely=.8)

    ttk.Button(
        frame, text="转数", command=lambda: inCode2(st.get("1.0", "end")), width=8
    ).place(relx=left + .1, rely=.5)
    ttk.Button(
        frame, text="编码", command=lambda: outCode(st.get("1.0", "end")), width=8
    ).place(relx=left + .1, rely=.6)
    ttk.Button(
        frame, text="重复", command=lambda: nt.place(relx=left + .2, rely=.7), width=8
    ).place(relx=left + .1, rely=.7)
    ttk.Button(
        frame, text="压缩", command=lambda: messagebox.showinfo(title="提示信息", message="压缩请找AI"), width=8
    ).place(relx=left + .1, rely=.8)


if __name__ == '__main__':
    pass
    # window = tk.Tk()
    # window.title(f"字符串运算")
    # screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
    # w, h = int(screen_w / 2), int(screen_h / 2)
    # window.geometry(f'{w}x{h}+{int(screen_w / 4)}+{int(screen_h / 4)}')
    # window.resizable(False, False)
    #
    # frameS = ttk.Frame(width=w, height=h)
    # frameString(frameS)
    # frameS.place(relx=0, rely=0)
    #
    # window.mainloop()
