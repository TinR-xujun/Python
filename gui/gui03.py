"""测试Label组件的基本用法 """

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
        self.label = Label(self, text="label", width=10, height=2, bg="black", fg="white")
        self.label.pack()

        self.labelFont = Label(self, text="黑体", width=10, height=2, bg="blue", fg="white", font=("黑体", 30))
        self.labelFont.pack()

        # 显示图片
        # 全局变量，如果是局部变量，本方法执行完毕后，图像对象销毁，窗口不显示
        global photo
        photo = PhotoImage(file="images/1597215869440.gif")
        self.labelImg = Label(self, image=photo)
        self.labelImg.pack()

        # 显示多行文本
        self.labelTextArea = Label(self, text="xxxxxxxxxxxxx\nxxxxx\nxxxx", borderwidth=5, relief="groove", justify="right")
        self.labelTextArea.pack()

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+200+300")
    app = Application(master=root)
    root.mainloop()
