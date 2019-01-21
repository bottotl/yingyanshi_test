# coding: utf-8
import atx
import time
import aircv as ac
import random
import os


def swipe(d, x1, y1, x2, y2):
	dis = d.display
	y11 = dis.height - x1
	x11 = y1

	y22 = dis.height - x2;
	x22 = y2

	d.swipe(x11, y11, x22, y22, 0.5);

def find_all_image_position(origin='origin.png', query='query.png', confidence=0.9):
    imsrc = ac.imread(origin) # 原始图像
    imsch = ac.imread(query) # 带查找的部分
    posArray = ac.find_all_template(imsrc, imsch)
    t = []
    for pos in posArray:
    	if pos['confidence'] > confidence:
    		t.append(pos['result'])
    return t;

def click_image(d, image):
	FindPoint = d.exists(image)
	if FindPoint != None:
		print(image)
		p_click(d, FindPoint)
		time.sleep(1);
	return FindPoint

def wait_image(d, image):
	FindPoint = None
	while FindPoint is None:
		print image;
		print 'finding...'
		FindPoint = d.exists(image)
	p_click(d, FindPoint)
	print(image)
	return FindPoint

def p_click(d, FindPoint):
	dis = d.display
	y = dis.height - FindPoint.pos[0] + random.random()*5
	x = FindPoint.pos[1] + random.random()*4;
	# print("click (%f, %f)" % (x, y))
	d.click(x , y)

def click_im(d, pos):
	dis = d.display
	y = dis.height - pos[0]
	x = pos[1]
	d.click(x + random.random()*5, y + random.random()*4)

def click(d, x1, y1, offset=True):
	dis = d.display
	y = dis.height - x1
	x = y1
	if offset:
		x = x + random.random()*5;
		y = y + random.random()*4;
	else:
		pass
	print("click (%f, %f)" % (x, y))
	d.click(x, y);

	
def yeyuanhuo(d):
	wait_image(d, "tiaozhan.750x1334.png")
	time.sleep(2)
	print 'enter loop'
	while d.exists("tiaozhan.750x1334.png") == None:
		# print '...'
		#click_image(d, "zhunbei.750x1334.png")
		click_image(d, "yuhunjieshu_4.750x1334.png")
		click_image(d, "shibai_jixu.750x1334.png")
		if d.exists("tilibuzu_goumaitili.750x1334.png") != None:
			click_image(d, "close_btn_tili_2.750x1334.png");
			time.sleep(2);
			d.home();

def yuhun(d):
	backHome(d)
	tansuo(d)
	wait_image(d, "yuhun_entrance.750x1334.png")
	time.sleep(2);
	click_image(d, "yuhun_dashe.750x1334.png")
	time.sleep(2);
	startJiacheng(d, "jiacheng_yuhun.750x1334.png");
	i = 0
	while i<20:
		wait_image(d, "tiaozhan.750x1334.png")
		time.sleep(2)
		print 'enter loop'
		while d.exists("tiaozhan.750x1334.png") == None:
			# print '...'
			click_image(d, "zhunbei.750x1334.png")
			click_image(d, "yuhunjieshu_4.750x1334.png")
			click_image(d, "shibai_jixu.750x1334.png")
			if d.exists("tilibuzu_goumaitili.750x1334.png") != None:
				stopAll(d)
				i=100
		i = i+1;

	stopJiacheng(d);
	print 'exit'

def stopAll(d):
	click_image(d, "close_btn_tili_2.750x1334.png");
	time.sleep(2);
	backHome(d)
	stopJiacheng(d);
	d.home();
	

def juexing(d):
	if d.exists("tiaozhan.750x1334.png") != None:
		click_image(d, "tiaozhan.750x1334.png");
		time.sleep(2);
		while d.exists("tiaozhan.750x1334.png") == None:
			click_image(d, "zhunbei.750x1334.png")
			click_image(d, "yuhunjieshu_4.750x1334.png")
			click_image(d, "shibai_jixu.750x1334.png")

def zudui(d):
	while 1:
		click_image(d, "yuhunjieshu_4.750x1334.png")
		click_image(d, "yuhunjieshu_3.750x1334.png")
		click_image(d, "shibai_jixu.750x1334.png")

def backHome(d):
	while (d.exists("close_btn.750x1334.png") != None) | (d.exists("return_btn.750x1334.png") != None) | (d.exists("close_btn_1.750x1334.png") != None):
		click_image(d, "close_btn.750x1334.png")
		click_image(d, "close_btn_1.750x1334.png")
		click_image(d, "return_btn.750x1334.png")


def tansuo(d):
	wait_image(d, "tansuo_btn.750x1334.png")

# 突破结界
def geren_tupo(d):
	backHome(d)
	tansuo(d)
	wait_image(d, "tupo_entrance.750x1334.png")
	time.sleep(2);
	click_image(d, "tupo_geren.750x1334.png")
	time.sleep(2);

	users = tupoUserPositions(d)
	i = 0;
	while i < 2:
		for user in users:
			print 'enter loop'
			while d.exists("tupo_jingong.750x1334.png") == None:
				click_image(d, "yuhunjieshu_4.750x1334.png")
				click_image(d, "shibai_jixu.750x1334.png")
				click_im(d, user)
				time.sleep(2);

			click_image(d, "tupo_jingong.750x1334.png")
			time.sleep(2);
			while 1:
				if d.exists("tupo_jingong.750x1334.png"):
					print "can not continue tupo, end topo";
					click(d, 600, 78);
					return;

				click_image(d, "zhunbei.750x1334.png")
				if (click_image(d, "yuhunjieshu_4.750x1334.png") != None) | (click_image(d, "shibai_jixu.750x1334.png") != None):
					time.sleep(3);
					break;
		click_image(d, "tupo_shuaxin.750x1334.png");
		time.sleep(2);
		click_image(d, "tupo_queding.750x1334.png");
		time.sleep(2);
		users = tupoUserPositions(d);
		if len(users) < 1:
			i = i+1;
			print "find more user to kill"
	time.sleep(2)
	click_image(d, "yuhunjieshu_4.750x1334.png")
	time.sleep(2);
	click_image(d, "yuhunjieshu_4.750x1334.png")
	print "no more user to kill"

def yingyangliao_tupo(d):
	backHome(d)
	tansuo(d)
	wait_image(d, "tupo_entrance.750x1334.png")
	time.sleep(2);
	click_image(d, "tupo_geren.750x1334.png")
	time.sleep(2);
	click_image(d, "tupo_yinyangliao.750x1334.png")
	time.sleep(2);
	users = tupoUserPositions(d)
	i = 0;
	while i < 4:
		for user in users:
			print 'enter loop'
			while d.exists("tupo_jingong.750x1334.png") == None:
				click_image(d, "yuhunjieshu_4.750x1334.png")
				click_image(d, "shibai_jixu.750x1334.png")
				click_im(d, user)
				time.sleep(2);

			click_image(d, "tupo_jingong.750x1334.png")
			time.sleep(2);
			while 1:
				if d.exists("tupo_jingong.750x1334.png"):
					print "can not continue tupo, end topo";
					click(d, 600, 78);
					return;

				click_image(d, "zhunbei.750x1334.png")
				if (click_image(d, "yuhunjieshu_4.750x1334.png") != None) | (click_image(d, "shibai_jixu.750x1334.png") != None):
					break;
		time.sleep(1);
		swipe(d, 148, 758, 590, 846);
		time.sleep(2);
		users = tupoUserPositions(d);
		if len(users) < 1:
			i = i+1;
			print "find more user to kill"
	click_image(d, "yuhunjieshu_4.750x1334.png")
	time.sleep(2)
	click_image(d, "shibai_jixu.750x1334.png")
	time.sleep(2)
	print "no more user to kill"


def switch_zidong_shoudong(d):
	click(d, 58, 62);

def tupoUserPositions(d):
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	t = find_all_image_position("screen.1920x1080.png", "tupo_user_flag.750x1334.png", 0.8)
	print "find users %d" %(len(t))
	return t;

def douji(d):
	return

def stopyuhunjiacheng():
	pass

def stopJiacheng(d):
	backHome(d)
	# 进入加成页面
	wait_image(d, "jiacheng_entrance_home.750x1334.png")
	#关闭所有加成
	time.sleep(2);
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	print "stop jiacheng"
	runnings = find_all_image_position("screen.1920x1080.png", "jiacheng_running.750x1334.png");
	print runnings;
	for run in runnings:
		click(d, run[0], run[1], False);
		time.sleep(0.2);
	# 退出加成页面
	wait_image(d, "jiacheng_entrance_home.750x1334.png")


def startJiacheng(d, image):
	# 进入加成页面
	wait_image(d, "jiacheng_entrance_2.750x1334.png")
	#关闭所有加成
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	runnings = find_all_image_position("screen.1920x1080.png", "jiacheng_running.750x1334.png");
	for run in runnings:
		print "stop jiacheng"
		click(d, run[0], run[1], False);
		time.sleep(0.2);

	print "start kaiqi jiacheng"
	#查找加成开关
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	t_btns = find_all_image_position("screen.1920x1080.png", "jiacheng_pauseing.750x1334.png");
	print t_btns;

	icons = find_all_image_position("screen.1920x1080.png", image);
	if len(icons):
		icon = icons[0];
		print icon;
		target = t_btns[0];
		dis = 9999;
		for btn in t_btns:
			if abs(btn[0] - icon[0]) < dis:
				dis = abs(btn[0] - icon[0]);
				target = btn
		print "success kaiqi yuhun jiacheng"
		click(d, target[0], target[1], False);
	# 退出加成页面
	wait_image(d, "jiacheng_entrance_2.750x1334.png")

def quick_click_image(d, image):
	d.keep_screen()
	pos = click_image(d, image);
	d.free_screen()
	return pos;

def click_guild(d):
	d.keep_screen()
	FindPoint = click_image(d, "hand_guild.750x1334.png");
	d.free_screen()

	dis = d.display
	y = dis.height - (FindPoint.pos[0] + 50)
	x = FindPoint.pos[1] - 50
	d.click(x, y)


def lianxiaohao(d):
	while 1:
		click_image(d, "diandiandian.750x1334.png");
		click_image(d, "diandiandian_2.750x1334.png");
		d.keep_screen()
		click_image(d, "daxiaoguai_1.750x1334.png");
		click_image(d, "juqing_yanjing.750x1334.png");
		click_image(d, "juqing_wenhao.750x1334.png");
		click_image(d, "skip.750x1334.png");
		click_image(d, "zhunbei.750x1334.png")
		click_image(d, "yuhunjieshu_4.750x1334.png")
		click_image(d, "shibai_jixu.750x1334.png")
		click_image(d, "quick_play.750x1334.png")
		click_image(d, "xiaobai.750x1334.png")
		click_image(d, "tupo_queding.750x1334.png")
		click_image(d, "close_btn.750x1334.png")
		d.free_screen()
		# click_guild(d);

def tansuo_find(d):
	if d.exists("tansuo_daguai.750x1334.png") != None:
		print "find boss";
		click_image(d, "tansuo_daguai.750x1334.png")
		time.sleep(2);
		click_image(d, "zhunbei.750x1334.png")
	elif (d.exists("yuhun_entrance.750x1334.png") != None) | (d.exists("tansuo.750x1334.png") != None):
		print "did end tansuo"
		return False;
	elif click_image(d, "daxiaoguai_3.750x1334.png") != None:
		print "find xiaoguai";
		time.sleep(2);
		click_image(d, "zhunbei.750x1334.png")
	elif d.exists("tansuo_xiao_baoxiang.750x1334.png") != None:
		click_image(d, "tansuo_xiao_baoxiang.750x1334.png");
		print "xiao baoxiang";
	elif d.exists("return_btn.750x1334.png") != None:
		print "No more to kill, move"
		time.sleep(1);
		click(d, 186, 904);
	else:
		print "maybe attacking"
		click_image(d, "zhunbei.750x1334.png")
		click_image(d, "yuhunjieshu_3.750x1334.png")
		click_image(d, "yuhunjieshu_4.750x1334.png")
		click_image(d, "yuhunjieshu_4.750x1334.png")
		click_image(d, "shibai_jixu.750x1334.png")
	return True;

def zzz_douji(d):
	enter = "zzz_pipei.750x1334.png"#匹配按钮
	lijijiechu = "lijijiechu.750x1334.png"#立即解除
	quxiao = "zzz_quxiao.750x1334.png"#取消
	zidongshangzhen = "douji_zidongshangzheng.750x1334.png"#自动上阵
	shoudong2zidong = "douji_shoudong_2_zidong.750x1334.png"#手动改自动

	# click_image(d, lijijiechu);
	# click_image(d, quxiao)
	click_image(d, enter)
	d.keep_screen()
	click_image(d, zidongshangzhen);
	click_image(d, shoudong2zidong);
	click_image(d, "zhunbei.750x1334.png")
	click_image(d, "zzz_end.750x1334.png")
	# click_image(d, "zzz_end_jiutun.750x1334.png")
	click_image(d, "zzz_end_jiangli.750x1334.png")
	d.free_screen()

def tansuo_lianji_28(d):

	backHome(d)
	tansuo(d)
	time.sleep(2);
	while click_image(d, "tansuo_level_28.750x1334.png") != None:
		pass
	
	startJiacheng(d, "jiacheng_jingyan.750x1334.png");
	while 1:
		if click_image(d, "tansuo_baoxiang_big.750x1334.png") != None:
			time.sleep(5);
			click_image(d, "yuhunjieshu_4.750x1334.png")

		if click_image(d, "tansuo_level_28.750x1334.png") != None:
			time.sleep(3);
			click_image(d, "tansuo_start.750x1334.png");
			while tansuo_find(d):
				pass
		elif click_image(d, "tansuo_start.750x1334.png") != None:
			while tansuo_find(d):
				pass

	stopJiacheng(d);

def tansuo_lianji_6(d):

	backHome(d)
	tansuo(d)
	time.sleep(2);
	while click_image(d, "tansuo_level_6.750x1334.png") != None:
		pass
	
	startJiacheng(d, "jiacheng_jingyan.750x1334.png");
	while 1:
		if click_image(d, "tansuo_baoxiang_big.750x1334.png") != None:
			time.sleep(5);
			click_image(d, "yuhunjieshu_4.750x1334.png")

		if click_image(d, "tansuo_level_6.750x1334.png") != None:
			time.sleep(3);
			click_image(d, "tansuo_start.750x1334.png");
			while tansuo_find(d):
				pass
		elif click_image(d, "tansuo_start.750x1334.png") != None:
			while tansuo_find(d):
				pass

	stopJiacheng(d);

# d = atx.connect('http://192.168.0.104:8100', platform='ios') # platform也可以不指定
d = atx.connect('http://172.18.40.153:8100', platform='ios') # platform也可以不指定
print d.rotation
dis = d.display
i = 0

#lianxiaohao(d);
#kaiqijiacheng(d)
# tansuo_lianji_6(d);

# while 1:
#  	zzz_douji(d);
	
#stopAll(d);
while i<10:
	# yuhun(d);
	yingyangliao_tupo(d)
	# geren_tupo(d);
	i = i+1;

# d.click();
# while 1:
# 	yuhun(d)
	#zudui(d)


#d.click_image("tiaozhan.1334x750.png")tansuo