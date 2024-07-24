# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   ToolsBox |User    Pfolg
# 2024/7/19   21:42
import tkinter as tk
import frame0


window = tk.Tk()
window.title("ToolsBox")
screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
w, h = int(screen_w / 2), int(screen_h / 2)
window.geometry(f'{w}x{h}+{int(screen_w / 4)}+{int(screen_h / 4)}')
window.resizable(False, False)
window.iconbitmap(".\\ico.ico")
window.attributes('-alpha', 0.9)

frame0.basicFrame0(w, h, window)

window.mainloop()
