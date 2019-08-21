# coding: utf-8

import wda
from action import action

c = wda.Client('http://172.18.40.68:8100') # 公司
#c = wda.Client('http://192.168.2.192:8100') #家里
# c = wda.Client('http://172.18.49.121:8100') # platform也可以不指定


ac = action.Action(c)
print(ac.client.status())

# ac.cImage('./imageCache/探索入口.png')
#ac.exists('./imageCache/探索入口.png') 
# ac.screenshot()
# ac.startJiacheng('./imageCache/经验加成.png')
while 1:
    ac.tansuo_28()
# ac.stopAll()
# ac.find_xiaoguai()
# ac.waitAttackEnd()
# ac.goRight()
# ac.tansuo_28()
# ac.wait_image('./imageCache/探索入口.png')
def gerentupo():
        ac.backHome()
        ac.wait_image('./imageCache/结界突破.png')
        time.sleep(2)
        ac.cImage('./imageCache/个人突破入口.png')

        users = tupoUserPositions()
        i = 0
        while i < 2:
            for user in users:
                print 'enter loop'
                while ac.exists("tupo_jingong.750x1334.png"):
                    ac.cImage("yuhunjieshu_4.750x1334.png")
                    ac.cImage("shibai_jixu.750x1334.png")
                    ac.click(user)
                    time.sleep(2)

                ac.cImage("tupo_jingong.750x1334.png")
                time.sleep(2)

                if ac.exists("tupo_jingong.750x1334.png"):
                    print "can not continue tupo, end topo"
                    click(600, 78)
                    return
                    
                wait_attack_end()

            ac.cImage("tupo_shuaxin.750x1334.png")
            time.sleep(2)
            ac.cImage("tupo_queding.750x1334.png")
            time.sleep(2)
            users = tupoUserPositions()
            if len(users) < 1:
                i = i+1
                print "find more user to kill"
        time.sleep(2)
        ac.cImage("yuhunjieshu_4.750x1334.png")
        time.sleep(2)
        ac.cImage("yuhunjieshu_4.750x1334.png")
        print "no more user to kill"