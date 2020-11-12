from tkinter import *
from tkinter import messagebox


root = Tk()

root.title('我的第一个GUI程序')
# 窗口大小设置和外间距设置  宽500高300 左外边距100 上外边距200
root.geometry('500x300+100+200')

btn01 = Button(root)
btn01['text'] = '点我就送花'
btn01.pack()

# e就是事件对象
def sendFlower(e):
    messagebox.showinfo('Message', '送你一朵玫瑰花，亲亲我吧')
    print('送你99朵玫瑰花')

btn01.bind('<Button-1>',sendFlower)

# 调用组件的mainloop()方法，进入事件循环，监听用户操作
root.mainloop()
