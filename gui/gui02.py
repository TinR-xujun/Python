"""测试一个经典的GUI程序的写法，使用面向对象的方式 """

from tkinter import *

class Application(Frame):
    """一个经典的GUI程序类的写法"""

    def __init__(self, master=None):
        # super代表的是父类的定义，而不是父类对象
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.createWidget()
    
    def createWidget(self):
        pass

root = Tk()
root.geometry("500x300+200+300")
root.title("一个经典的GUI程序类的测试")
app = Application(master=root)
root.mainloop()