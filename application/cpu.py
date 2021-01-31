# coding=utf-8
import time
import psutil
import os
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(125, 210, 200)

class MainWindow:
    window = None

    def __init__(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        MainWindow.window = pygame.display.set_mode(
            [SCREEN_WIDTH, SCREEN_HEIGHT])
        # 设置窗口的标题
        pygame.display.set_caption('系统数据管控1.01')
        while True:
            time.sleep(1)
            # 给窗口设置填充色
            MainWindow.window.fill(BG_COLOR)
            # 获取事件
            self.getEvent()
            #当前CPU利用率
            cpu_lv = psutil.cpu_percent()
            # print(cpu_lv)
            MainWindow.window.blit(self.getTextSurface('CPU使用率：'+str(cpu_lv)+'%'), (10, 10))
            
            # 当前内存使用率
            memory = psutil.virtual_memory()
            # print(memory)
            # 使用内存
            usedMemory = round(float(memory.used)/1024/1024/1024,2)
            MainWindow.window.blit(self.getTextSurface('使用内存：'+str(usedMemory)+'G'), (10, 50))
            # 可用内存
            availableMemory = round(float(memory.available)/1024/1024/1024,2)
            MainWindow.window.blit(self.getTextSurface('可用内存：'+str(availableMemory)+'G'), (10, 90))
            # 最大内存
            totalMemory =  round(float(memory.total)/1024/1024/1024,2)
            MainWindow.window.blit(self.getTextSurface('最大内存：'+str(totalMemory)+'G'), (10, 130))
            memory_lv = round(usedMemory/totalMemory*100, 2)
            MainWindow.window.blit(self.getTextSurface('内存使用率：'+str(memory_lv)+'%'), (10, 170))
            pygame.display.update()

    def getTextSurface(self, text):
        # 初始化字体的模块
        pygame.font.init()
        # 查看所有的字体名称
        # print(pygame.font.get_fonts())
        # 获取字体Font对象
        font = pygame.font.SysFont('kaiti', 18)
        # 绘制文字信息
        textSurface = font.render(text, True, TEXT_COLOR)
        return textSurface
    # 获取事件

    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()
        # 遍历事件
        for event in eventList:
            # 判断按下的键是关闭还是键盘按下的
            # 如果按的是推出，关闭窗口
            if event.type == pygame.QUIT:
                exit()

# while True:
#     time.sleep(1)
#     cpu_lv = psutil.cpu_percent()
#     # 当前cpu利用率:
#     # print(cpu_lv)
#     memory = psutil.virtual_memory()
#     # 当前内存使用率
#     memory_lv = float(memory.used) / float(memory.total) * 100
#     # print(memory_lv)
#     message = "当前CPU利用率："+str(cpu_lv)+"% 当前内存利用率：" +\
#     str(round(memory_lv, 2))+"%"
#     print(message)
if __name__ == '__main__':
    MainWindow()