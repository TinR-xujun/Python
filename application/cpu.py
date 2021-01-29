# coding=utf-8
import time
import psutil
import os
from tkinter import *

message = StringVar()

root = Tk()
root.title('系统参数')
# 窗口大小设置和外间距设置  宽500高300 左外边距100 上外边距200
root.geometry('500x300+100+200')
label = Label(root, text=message, width=10,
              height=2, bg="black", fg="white")
label.pack()

while True:
    time.sleep(1)
    cpu_lv = psutil.cpu_percent()
    # 当前cpu利用率:
    # print(cpu_lv)
    memory = psutil.virtual_memory()
    # 当前内存使用率
    memory_lv = float(memory.used) / float(memory.total) * 100
    # print(memory_lv)
    label['text'] = "当前CPU利用率："+str(cpu_lv)+"% 当前内存利用率：" +\
    str(round(memory_lv, 2))+"%"
    print(message)
    # 调用组件的mainloop()方法，进入事件循环，监听用户操作
root.mainloop()
