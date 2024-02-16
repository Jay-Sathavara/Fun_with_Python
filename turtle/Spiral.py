from turtle import*
import colorsys
bgcolor("black")
speed(0)
h=0
for i in range(130):
	c=colorsys.hsv_to_rgb(h,1,0.8)
	color(c)
	h+=0.005
	fd(i)
	lt(80)
	for j in range(2):
		fd(i)
		rt(20) 
		for k in range(2):
			rt(20)