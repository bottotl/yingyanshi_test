# coding: utf-8

import wda
from PIL import Image
import aircv as ac
import time
import random

screen_image_path = './imageCache/screen.png'

class Action(object):
    def __init__(self, client):
        global s
        global c
        global sWidth
        global sHeight
        self.client = c = client
        self.session = s = c.session()
        size = s.window_size()
        sWidth = size.width * s.scale
        sHeight = size.height * s.scale
        print s

    def find_all_image_position(self, origin='origin.png', query='query.png', confidence=0.7):
        imsrc = ac.imread(origin) # 原始图像
        imsch = ac.imread(query) # 带查找的部分
        posArray = ac.find_all_template(imsrc, imsch)
        t = []
        for pos in posArray:
        	if pos['confidence'] > confidence:
        		t.append(pos['result'])
        return t

    def find_all_image_position2(self, origin='origin.png', query='query.png', confidence=0.8):
        imsrc = ac.imread(origin) # 原始图像
        imsch = ac.imread(query) # 带查找的部分
        posArray = ac.find_all_template(imsrc, imsch)
        t = []
        for pos in posArray:
            if pos['confidence'] > confidence:
                t.append(pos)
        return t


    def find_image_position(self, origin='origin.png', query='query.png'):
        imsrc = ac.imread(origin) # 原始图像
        imsch = ac.imread(query) # 带查找的部分
        posArray = ac.find_all_template(imsrc, imsch)
        if len(posArray) == 0:
            return None
        t = posArray[0]
        for pos in posArray:
            if t == None:
                t = pos
            else:
                if pos['confidence'] > t['confidence']:
                    t = pos
        print 'find', t
        return t

    def cImage(self, image):
        c.screenshot(screen_image_path)
        img = self.find_image_position(screen_image_path, image)
        self.errorCheck()
        if img:
            pos = img['result']
            self.click(pos)

    def errorCheck(self):
        c.screenshot(screen_image_path)
        imgs = self.find_all_image_position2(screen_image_path, "./imageCache/拒绝.png",)
        if len(imgs) > 0:
            print '该死的，别邀请我啊！'
            pos = imgs[0]['result']
            m = (pos[0] + random.uniform(1, 5.4)) / s.scale
            n = (pos[1] + random.uniform(1.1,5.4)) / s.scale
            s.tap(m, n)
            time.sleep(2)


    def exists(self, image):
        c.screenshot(screen_image_path)
        posArray = self.find_all_image_position(screen_image_path, image)
        print image, '查找到---' ,len(posArray)
        self.errorCheck()
        if len(posArray) > 0:
            print posArray
            return True
        return False

    def screenshot(self):
        c.screenshot(screen_image_path)

    def click(self, pos):
        self.errorCheck()
        m = (pos[0] + random.uniform(1, 5.4)) / s.scale
        n = (pos[1] + random.uniform(1, 5.4)) / s.scale
        print 'click ', m, n
        s.tap(m, n)

    def swipe(self, x1, y1, x2, y2):
        w, h = s.window_size()
        a = (x1 + random.uniform(1, 5.4))/ s.scale / w
        b = (y1 + random.uniform(1, 5.4))/ s.scale / h
        c = (x2 + random.uniform(1, 5.4))/ s.scale / w
        d = (y2 + random.uniform(1, 5.4))/ s.scale / h
        s.swipe(a, b, c, d, 0.5)

    def tupoUserPositions():
        c.screenshot(screen_image_path)
        t = find_all_image_position(screen_image_path, "未突破用户.png", 0.8)
        print "find users %d" %(len(t))
        return t

    def wait_attack_end(self):
        while 1:
            click_image("zhunbei.750x1334.png")
            d.keep_screen()
            success = d.exists("yuhunjieshu_4.750x1334.png")
            fail = d.exists("shibai_jixu.750x1334.png")
            if success != None:
                c.screenshot("yuhunjieshu_success_snapshot.png")
            if fail != None:
                c.screenshot("yuhunjieshu_fail_snapshot.png")
            d.free_screen()
            if (success != None) | (fail != None):
                print "find attack end flag, try to clear all end flag"
                time.sleep(4)
                while (success != None) | (fail != None):
                    success = click_image("yuhunjieshu_4.750x1334.png")
                    fail = click_image("shibai_jixu.750x1334.png")
                print "attack did end ~~~ "
                return

    # 等到图片消失
    def wait_image(self, image):
        c.screenshot(screen_image_path)
        r = self.find_image_position(screen_image_path, image)
        if (r != None):
            pos = r['result']
            while pos:
                self.click(pos)
                time.sleep(2)
                c.screenshot(screen_image_path)
                imageResult = self.find_image_position(screen_image_path, image)
                if imageResult:
                    if imageResult['confidence'] > 0.7:
                        pos = imageResult['result']
                    else:
                        pos = None
                else:
                    pos = None
        print image + ' === did disappear'

    def tansuo_28(self):
        self.backHome()
        self.wait_image('./imageCache/探索入口.png')
        self.wait_image('./imageCache/第二十八章.png')
        for x in xrange(1,10):
            if self.exists('./imageCache/第二十八章.png'):
                self.wait_image('./imageCache/第二十八章.png')
            self.wait_image('./imageCache/第二十八章_探索_按钮.png')
            print '激动人心的时刻，开始清理小怪'
            if self.goRightIfNeeded() == False:
                print '找不到小怪，开始尝试回到探索入口'
                if self.isInTansuo_28() == True:
                    self.cImage('./imageCache/return_btn.png')
                    self.cImage('./imageCache/确认退出探索.png')
                    time.sleep(2)
                    self.cImage('./imageCache/确认退出探索.png')
                    time.sleep(2)
                    backToTansuoEntrance = self.exists('./imageCache/第二十八章_探索_按钮.png')
                    backToTansuoHome = self.exists('./imageCache/第二十八章.png')
                    if (backToTansuoHome == False) & (backToTansuoEntrance == False):
                        self.stopAll()

                    if backToTansuoHome == True:
                        self.wait_image('./imageCache/第二十八章.png')
                    self.wait_image('./imageCache/第二十八章_探索_按钮.png')
                    print '成功返回探索入口，开始下一轮探索'
            else:
                self.find_guaiwu()

    def isInTansuo_28(self):
        return self.exists('./imageCache/固定阵容.png')


    def isBackToTansuo28Entrance(self):
        return self.exists('./imageCache/第二十八章_探索_按钮.png')

    def attackToEnd(self):
        print '死战到底！'
        while self.goRightIfNeeded():
            pass
        

    def checkTansuoIsFinished(self):
        time.sleep(2)
        if self.exists('./imageCache/探索小宝箱.png') == True:
            return True
        if self.exists('./imageCache/第二十八章_探索_按钮.png') == True:
            return

    def stopAll(self):
        c.home()

    def goRightIfNeeded(self):
        for x in xrange(1, 5):
            if self.exists('./imageCache/小怪标记.png') == False | self.exists('./imageCache/boss标记.png') == False:
                time.sleep(1)
                print '没找到可以攻击的目标，向右走第', x, '次'
                self.goRight()
            else:
                return True
        print '找不到怪物'
        return False

    def goRight(self):
        self.click([882 , 542])

    def find_guaiwu(self):
        print '查找怪物中'
        isBoss = False
        while 1:
            if self.exists('./imageCache/boss标记.png') == True:
                isBoss = True
                break
            elif self.exists('./imageCache/小怪标记.png') == True:
                isBoss = False
                break
            else:
                if self.exists('./imageCache/战斗_准备按钮.png') == True:
                    break
                pass
        while self.exists('./imageCache/固定阵容.png'):
            if isBoss:
                self.wait_image('./imageCache/boss标记.png')
            else:
                self.wait_image('./imageCache/小怪标记.png')

        print '战斗开始'
        time.sleep(3)
        babyMaxLevelCount = self.babyMaxLevelCount()
        print '当前满级宠物数量====', babyMaxLevelCount
        if babyMaxLevelCount >= 2:
            print '宝宝满级切换中'
            while self.exists('./imageCache/全部按钮.png') == False:
                    self.click([515, 565])
                    time.sleep(4)
            print "尝试点击全部按钮"
            while self.exists('./imageCache/素材卡列表.png') == False:
                time.sleep(1)
                self.cImage('./imageCache/全部按钮.png')
                time.sleep(2)
            self.cImage('./imageCache/素材卡列表.png')
            self.changeBaby()
            self.cImage('./imageCache/战斗_准备按钮.png')
        self.cImage('./imageCache/战斗_准备按钮.png')
        time.sleep(2)
        self.waitAttackEnd()
    
    def changeBaby(self):
        self.swipe(871, 631, 479, 602)
        time.sleep(2)
        self.swipe(871, 631, 479, 602)
        time.sleep(1)
        self.swipe(632, 609, 214, 390)
        time.sleep(2)
        self.swipe(770, 609, 666, 374)
        time.sleep(2)

    def babyMaxLevelCount(self):
        c.screenshot(screen_image_path)
        babys = self.find_all_image_position(screen_image_path, './imageCache/满级.png', 0.5)
        if babys:
            return len(babys)
        return 0


    def waitAttackEnd(self):
        while self.exists('./imageCache/战斗结束_魂.png') == False:
            self.cImage('./imageCache/战斗胜利.png')
        self.wait_image('./imageCache/战斗结束_魂.png')
        print '开心，打完了一只小怪，回到主界面，开始寻找下一只'


    def startJiacheng(self, image, confidence=0.7):
        # 进入加成页面
        while self.exists('./imageCache/经验加成.png') == False:
            self.cImage("./imageCache/加成入口.png")
            time.sleep(0.5)

        #关闭所有加成
        time.sleep(1)
        c.screenshot(screen_image_path) # Save screenshot as file
        runnings = self.find_all_image_position(screen_image_path, "./imageCache/加成开启.png")
        for run in runnings:
            print "关闭加成"
            self.click(run)
            time.sleep(1)

        print "开始打开加成"
        #查找加成开关
        c.screenshot('screen_image_path') # Save screenshot as file
        t_btns = self.find_all_image_position(screen_image_path, "./imageCache/加成暂停.png", 0.8)
        print "加成暂停按钮如下"
        print t_btns

        icons = self.find_all_image_position(screen_image_path, image, confidence)
        print "找到加成 icon 如下", icons

        if len(icons):
            for icon in icons:
                print icon
                target = None
                dis = 9999
                for btn in t_btns:
                    print btn
                    tDis = abs(btn[0] - icon[0])
                    print("tDis=",tDis,"dis=",dis, "btn =", btn)
                    if tDis < dis:
                        dis = tDis
                        target = btn
                        print(target,"= btn")

                print "target = ", target

                time.sleep(1)
                self.click(target)
        # 退出加成页面
        # while self.exists('./imageCache/探索入口.png') == False:
        #     self.cImage('./imageCache/加成入口.png')


    def backHome(self):
        c.screenshot(screen_image_path)
        t = []
        rBtn = self.find_all_image_position2(screen_image_path, './imageCache/return_btn.png')
        cBtn = self.find_all_image_position2(screen_image_path, './imageCache/close.png')
        c1Btn = self.find_all_image_position2(screen_image_path, './imageCache/close_1.png')
        confirmBtn = self.find_all_image_position2(screen_image_path, './imageCache/确认按钮.png')
        if len(rBtn) > 0:
            print '发现返回按钮', rBtn[0]
        if len(cBtn) > 0:
            print '发现关闭按钮', cBtn[0]
        if len(c1Btn) > 0:
            print '发现关闭按钮', c1Btn[0]
        if len(confirmBtn) > 0:
            print '发现确认按钮', confirmBtn[0]

        mostLikilyBtn = None
        for x in rBtn:
            if mostLikilyBtn == None:
                mostLikilyBtn = x
            else:
                mostLikilyBtn['confidence'] < x['confidence']
                mostLikilyBtn = x
                print 'current btn is return'

        for x in cBtn:
            if mostLikilyBtn == None:
                mostLikilyBtn = x
            else:
                mostLikilyBtn['confidence'] < x['confidence']
                mostLikilyBtn = x
                print 'current btn is close'

        for x in c1Btn:
            if mostLikilyBtn == None:
                mostLikilyBtn = x
            else:
                mostLikilyBtn['confidence'] < x['confidence']
                mostLikilyBtn = x
                print 'current btn is close'

        for x in confirmBtn:
            if mostLikilyBtn == None:
                mostLikilyBtn = x
            else:
                mostLikilyBtn['confidence'] < x['confidence']
                mostLikilyBtn = x
                print '确认按钮'

        print 'mostLikilyBtn is ', mostLikilyBtn
        if mostLikilyBtn != None:
            pos = mostLikilyBtn['result']
            self.click(pos)
            time.sleep(2)
            self.backHome()
