# coding: utf-8

import wda
from action import action

c = wda.Client('http://172.18.40.59:8100') # platform也可以不指定
ac = action.Action(c)
print(ac.client.status())

# ac.cImage('./imageCache/探索入口.png')
#ac.exists('./imageCache/探索入口.png')
ac.tansuo_28()
# ac.find_xiaoguai()
# ac.waitAttackEnd()
# ac.goRight()
# ac.tansuo_28()
# ac.wait_image('./imageCache/探索入口.png')