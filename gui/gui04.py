"""测试Button组件的基本用法 """

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
        self.loginBtn3 = Button(root, text="登陆", command=self.login)
        self.loginBtn3.pack()
        self.loginBtn = Button(root, text="登陆", 
        width=6, height=3, anchor=E, command=self.login)
        self.loginBtn.pack()

        global photo
        photo = PhotoImage(file="images/1601094146011.gif")
        self.loginBtn2 = Button(root, image=photo, command=self.login)
        self.loginBtn2.pack()
        # 设置按钮为禁用
        self.loginBtn2.config(state="disabled")

    def login(self):
        messagebox.showinfo("按钮测试","登陆成功！欢迎使用")

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+200+300")
    app = Application(master=root)
    root.mainloop()
