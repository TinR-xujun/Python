'''
新增功能：
    加载我方坦克
'''
#导入pygame模块
import pygame
import os


#1、获取当前文件的路径
basedir = os.path.dirname(__file__)

#2、拼接文件路径
# update_path = os.path.join(basedir, "data/input", filename)

SCREEN_WIDTH=700
SCREEN_HEIGHT=500
BG_COLOR = pygame.Color(0,0,0)
TEXT_COLOR = pygame.Color(255,0,0)
class MainGame():
    window = None
    my_tank = None
    def __init__(self):
        pass
    #开始游戏
    def startGame(self):
        #加载主窗口
        #初始化窗口
        pygame.display.init()
        #设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #初始化我方坦克
        MainGame.my_tank = Tank(350,250)
        #设置窗口的标题
        pygame.display.set_caption('坦克大战1.01')
        while True:
            #给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            #获取事件
            self.getEvent()
            #绘制文字
            MainGame().window.blit(self.getTextSurface('敌方坦克剩余数量%d' %6),(10,10))
            #调用坦克显示的方法
            MainGame.my_tank.display()
            pygame.display.update()
    #结束游戏
    def gameOver(self,text):
        print('谢谢使用，欢迎再次使用')
        exit()
    #左上角文字的绘制
    def getTextSurface(self,text):
        #初始化字体的模块
        pygame.font.init()
        #查看所有的字体名称
        # print(pygame.font.get_fonts())
        #获取字体Font对象
        font = pygame.font.SysFont('kaiti',18)
        #绘制文字信息
        textSurface = font.render(text,True,TEXT_COLOR)
        return textSurface
    #获取事件
    def getEvent(self):
        #获取所有事件
        eventList = pygame.event.get()
        #遍历事件
        for event in eventList:
            #判断按下的键是关闭还是键盘按下的
            #如果按的是推出，关闭窗口
            if event.type == pygame.QUIT:
                self.gameOver()
            #如果是键盘的按下
            if event.type == pygame.KEYDOWN:
                #判断按下的是上、下、左、右
                if event.key == pygame.K_LEFT:
                    print('左')
                elif event.key == pygame.K_RIGHT:
                    print('右')
                elif event.key == pygame.K_UP:
                    print('上')
                elif event.key == pygame.K_DOWN:
                    print('下')

#坦克类
class Tank():
    #添加距离左边Left  距离上边top
    def __init__(self,left,top):
        # print("文件夹目录"+basedir)
        #保存加载的图片
        self.images = {
            'U': pygame.image.load(basedir+'/images/tank_1p_up.jpg'),
            'D': pygame.image.load(basedir+'/images/tank_1p_down.jpg'),
            'L': pygame.image.load(basedir+'/images/tank_1p_left.jpg'),
            'R': pygame.image.load(basedir+'/images/tank_1p_right.jpg')
        }
        #方向
        self.direction = 'L'
        #根据当前图片的方向获取图片 surface
        self.image = self.images[self.direction]
        #根据图片获取区域
        self.rect = self.image.get_rect()
        #设置区域的left和top
        self.rect.left = left
        self.rect.top = top

    #移动
    def move(self):
        pass
    #射击
    def shot(self):
        pass
    #展示坦克的方法
    def display(self):
        #获取展示的对象
        self.image = self.images[self.direction]
        #调用blit方法展示
        MainGame.window.blit(self.image,self.rect)

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
    # MainGame().getTextSurface()