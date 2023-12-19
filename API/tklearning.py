import tkinter as tk
from tkinter import *
import time as cur_time


class MainWindow(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__()
        self.geometry("730x400+700+400")  # 设置窗口长宽和坐标

        # 窗口标题
        self.title('Label')
        # 初始按钮，后面会被覆盖
        self.label1 = Label(self, text='', width=70, height=10)
        # 设置按钮位置
        self.label1.grid(row=0, column=1)
        # 调用after函数
        self.after(100, self.refresh_data)
        # 窗口显示
        self.mainloop()

    def refresh_data(self):
        print('我在刷新')
        # 需要刷新数据的操作，从time函数活的当前时间
        self.label1 = Label(self, text=cur_time.time(), font=18, relief="solid", width=25, height=5, padx=2)
        self.label1.grid(row=0, column=1, padx=15, pady=20)
        # 递归循环调用after
        self.after(100, self.refresh_data)  # 这里的100单位为毫秒


if __name__ == '__main__':
    MainWindow = MainWindow()

