# coding=utf-8
import time
import psutil
import os
import pygame

SCREEN_WIDTH=700
SCREEN_HEIGHT=500
BG_COLOR = pygame.Color(0,0,0)

class MainWindow:
    def __init__(self):
        pass

while True:
    time.sleep(1)
    cpu_lv = psutil.cpu_percent()
    # 当前cpu利用率:
    # print(cpu_lv)
    memory = psutil.virtual_memory()
    # 当前内存使用率
    memory_lv = float(memory.used) / float(memory.total) * 100
    # print(memory_lv)
    message = "当前CPU利用率："+str(cpu_lv)+"% 当前内存利用率：" +\
    str(round(memory_lv, 2))+"%"
    print(message)


