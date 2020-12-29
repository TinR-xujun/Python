'''
新增功能：
    加载主窗口
    pygame官方网站 www.pygame.org
'''
#导入pygame模块
import pygame

SCREEN_WIDTH=700
SCREEN_HEIGHT=500
BG_COLOR = pygame.Color(0,0,0)

class MainGame():
    window=None
    def __init__(self):
        pass
    #开始游戏
    def startGame(self):
        #加载主窗口
        #初始化窗口
        pygame.display.init()
        #设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #设置窗口的标题
        pygame.display.set_caption('坦克大战1.01')
        while True:
            #给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            pygame.display.update()
    #结束游戏
    def gameOver(self):
        pass
#坦克类
class Tank():
    def __init__(self):
        pass
    #移动
    def move(self):
        pass
    #射击
    def shot(self):
        pass
    #展示坦克的方法
    def display(self):
        pass
#我方坦克
class MyTank(Tank):
    def __init__(self):
        pass
#敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass
#子弹类
class Bullet():
    def __init__(self):
        pass
    #移动
    def move(self):
        pass
    #显示子弹的方法
    def display(self):
        pass
#墙壁类
class Wall():
    def __init__(self):
        pass
    #展示墙壁的方法
    def display(self):
        pass
#爆炸效果类
class Explode():
    def __init__(self):
        pass
    #展示爆炸效果的方法
    def display(self):
        pass
#音效类
class Music():
    def __init__(self):
        pass
    #播放音乐的方法
    def play(self):
        pass
if __name__=='__main__':
    MainGame().startGame()