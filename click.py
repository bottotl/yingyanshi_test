# coding: utf-8
import atx
import time
import aircv as ac
import random
import os
import global_var_model as gl


# d = atx.connect('http://192.168.0.101:8100', platform='ios') # platform也可以不指定
d = atx.connect('http://172.18.40.25:8100', platform='ios') # platform也可以不指定
dis = d.display

def swipe(x1, y1, x2, y2):
	dis = d.display
	y11 = dis.height - x1
	x11 = y1

	y22 = dis.height - x2
	x22 = y2

	d.swipe(x11, y11, x22, y22, 0.5)

def find_all_image_position(origin='origin.png', query='query.png', confidence=0.9):
    imsrc = ac.imread(origin) # 原始图像
    imsch = ac.imread(query) # 带查找的部分
    posArray = ac.find_all_template(imsrc, imsch)
    t = []
    for pos in posArray:
    	if pos['confidence'] > confidence:
    		t.append(pos['result'])
    return t

def click_image(image, disAppear=False, check=True):
	if disAppear == False:
		print("[DisAppear = False] try to find image", image)
		FindPoint = d.exists(image)
		if FindPoint != None:
			print(image)
			p_click(FindPoint)
			print("did click image", image)
			time.sleep(1)
			return FindPoint
		return FindPoint
	print("[DisAppear = True] try to find image", image)
	FindPoint = None
	while FindPoint == None:
		FindPoint = d.exists(image)

	while FindPoint != None:
		print("did find image", image)
		FindPoint = d.exists(image)
		if FindPoint != None:
			p_click(FindPoint, check)
			print("did click image", image)
			time.sleep(1)
		FindPoint = d.exists(image)
	

def wait_image(image, disAppear=False, check=True):
	FindPoint = None
	while FindPoint is None:
		print image
		print 'waiting...'
		FindPoint = d.exists(image)
	print('did find', image)
	click_image(image, disAppear, check)

def check_xuanshang():
	if d.exists("xuanshang_flag.750x1334.png") != None:
		print "warning !! warning !!! xuan shang is comming"
		time.sleep(1)
		dis = d.display
		y = dis.height - 206
		x = 896
		print "jujue xuanchang"
		d.click(x, y)
		time.sleep(2)
		if d.exists("xuanshang_flag.750x1334.png") == None:
			print "jujue xuanshang"
		else:
			print "error!!! error!!!"
			d.screenshot('screen.1920x1080.png') # Save screenshot as file
			d.home()


def p_click(FindPoint, check=True):
	dis = d.display
	y = dis.height - FindPoint.pos[0] + random.random()*5
	x = FindPoint.pos[1] + random.random()*4
	# print("click (%f, %f)" % (x, y))
	if gl.lastClick == None:
		gl.lastClick = { 'x' : x, 'y' : y}
	elif check == True:
		clickCheck(x, y)
	else:
		pass
	check_xuanshang()
	d.click(x, y)

def clickCheck(x, y):
	if ((abs(gl.lastClick['x'] - x) < 3) & (abs(gl.lastClick['y'] - y) < 3)):
		gl.dClickCount = gl.dClickCount + 1
		print "【click same position】【error】!!!"
	else:
		gl.dClickCount = gl.dClickCount - 1
		gl.dClickCount = max(gl.dClickCount, 0)

	if gl.dClickCount > 3:
		print "[error][error][error][error][error][error][error][error] try to stopAll!!!"
		d.screenshot('screen.1920x1080.png') # Save screenshot as file
		d.home()

def click_im(pos):
	dis = d.display
	y = dis.height - pos[0]
	x = pos[1]
	check_xuanshang()
	d.click(x + random.random()*5, y + random.random()*4)

def click(x1, y1, offset=True):
	dis = d.display
	y = dis.height - x1
	x = y1
	if offset:
		x = x + random.random()*5
		y = y + random.random()*4
	else:
		pass
	print("click (%f, %f)" % (x, y))
	clickCheck(x, y)
	check_xuanshang()
	d.click(x, y)

	
def yeyuanhuo():
	wait_image("tiaozhan.750x1334.png")
	time.sleep(2)
	print 'enter loop'
	while d.exists("tiaozhan.750x1334.png") == None:
		# print '...'
		#click_image("zhunbei.750x1334.png")
		click_image("yuhunjieshu_4.750x1334.png")
		click_image("shibai_jixu.750x1334.png")
		if d.exists("tilibuzu_goumaitili.750x1334.png") != None:
			click_image("close_btn_tili_2.750x1334.png")
			time.sleep(2)
			d.home()

def yuhun():
	backHome()
	tansuo()
	wait_image("yuhun_entrance.750x1334.png")
	time.sleep(2)
	click_image("yuhun_dashe.750x1334.png")
	time.sleep(2)
	startJiacheng("jiacheng_yuhun.750x1334.png")
	i = 0
	while i<20:
		wait_image("tiaozhan.750x1334.png")
		time.sleep(2)
		print 'enter loop'
		while d.exists("tiaozhan.750x1334.png") == None:
			# print '...'
			click_image("zhunbei.750x1334.png")
			click_image("yuhunjieshu_4.750x1334.png")
			click_image("shibai_jixu.750x1334.png")
			if d.exists("tilibuzu_goumaitili.750x1334.png") != None:
				stopAll()
				i=100
		i = i+1

	stopJiacheng()
	print 'exit'

def stopAll():
	click_image("close_btn_tili_2.750x1334.png", False)
	time.sleep(2)
	while (d.exists("close_btn.750x1334.png") != None) | (d.exists("return_btn.750x1334.png") != None) | (d.exists("close_btn_1.750x1334.png") != None):
		click_image("close_btn.750x1334.png", False)
		click_image("close_btn_1.750x1334.png", False)
		click_image("return_btn.750x1334.png", False)
		click_image("tuichu_tansuo_queren.750x1334.png", False)
	# 进入加成页面
	wait_image("jiacheng_entrance_home.750x1334.png", False)
	#关闭所有加成
	time.sleep(2)
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	print "stop jiacheng"
	runnings = find_all_image_position("screen.1920x1080.png", "jiacheng_running.750x1334.png")
	print runnings
	for run in runnings:
		click(run[0], run[1], False)
		time.sleep(1)
	# 退出加成页面
	wait_image("jiacheng_entrance_home.750x1334.png", False)
	d.home()
	

def juexing():
	backHome()
	tansuo()
	wait_image("juexing_entrance.750x1334.png")
	time.sleep(2)
	wait_image("juexing_lei_qiling.750x1334.png")
	time.sleep(2)
	startJiacheng("jiacheng_juexing.750x1334.png")
	i = 0
	while i<10:
		wait_image("tiaozhan.750x1334.png")
		time.sleep(2)
		print 'enter loop'
		while d.exists("tiaozhan.750x1334.png") == None:
			# print '...'
			click_image("zhunbei.750x1334.png")
			click_image("yuhunjieshu_4.750x1334.png")
			click_image("shibai_jixu.750x1334.png")
			if d.exists("tilibuzu_goumaitili.750x1334.png") != None:
				stopAll()
				i=100
		i = i+1

	stopJiacheng()
	print 'exit'

def zudui():
	while 1:
		click_image("yuhunjieshu_4.750x1334.png")
		click_image("yuhunjieshu_3.750x1334.png")
		click_image("shibai_jixu.750x1334.png")

def backHome():
	while (d.exists("close_btn.750x1334.png") != None) | (d.exists("return_btn.750x1334.png") != None) | (d.exists("close_btn_1.750x1334.png") != None):
		click_image("close_btn.750x1334.png")
		click_image("close_btn_1.750x1334.png")
		click_image("return_btn.750x1334.png")
		click_image("tuichu_tansuo_queren.750x1334.png")


def tansuo():
	wait_image("tansuo_btn.750x1334.png", True)

# 突破结界
def geren_tupo():
	backHome()
	tansuo()
	wait_image("tupo_entrance.750x1334.png", True)
	time.sleep(2)
	click_image("tupo_geren.750x1334.png")
	time.sleep(2)

	users = tupoUserPositions()
	i = 0
	while i < 2:
		for user in users:
			print 'enter loop'
			while d.exists("tupo_jingong.750x1334.png") == None:
				click_image("yuhunjieshu_4.750x1334.png")
				click_image("shibai_jixu.750x1334.png")
				click_im(user)
				time.sleep(2)

			click_image("tupo_jingong.750x1334.png")
			time.sleep(2)

			if d.exists("tupo_jingong.750x1334.png") != None:
				print "can not continue tupo, end topo"
				click(600, 78)
				return
				
			wait_attack_end()

		click_image("tupo_shuaxin.750x1334.png")
		time.sleep(2)
		click_image("tupo_queding.750x1334.png")
		time.sleep(2)
		users = tupoUserPositions()
		if len(users) < 1:
			i = i+1
			print "find more user to kill"
	time.sleep(2)
	click_image("yuhunjieshu_4.750x1334.png")
	time.sleep(2)
	click_image("yuhunjieshu_4.750x1334.png")
	print "no more user to kill"


def yingyangliao_tupo():
	backHome()
	tansuo()
	wait_image("tupo_entrance.750x1334.png", True)
	time.sleep(2)
	click_image("tupo_geren.750x1334.png")
	time.sleep(2)
	click_image("tupo_yinyangliao.750x1334.png")
	time.sleep(2)
	users = tupoUserPositions()
	i = 0
	while i < 4:
		for user in users:
			wait_image("yinyangliao_tupo_selected.750x1334.png")
			click_im(user)
			print 'start topo'
			#check user status
			time.sleep(1)
			if d.exists("tupo_jingong.750x1334.png") == None:
				print "error !!!!!!!!"
				d.screenshot('screen.1920x1080.png') # Save screenshot as file
				stopAll()
			print "click attack once"
			click_image("tupo_jingong.750x1334.png")
			time.sleep(3)
			if d.exists("tupo_jingong.750x1334.png") != None:
				print "can not continue attack, start to back home"
				click(600, 78)
				backHome()
				return
			print "did start attack"
			wait_attack_end()
			time.sleep(4)

		time.sleep(1)
		swipe(148, 758, 590, 846)
		time.sleep(2)
		users = tupoUserPositions()
		if len(users) < 1:
			i = i+1
			print "find more user to kill"
	print "no more user to kill"

def wait_attack_end():
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
		
			
def switch_zidong_shoudong():
	click(58, 62)

def tupoUserPositions():
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	t = find_all_image_position("screen.1920x1080.png", "tupo_user_flag.750x1334.png", 0.8)
	print "find users %d" %(len(t))
	return t

def douji():
	return

def stopyuhunjiacheng():
	pass

def stopJiacheng():
	backHome()
	# 进入加成页面
	wait_image("jiacheng_entrance_home.750x1334.png")
	#关闭所有加成
	time.sleep(2)
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	print "stop jiacheng"
	runnings = find_all_image_position("screen.1920x1080.png", "jiacheng_running.750x1334.png")
	print runnings
	for run in runnings:
		click(run[0], run[1], False)
		time.sleep(1)
	# 退出加成页面
	wait_image("jiacheng_entrance_home.750x1334.png")


def startJiacheng(image):
	# 进入加成页面
	wait_image("jiacheng_entrance_2.750x1334.png")
	#关闭所有加成
	time.sleep(2)
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	runnings = find_all_image_position("screen.1920x1080.png", "jiacheng_running.750x1334.png")
	for run in runnings:
		print "stop jiacheng"
		click(run[0], run[1], False)
		time.sleep(1)

	print "start kaiqi jiacheng"
	#查找加成开关
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	t_btns = find_all_image_position("screen.1920x1080.png", "jiacheng_pauseing.750x1334.png")
	print t_btns

	icons = find_all_image_position("screen.1920x1080.png", image, 0.7)
	print("find jiacheng %d"%(len(icons)))
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

					print(target,"= btn")
			print("target = ", target)
			time.sleep(1)
			click(target[0], target[1], False)
	# 退出加成页面
	wait_image("jiacheng_entrance_2.750x1334.png")

def quick_click_image(image):
	d.keep_screen()
	pos = click_image(image)
	d.free_screen()
	return pos

def click_guild():
	d.keep_screen()
	FindPoint = click_image("hand_guild.750x1334.png")
	d.free_screen()

	dis = d.display
	y = dis.height - (FindPoint.pos[0] + 50)
	x = FindPoint.pos[1] - 50
	d.click(x, y)


def lianxiaohao():
	while 1:
		click_image("diandiandian.750x1334.png")
		click_image("diandiandian_2.750x1334.png")
		d.keep_screen()
		click_image("daxiaoguai_1.750x1334.png")
		click_image("juqing_yanjing.750x1334.png")
		click_image("juqing_wenhao.750x1334.png")
		click_image("skip.750x1334.png")
		click_image("zhunbei.750x1334.png")
		click_image("yuhunjieshu_4.750x1334.png")
		click_image("shibai_jixu.750x1334.png")
		click_image("quick_play.750x1334.png")
		click_image("xiaobai.750x1334.png")
		click_image("tupo_queding.750x1334.png")
		click_image("close_btn.750x1334.png")
		d.free_screen()
		# click_guild()

def change_gouliang():
	print "start change gouliang"
	while d.exists("zhunbei.750x1334.png") == None:
		pass
	while d.exists("gouliang_quanbu_btn.750x1334.png") == None:
		click(216, 486)
		time.sleep(1)
	
	while d.exists("gouliang_sucai_btn.750x1334.png") == None:
		wait_image("gouliang_quanbu_btn.750x1334.png")
		time.sleep(2)

	wait_image("gouliang_sucai_btn.750x1334.png")
	swipe(148, 884, 126, 352)#左滑一段距离
	time.sleep(1)
	swipe(134, 374, 370, 194)#替换第一张狗粮
	time.sleep(2)
	swipe(138, 618, 364, 582)#替换第二张狗粮
	print "end change gouliang"

def change_gouliang_and_start():
	print "change_gouliang_and_start"
	while d.exists("zhunbei.750x1334.png") == None:
		pass
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	t = find_all_image_position("screen.1920x1080.png", "gouliang_manji.750x1334.png", 0.8)
	if len(t)>1:
		print "need change gouliang"
		change_gouliang()
			
	click_image("zhunbei.750x1334.png")
	print "change gouliang end"

def tansuo_find_boss():
	while (d.exists("tansuo_daguai.750x1334.png") == None) & (d.exists("daxiaoguai_3.750x1334.png") == None):
		print "no boss to attack, move right"
		offset = random.random() * 10
		click(140 + offset, 920 + offset)
		time.sleep(1)
		return False

	print 'have boss, start find'

	while (d.exists("zhunbei.750x1334.png") == None):
		if (click_image("tansuo_daguai.750x1334.png") == None) & (click_image("daxiaoguai_3.750x1334.png") == None) :
			print "move right"
			offset = random.random() * 10
			click(140 + offset, 920 + offset)
			time.sleep(1)
		if d.exists("tilibuzu_goumaitili.750x1334.png") != None:
			stopAll()
			return False
		if (d.exists("tansuo_xiao_baoxiang.750x1334.png") != None) | (d.exists("tansuo_huodejiangli.750x1334.png") != None):
			return False

	return True

def tansuo_find():
	if d.exists("tansuo_xiao_baoxiang.750x1334.png") != None:#结束以后点击宝箱
		while (d.exists("tansuo_xiao_baoxiang.750x1334.png") != None) | (d.exists("tansuo_huodejiangli.750x1334.png") != None):
			click_image("tansuo_xiao_baoxiang.750x1334.png")
			time.sleep(2)
			if d.exists("tansuo_huodejiangli.750x1334.png") != None:
				click(330, 1160)
				print "jiang li"
				time.sleep(2)
	elif d.exists("return_btn.750x1334.png") != None:#找怪物
		if tansuo_find_boss():
			print "find boss"
			if d.exists("tilibuzu_goumaitili.750x1334.png") != None:
				stopAll()
			change_gouliang_and_start()
	else:#退出战斗界面
		print "maybe attacking"
		click_image("zhunbei.750x1334.png")
		click_image("yuhunjieshu_3.750x1334.png")
		time.sleep(2)
		click_image("yuhunjieshu_4.750x1334.png")
		click_image("yuhunjieshu_4.750x1334.png")
		click_image("shibai_jixu.750x1334.png")

def zzz_douji():
	enter = "zzz_pipei.750x1334.png"#匹配按钮
	lijijiechu = "lijijiechu.750x1334.png"#立即解除
	quxiao = "zzz_quxiao.750x1334.png"#取消
	zidongshangzhen = "douji_zidongshangzheng.750x1334.png"#自动上阵
	shoudong2zidong = "douji_shoudong_2_zidong.750x1334.png"#手动改自动

	# click_image(lijijiechu)
	# click_image(quxiao)
	# click_image(enter)
	d.keep_screen()
	click_image("douji_zhan.750x1334.png")
	click_image(zidongshangzhen)
	click_image(shoudong2zidong)
	click_image("zhunbei.750x1334.png")
	click_image("zzz_end.750x1334.png")
	click_image("douji_shibai.750x1334.png")
	# click_image("zzz_end_jiutun.750x1334.png")
	click_image("zzz_end_jiangli.750x1334.png")
	d.free_screen()

def tansuoEntranceIfNeeded(level):
	if d.exists("tansuo_home_flag.750x1334.png") != None:
		print "in tansuo home, go tansuo entrance"
		while click_image(level) != None:
			time.sleep(2)
			pass
		print("did enter", level)


def isTansuoFinished():
	if (d.exists("tansuo_home_flag.750x1334.png") != None) | (d.exists("tansuo_entrance_flag.750x1334.png") != None):
		print "tansuo finished"
		return True
	return False
		

def tansuo_once(level):
	tansuoEntranceIfNeeded(level)
	time.sleep(2)
	click_image("tansuo.750x1334.png", True)
	print "start tansuo"
	while isTansuoFinished() == False:
		tansuo_find()
		print "enter loop"

	while d.exists("tansuo_home_flag.750x1334.png") == None:
		print "try go back tansuo home"
		click_image("close_btn_1.750x1334.png")
		
	print "did go back tansuo home"
	if click_image("tansuo_baoxiang_big.750x1334.png") != None:
		time.sleep(3)
		click_image("yuhunjieshu_4.750x1334.png")


def tansuo_lianji_28():

	backHome()
	tansuo()
	time.sleep(2)
	startJiacheng("jiacheng_jingyan.750x1334.png")
	i = 0
	while i < 5:
		i = i + 1
		tansuo_once("tansuo_level_28.750x1334.png")
	stopJiacheng()

def tansuo_lianji_18():
	# backHome()
	# tansuo()
	# time.sleep(2)
	while click_image("tansuo_level_10.750x1334.png") != None:
		pass
	
	# startJiacheng("jiacheng_jingyan.750x1334.png")
	while 1:
		if click_image("tansuo_baoxiang_big.750x1334.png") != None:
			time.sleep(5)
			click_image("yuhunjieshu_4.750x1334.png")

		if click_image("tansuo_level_10.750x1334.png") != None:
			time.sleep(3)
			click_image("tansuo_start.750x1334.png")
			tansuo_find()
		elif click_image("tansuo_start.750x1334.png") != None:
			tansuo_find()
	# stopJiacheng()

def random_click():
	minX = 258
	maxX = 438
	minY = 188
	maxY = 1140
	x = random.uniform(minX, maxX)
	y = random.uniform(minY, maxY)
	click(x, y)

def baigui_yaoqing():
	i = 0
	flag = 0
	while d.exists("baigui_kaishi.750x1334.png") == None:
		while d.exists("baigui_yaoqing_start.750x1334.png") != None:
			click_image("baigui_yaoqing_start.750x1334.png")
			if d.exists("baigui_user_list_flag.750x1334.png") != None:
				print "----- user list -----"
				users = [(474, 494), (490, 770),
						(388, 494), (398, 770),
						(316, 494), (310, 770),
						(226, 494), (228, 770)]
				index = random.randint(0, 7)
				for i in xrange(0, i):
					swipe(188, 666, 472, 661)
					time.sleep(0.1)
				print("index = ", index)
				user = users[index]
				click(user[0], user[1])
				while d.exists("baigui_user_list_flag.750x1334.png") != None:
					print "chose other"
					swipe(188, 666, 472, 661)
					user = users[random.randint(0, 7)]
					click(user[0], user[1])
		print "did invite friend"

		click_image("baigui_jinru.750x1334.png")
		print "start baigui"
		time.sleep(1)
		if d.exists("baigui_jinru.750x1334.png") != None:
			print "can not invite"
			flag = flag + 1
			if flag > 3:
				i = i + 1
				flag = 0
			click_image("baigui_yaoqing_cancel.750x1334.png", True)
		time.sleep(1)

def baigui():
	baigui_yaoqing()
	
	print "did enter gui wang chose"
	click(282, 670)
	click_image("baigui_kaishi.750x1334.png", True)

	swipe(62, 402, 56, 510)

	while 1:
		d.keep_screen()
		jinru = d.exists("baigui_jinru.750x1334.png") != None
		end = d.exists("baigui_end_flag.750x1334.png") != None
		kaishi = d.exists("baigui_kaishi.750x1334.png") != None
		d.free_screen()
		if jinru | end | kaishi:
			break
		i = 0
		while i < 7:
			random_click()
			i = i + 1

	click_image("baigui_end_flag.750x1334.png")
	print "end baigui"
		
print d.rotation
#lianxiaohao()
#kaiqijiacheng()
# while 1:
# tansuo_lianji_18()
# 	geren_tupo()
# while 1:
# 	print "start douji"
# 	zzz_douji() 
	
#stopAll()
i =  0
while 1:
	# baigui()
	i = i + 1
	yingyangliao_tupo()
	geren_tupo()
	juexing()
	# tansuo_lianji_28()
	
# d.home()
# d.click()
# while 1:
# 	yuhun()
	#zudui()


#d.click_image("tiaozhan.1334x750.png")tansuo