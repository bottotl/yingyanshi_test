# coding: utf-8

import wda
from PIL import Image
import aircv as ac
import time

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
        pos = self.find_image_position(screen_image_path, image)['result']
        self.click(pos)

    def exists(self, image):
        c.screenshot(screen_image_path)
        posArray = self.find_all_image_position(screen_image_path, image)
        print image, '查找到---' ,len(posArray)
        if len(posArray) > 0:
            print posArray
            return True
        return False

    def screenshot(self):
        c.screenshot(screen_image_path)

    def click(self, pos):
        m = pos[0] / s.scale
        n = pos[1] / s.scale
        print 'click ', m, n
        s.tap(m, n)

    def tupoUserPositions():
        c.screenshot(screen_image_path)
        t = find_all_image_position(screen_image_path, "未突破用户.png", 0.8)
        print "find users %d" %(len(t))
        return t

    def gerentupo(self):
        self.backHome()
        self.wait_image('./imageCache/结界突破.png')
        time.sleep(2)
        self.cImage('./imageCache/个人突破入口.png')

        users = tupoUserPositions()
        i = 0
        while i < 2:
            for user in users:
                print 'enter loop'
                while self.exists("tupo_jingong.750x1334.png"):
                    self.cImage("yuhunjieshu_4.750x1334.png")
                    self.cImage("shibai_jixu.750x1334.png")
                    self.click(user)
                    time.sleep(2)

                self.cImage("tupo_jingong.750x1334.png")
                time.sleep(2)

                if self.exists("tupo_jingong.750x1334.png"):
                    print "can not continue tupo, end topo"
                    click(600, 78)
                    return
                    
                wait_attack_end()

            self.cImage("tupo_shuaxin.750x1334.png")
            time.sleep(2)
            self.cImage("tupo_queding.750x1334.png")
            time.sleep(2)
            users = tupoUserPositions()
            if len(users) < 1:
                i = i+1
                print "find more user to kill"
        time.sleep(2)
        self.cImage("yuhunjieshu_4.750x1334.png")
        time.sleep(2)
        self.cImage("yuhunjieshu_4.750x1334.png")
        print "no more user to kill"

    def wait_attack_end(self):
        while 1:
            click_image("zhunbei.750x1334.png")
            d.keep_screen()
            success = d.exists("yuhunjieshu_4.750x1334.png")
            fail = d.exists("shibai_jixu.750x1334.png")
            if success != None:
                d.screenshot("yuhunjieshu_success_snapshot.png")
            if fail != None:
                d.screenshot("yuhunjieshu_fail_snapshot.png")
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
            self.wait_image('./imageCache/第二十八章_探索_按钮.png')
            print '激动人心的时刻，开始清理小怪'
            if self.goRightIfNeeded() == False:
                print '找不到小怪，开始尝试回到探索入口'
                if self.isInTansuo_28() == True:
                    self.cImage('./imageCache/return_btn.png')
                    self.cImage('./imageCache/确认退出探索.png')
                    time.sleep(2)
                    if self.exists('./imageCache/第二十八章_探索_按钮.png') == False:
                        self.stopAll()
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
                print '没找到可以攻击的目标，向右走第', x, '次'
                self.goRight()
            else:
                return True
        print '找不到怪物'
        return False

    def goRight(self):
        self.click([882, 542])

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
                pass
        if isBoss:
            self.wait_image('./imageCache/boss标记.png')
        else:
            self.wait_image('./imageCache/小怪标记.png')

        print '战斗开始'
        time.sleep(2)
        self.wait_image('./imageCache/战斗_准备按钮.png')
        time.sleep(2)
        self.waitAttackEnd()
    
    def waitAttackEnd(self):
        while self.exists('./imageCache/战斗结束_魂.png') == False:
            pass
        self.wait_image('./imageCache/战斗结束_魂.png')
        print '开心，打完了一只小怪，回到主界面，开始寻找下一只'



    def backHome(self):
        c.screenshot(screen_image_path)
        t = []
        rBtn = self.find_all_image_position2(screen_image_path, './imageCache/return_btn.png')
        cBtn = self.find_all_image_position2(screen_image_path, './imageCache/close.png')
        c1Btn = self.find_all_image_position2(screen_image_path, './imageCache/close_1.png')
        if len(rBtn) > 0:
            print '发现返回按钮', rBtn[0]
        if len(cBtn) > 0:
            print '发现关闭按钮', cBtn[0]
        if len(c1Btn) > 0:
            print '发现关闭按钮', c1Btn[0]

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

        print 'mostLikilyBtn is ', mostLikilyBtn
        if mostLikilyBtn != None:
            pos = mostLikilyBtn['result']
            self.click(pos)
            time.sleep(2)
            self.backHome()
