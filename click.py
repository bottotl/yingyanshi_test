# coding: utf-8
import atx
import time

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

def click(d, x1, y1):
	dis = d.display
	y = dis.height - x1
	x = y1
	d.click(x, y)

def yuhun(d):
	while 1:
		wait_image(d, "tiaozhan.750x1334.png")
		time.sleep(2)
		print 'enter loop'
		while d.exists("tiaozhan.750x1334.png") == None:
			# print '...'
			click_image(d, "zhunbei.750x1334.png")
			click_image(d, "yuhunjieshu_1.750x1334.png")
			click_image(d, "shibai_jixu.750x1334.png")
			
		print 'exit'

def zudui(d):
	while 1:
		print 'waiting for kaishi zudui'
		while click_image(d, "kaishizhandou.750x1334.png") != None:
			print '.'
		while d.exists("kaishizhandou.750x1334.png") == None:
			click_image(d, "zhunbei.750x1334.png")
			click(d, 382, 1166)

d = atx.connect('http://172.16.44.19:8100', platform='ios') # platform也可以不指定
print d.rotation
dis = d.display
while 1:
	yuhun(d)
	#zudui(d)


#d.click_image("tiaozhan.1334x750.png")