# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   frameTimer |User    Pfolg
# 2024/8/3   12:29
# 这个程序就不合并在PGTools上了，单拿出来也能用

import time
from tkinter import ttk
import threading
from tkinter import scrolledtext
import tkinter as tk


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("计时器")
        self.screen_w, self.screen_h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.w, self.h = int(self.screen_w / 3), int(self.screen_h / 3)
        self.root.geometry(f'{self.w}x{self.h}+{int(self.screen_w / 4)}+{int(self.screen_h / 4)}')
        self.root.resizable(False, False)

        self.running = False
        self.paused = False
        self.start_time = None
        self.pause_time = None
        self.count = 0

        self.time_label = ttk.Label(
            self.root, text="0.0000", font=("微软雅黑", 32), foreground="#FFFFFF", background="#c9d8ee")
        self.time_label.place(relx=.4, rely=.2)
        self.box = scrolledtext.ScrolledText(self.root, width=12, height=10)
        self.box.place(relx=.1, rely=.3)

        ttk.Button(self.root, text="Start", command=self.start_timer, width=8).place(relx=.4, rely=.5)
        ttk.Button(self.root, text="Pause", command=self.pause_timer, width=8).place(relx=.4, rely=.6)
        ttk.Button(self.root, text="Continue", command=self.continue_timer, width=8).place(relx=.55, rely=.6)
        ttk.Button(self.root, text="Stop", command=self.stop_timer, width=8).place(relx=.55, rely=.5)
        ttk.Button(self.root, text="Clear", command=self.clear_box, width=5).place(relx=.18, rely=.79)
        ttk.Button(self.root, text="Get", command=self.insert_timer, width=8).place(relx=.4, rely=.7)
        ttk.Button(self.root, text="Restore", command=self.restore_time_label, width=8
                   ).place(relx=.55, rely=.7)
        ttk.Button(self.root, text="Close", command=lambda: self.root.destroy(), width=8).place(relx=.85, rely=.9)

    def restore_time_label(self):
        self.stop_timer()
        self.time_label.config(text="0.0000")

    def clear_box(self):
        self.count = 0
        self.box.delete("1.0", "end")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = time.perf_counter()
            self.time_thread = threading.Thread(target=self.update_time)
            self.time_thread.start()

    def pause_timer(self):
        if self.running and not self.paused:
            self.paused = True
            self.pause_time = time.perf_counter()
            # self.count += 1
            # self.box.insert("end", "<{0}>{1:.4f}\n".format(self.count, self.main_time))

    def insert_timer(self):
        if self.main_time and self.running:
            self.count += 1
            self.box.insert("end", "<{0}>{1:.4f}\n".format(self.count, self.main_time))

    def continue_timer(self):
        if self.paused:
            self.paused = False
            self.start_time += time.perf_counter() - self.pause_time

    def stop_timer(self):
        self.running = False
        self.paused = False
        try:
            if self.time_thread is not None:
                self.time_thread.join()
                # self.time_label.config(text="0.0000")
        except AttributeError:
            self.root.destroy()

    def update_time(self):
        while self.running:
            if not self.paused:
                self.main_time = time.perf_counter() - self.start_time
                self.time_label.config(text="{:.4f}".format(self.main_time))
            time.sleep(0.1)

    def on_closing(self):
        self.stop_timer()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
