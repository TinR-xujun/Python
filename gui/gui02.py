"""测试一个经典的GUI程序的写法，使用面向对象的方式 """

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序类的写法"""

    def __init__(self, master=None):
        # super代表的是父类的定义，而不是父类对象
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.btn = Button(self)
        self.btn["text"] = "点击送花"
        self.btn.pack()
        self.btn["command"] = self.sendFlower

        # 创建一个退出按钮
        self.quit = Button(self, text="退出", command=root.destroy)
        self.quit.pack()

    def sendFlower(self):
        messagebox.showinfo('送花', '送你99朵玫瑰花')

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+200+300")
    root.title("一个经典的GUI程序类的测试")
    app = Application(master=root)
    root.mainloop()
