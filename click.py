# coding: utf-8
import atx
import time
import aircv as ac

def swipe(d, x1, y1, x2, y2):
	dis = d.display
	y11 = dis.height - x1
	x11 = y1

	y22 = dis.height - x2;
	x22 = y2

	d.swipe(x11, y11, x22, y22, 0.5);

def find_all_image_position(origin='origin.png', query='query.png', outfile=None):
    imsrc = ac.imread(origin) # 原始图像
    imsch = ac.imread(query) # 带查找的部分
    return ac.find_all_template(imsrc, imsch)

def click_image(d, image):
	FindPoint = d.exists(image)
	if FindPoint != None:
		print(image)
		p_click(d, FindPoint)
	return FindPoint

def wait_image(d, image):
	FindPoint = None
	while FindPoint is None:
		print 'finding...'
		FindPoint = d.exists(image)
	p_click(d, FindPoint)
	print(image)
	return FindPoint

def p_click(d, FindPoint):
	dis = d.display
	y = dis.height - FindPoint.pos[0]
	x = FindPoint.pos[1]
	d.click(x, y)

def click_im(d, pos):
	dis = d.display
	y = dis.height - pos[0]
	x = pos[1]
	d.click(x, y)

def click(d, x1, y1):
	dis = d.display
	y = dis.height - x1
	x = y1
	d.click(x, y)

def yuhun(d):
	backHome(d)
	tansuo(d)
	wait_image(d, "yuhun_entrance.750x1334.png")
	time.sleep(2);
	click_image(d, "yuhun_dashe.750x1334.png")
	time.sleep(2);
	i = 0
	while i<20:
		wait_image(d, "tiaozhan.750x1334.png")
		time.sleep(2)
		print 'enter loop'
		while d.exists("tiaozhan.750x1334.png") == None:
			# print '...'
			click_image(d, "zhunbei.750x1334.png")
			click_image(d, "yuhunjieshu_1.750x1334.png")
			click_image(d, "shibai_jixu.750x1334.png")
			if d.exists("tilibuzu_goumaitili.750x1334.png") != None:
				click_image(d, "close_btn_tili_2.750x1334.png");
				time.sleep(2);
				print "no tili exit yuhun";
				return;
		i = i+1;
		print 'exit'

def zudui(d):
	while 1:
		click_image(d, "yuhunjieshu_1.750x1334.png")
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
				click_image(d, "yuhunjieshu_1.750x1334.png")
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
				if (click_image(d, "yuhunjieshu_1.750x1334.png") != None) | (click_image(d, "shibai_jixu.750x1334.png") != None):
					break;
		click_image(d, "tupo_shuaxin.750x1334.png");
		time.sleep(2);
		click_image(d, "tupo_queding.750x1334.png");
		time.sleep(2);
		users = tupoUserPositions(d);
		if len(users) < 1:
			i = i+1;
			print "find more user to kill"
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
				click_image(d, "yuhunjieshu_1.750x1334.png")
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
				if (click_image(d, "yuhunjieshu_1.750x1334.png") != None) | (click_image(d, "shibai_jixu.750x1334.png") != None):
					break;
		time.sleep(1);
		swipe(d, 148, 758, 590, 846);
		time.sleep(2);
		users = tupoUserPositions(d);
		if len(users) < 1:
			i = i+1;
			print "find more user to kill"
	click_image(d, "yuhunjieshu_1.750x1334.png")
	time.sleep(2)
	click_image(d, "shibai_jixu.750x1334.png")
	time.sleep(2)
	print "no more user to kill"


def switch_zidong_shoudong(d):
	click(d, 58, 62);

def tupoUserPositions(d):
	d.screenshot('screen.1920x1080.png') # Save screenshot as file
	posArray = find_all_image_position("screen.1920x1080.png", "tupo_user_flag.750x1334.png")
	t = []
	for pos in posArray:
		if pos['confidence'] > 0.8:
			t.append(pos['result'])
	print "find users %d" %(len(t))
	return t

def douji(d):
	return

#d = atx.connect('http://192.168.0.102:8100', platform='ios') # platform也可以不指定
d = atx.connect('http://172.16.44.42:8100', platform='ios') # platform也可以不指定
print d.rotation
dis = d.display
i = 0
while i<10:
	geren_tupo(d);
	yingyangliao_tupo(d)
	yuhun(d);
	i = i+1;

# d.click();
# while 1:
# 	yuhun(d)
	#zudui(d)


#d.click_image("tiaozhan.1334x750.png")