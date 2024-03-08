import turtle 

turtle.Screen().bgcolor("floralwhite") 

t = turtle.Turtle()

t.speed(10) 

t.pensize(10)

t.penup()

def draw_circle():
	t.setposition(0,-280)
	t.pendown()
	t.begin_fill()
	t.color('darkorchid2')
	t.pencolor("gold1")
	t.circle(300)
	t.end_fill()
	t.penup()