# J_P_0030

import turtle
import random

t = turtle.Turtle()

w = turtle.Screen()

t.speed(15)

w.bgcolor("black")

t.color("white")

w.title("Starry Sky")

def stars():
	for i in range(6):
		t.fd(10)
		t.right(144)

for i in range(120):

	x = random.randint(-640, 640)
	y = random.randint(-330, 330)
	
	stars()
	
	t.up()
	
	t.goto(x, y)
	
	t.down()

t.up()

t.goto(0, 180)

t.down()

t.color("white")

t.begin_fill()

t.circle(70)

t.end_fill()

t.hideturtle()

w.exitonclick()
