'''
新增功能：
    1.子弹不能穿墙
        子弹碰撞到墙壁的时候，子弹消失
    2.墙壁被击中，墙壁的生命值处理
          
'''
# 导入pygame模块
import pygame
import os
import time
import random


# 1、获取当前文件的路径
basedir = os.path.dirname(__file__)

# 2、拼接文件路径
# update_path = os.path.join(basedir, "data/input", filename)

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 900
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)
ENEMY_STEP = 60
# 定义一个基类


class BaseItem(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


class MainGame():
    window = None
    my_tank = None
    # 存储敌方坦克的列表
    enemyTankList = []
    # 定义敌方坦克的数量
    enemyTankCount = 5
    # 存储我方子弹的列表
    myBulletList = []
    # 存储敌方子弹的列表
    enemyBulletList = []
    # 存储爆炸对象的列表
    explodeList = []
    # 存储墙壁的列表
    wallList = []

    def __init__(self):
        pass
    # 开始游戏

    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode(
            [SCREEN_WIDTH, SCREEN_HEIGHT])
        # 初始化我方坦克
        self.createMyTank()
        # 初始化敌方坦克，并将敌方坦克添加到列表中
        self.createEnemyTank()
        # 初始化墙壁
        self.createWall()
        # 设置窗口的标题
        pygame.display.set_caption('坦克大战1.01')
        while True:
            # 使坦克移动的速度慢一点
            time.sleep(0.02)
            # 给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            # 获取事件
            self.getEvent()
            # 绘制文字
            MainGame().window.blit(self.getTextSurface('敌方坦克剩余数量%d' %
                                                       len(MainGame.enemyTankList)), (10, 10))
            if MainGame.my_tank and MainGame.my_tank.live:
                # 调用坦克显示的方法
                MainGame.my_tank.display()
            else:
                # 删除我方坦克
                del MainGame.my_tank
                MainGame.my_tank = None
            # 循环遍历敌方坦克列表，展示敌方坦克
            self.blitEnemyTank()
            # 循环遍历我方坦克的子弹
            self.blitMyBullet()
            # 循环遍历敌方子弹列表，展示敌方子弹
            self.blitEnemyBullet()
            # 遍历爆炸列表，展示爆炸效果
            self.blitExplode()
            # 遍历墙壁列表，展示墙壁
            self.blitWall()
            # 调用移动方法
            # 如果坦克的开关是开启才可以移动
            if MainGame.my_tank and MainGame.my_tank.live:
                if not MainGame.my_tank.stop:
                    MainGame.my_tank.move()
            pygame.display.update()
    # 创建我方坦克

    def createMyTank(self):
        MainGame.my_tank = Tank(800, 800)
    # 初始化敌方坦克，并将敌方坦克添加到列表中

    def createEnemyTank(self):
        top = 60
        # 循环生成敌方坦克
        for i in range(MainGame.enemyTankCount):
            left = random.randint(0, 1600)
            speed = random.randint(1, 4)
            enemy = EnemyTank(left, top, speed)
            MainGame.enemyTankList.append(enemy)
    # 初始化墙壁

    def createWall(self):
        for i in range(6):
            # 初始化墙壁
            wall = Wall(i*200, 400)
            # 将墙壁添加到列表中
            MainGame.wallList.append(wall)
    # 遍历爆炸列表，展示爆炸效果

    def blitExplode(self):
        for explode in MainGame.explodeList:
            # 判断是否活着
            if explode.live:
                # 展示
                explode.display()
            else:
                # 在爆炸列表中移除
                MainGame.explodeList.remove(explode)
    # 遍历墙壁列表，展示墙壁

    def blitWall(self):
        for wall in MainGame.wallList:
            #判断墙壁是否存活
            if wall.live:
                # 调用墙壁的展示方法
                wall.display()
            else:
                #从墙壁列表中移除
                MainGame.wallList.remove(wall)
    # 循环遍历敌方坦克列表，展示敌方坦克

    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            if enemyTank.live:
                enemyTank.display()
                enemyTank.randMove()
                # 发射子弹
                enemyBullet = enemyTank.shot()
                # 敌方子弹是否是None，如果不为None则添加到敌方子弹列表
                if enemyBullet:
                    # 将敌方子弹存储到敌方子弹列表中
                    MainGame.enemyBulletList.append(enemyBullet)
            else:
                # 从敌方坦克列表中移除
                MainGame.enemyTankList.remove(enemyTank)

    # 循环遍历我方子弹存储列表
    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            # 判断当前的子弹是否是存活状态，如果是则 进行显示及移动
            if myBullet.live:
                myBullet.display()
                # 调用子弹的移动方法
                myBullet.move()
                # 调用检测我方子弹是否与敌方坦克发生碰撞
                myBullet.myBullet_hit_enemyTank()
                # 检测我 方子弹是否与墙壁碰撞
                myBullet.hitWall()
            # 否则在列表中删除
            else:
                MainGame.myBulletList.remove(myBullet)
    # 循环遍历敌方子弹列表，展示敌方子弹

    def blitEnemyBullet(self):
        for enemyBullet in MainGame.enemyBulletList:
            # 判断敌方子弹是否存活
            if enemyBullet.live:
                enemyBullet.display()
                # 调用子弹的移动方法
                enemyBullet.move()
                # 调用敌方子弹是否与我方坦克发生碰撞
                enemyBullet.enemyBullet_hit_myTank()
                # 检测敌方子弹是否与墙壁碰撞
                enemyBullet.hitWall()
            # 否则在列表中删除
            else:
                MainGame.enemyBulletList.remove(enemyBullet)

    # 结束游戏

    def gameOver(self, text):
        print('谢谢使用，欢迎再次使用')
        exit()
    # 左上角文字的绘制

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
                self.gameOver('欢迎使用！')
            # 如果是键盘的按下
            if event.type == pygame.KEYDOWN:
                # 当我方坦克死亡或者不存在的时候
                if not MainGame.my_tank:
                    # 判断按下的是F1
                    if event.key == pygame.K_F1:
                        self.createMyTank()
                if MainGame.my_tank and MainGame.my_tank.live:
                    # 判断按下的是上、下、左、右
                    if event.key == pygame.K_LEFT:
                        # 切换方向
                        MainGame.my_tank.direction = 'L'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                    elif event.key == pygame.K_RIGHT:
                        # 切换方向
                        MainGame.my_tank.direction = 'R'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                    elif event.key == pygame.K_UP:
                        # 切换方向
                        MainGame.my_tank.direction = 'U'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                    elif event.key == pygame.K_DOWN:
                        # 切换方向
                        MainGame.my_tank.direction = 'D'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                    elif event.key == pygame.K_SPACE:
                        # 如果 当前我方子弹列表的大小 小于等于3才创建我方坦克发射的子弹
                        if len(MainGame.myBulletList) < 3:
                            myBullet = Bullet(MainGame.my_tank)
                            MainGame.myBulletList.append(myBullet)
            # 松开方向键，坦克停止移动，修改坦克的移动开关
            if event.type == pygame.KEYUP:
                # 判断松开的是上、下、左、右的时候才停止坦克移动
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if MainGame.my_tank and MainGame.my_tank.live:
                        MainGame.my_tank.stop = True
# 坦克类


class Tank(BaseItem):
    # 添加距离左边Left  距离上边top
    def __init__(self, left, top):
        # print("文件夹目录"+basedir)
        # 保存加载的图片
        self.images = {
            'U': pygame.image.load(basedir+'/images/tank_1p_up.jpg'),
            'D': pygame.image.load(basedir+'/images/tank_1p_down.jpg'),
            'L': pygame.image.load(basedir+'/images/tank_1p_left.jpg'),
            'R': pygame.image.load(basedir+'/images/tank_1p_right.jpg')
        }
        # 方向
        self.direction = 'L'
        # 根据当前图片的方向获取图片 surface
        self.image = self.images[self.direction]
        # 根据图片获取区域
        self.rect = self.image.get_rect()
        # 设置区域的left和top
        self.rect.left = left
        self.rect.top = top
        # 速度 决定了移动的快慢
        self.speed = 8
        # 坦克移动的开关
        self.stop = True
        # 是否活着
        self.live = True

    # 移动

    def move(self):
        # 判断坦克的方向来进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height + self.speed < SCREEN_HEIGHT:
                self.rect.top += self.speed

    # 射击
    def shot(self):
        return Bullet(self)
    # 展示坦克的方法

    def display(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        MainGame.window.blit(self.image, self.rect)

# 我方坦克


class MyTank(Tank):
    def __init__(self):
        pass
# 敌方坦克


class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        # 调用父类的初始化方法
        super(EnemyTank, self).__init__(left, top)
        # 加载图片集
        self.images = {
            'U': pygame.image.load(basedir+'/images/enemy_1_up.png'),
            'D': pygame.image.load(basedir+'/images/enemy_1_down.png'),
            'L': pygame.image.load(basedir+'/images/enemy_1_left.png'),
            'R': pygame.image.load(basedir+'/images/enemy_1_right.png'),
        }
        # 方向,随机生成敌方坦克的方向
        self.direction = self.randDirection()
        # 根据方向获取图片
        self.image = self.images[self.direction]
        # 区域
        self.rect = self.image.get_rect()
        # 对left和top进行赋值
        self.rect.left = left
        self.rect.top = top
        # 速度
        self.speed = speed
        # 移动开关键
        self.stop = True
        # 新增一个步数变量
        self.step = ENEMY_STEP

    # 随机生成方向
    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'
    # 敌方坦克随机移动的方法

    def randMove(self):
        if self.step <= 0:
            # 修改方向
            self.direction = self.randDirection()
            self.step = ENEMY_STEP
        else:
            self.move()
            # 让步数递减
            self.step -= 1
    # 重写shot()

    def shot(self):
        # 随机生成100以内的数
        num = random.randint(1, 100)
        if num < 10:
            return Bullet(self)
# 子弹类


class Bullet(BaseItem):
    def __init__(self, tank):
        # 加载图片
        self.image = pygame.image.load(basedir+'/images/bullet.png')
        # 坦克的方向决定 子弹的方向
        self.direction = tank.direction
        # 获取区域
        self.rect = self.image.get_rect()
        # 子弹的left和top与方向有关
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2-self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width/2-self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height-self.rect.width/2
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.width/2
        # 子弹的速度
        self.speed = 15
        # 子弹的状态，是否碰到墙壁，如果碰到墙壁，修改此状态
        self.live = True
    # 移动

    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 修改子弹的状态
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                # 修改子弹的状态
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                # 修改子弹的状态
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                # 修改子弹的状态
                self.live = False
    # 子弹是否碰撞墙壁

    def hitWall(self):
        # 遍历墙壁列表
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self, wall):
                # 发生碰撞,修改子弹的生存状态，让子弹消失
                wall.live = False
                #墙壁的生命值减少
                wall.hp -= 1
                if wall.hp <= 0:
                    #修改墙壁的生存状态
                    wall.live = False

    # 显示子弹的方法

    def display(self):
        # 将图片surface加载到窗口
        MainGame.window.blit(self.image, self.rect)

    # 我方子弹和敌方坦克的碰撞
    def myBullet_hit_enemyTank(self):
        # 遍历敌方坦克列表，判断是否发生碰撞
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(enemyTank, self):
                # 修改敌方坦克和我方子弹的状态
                enemyTank.live = False
                self.live = False
                # 创建爆炸对象
                explode = Explode(enemyTank)
                # 将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)
    # 敌方子弹与我方坦克的碰撞

    def enemyBullet_hit_myTank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank, self):
                # 产生爆炸对象
                explode = Explode(MainGame.my_tank)
                # 将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)
                # 修改敌方子弹与我方坦克的状态
                self.live = False
                MainGame.my_tank.live = False
# 墙壁类


class Wall():
    def __init__(self, left, top):
        # 加载墙壁图片
        self.image = pygame.image.load(basedir+'/images/wall.png')
        # 获取墙壁的区域
        self.rect = self.image.get_rect()
        # 设置位置 left top
        self.rect.left = left
        self.rect.top = top
        # 是否存活
        self.live = True
        # 设置生命值
        self.hp = 3

    # 展示墙壁的方法

    def display(self):
        MainGame.window.blit(self.image, self.rect)
# 爆炸效果类


class Explode():
    def __init__(self, tank):
        # 爆炸的位置由当前子弹击中的坦克的位置来决定
        self.rect = tank.rect
        self.images = [
            pygame.image.load(basedir+'/images/blast1.png'),
            pygame.image.load(basedir+'/images/blast2.png'),
            pygame.image.load(basedir+'/images/blast3.png'),
        ]
        self.step = 0
        self.image = self.images[self.step]
        # 是否活着
        self.live = True

    # 展示爆炸效果的方法

    def display(self):
        if self.step < len(self.images):
            # 根据索引获取爆炸对象
            self.image = self.images[self.step]
            self.step += 1
            # 添加到主窗口
            MainGame.window.blit(self.image, self.rect)
        else:
            # 修改活着的状态
            self.live = False
            self.step = 0

# 音效类


class Music():
    def __init__(self):
        pass
    # 播放音乐的方法

    def play(self):
        pass


if __name__ == '__main__':
    MainGame().startGame()
    # MainGame().getTextSurface()
