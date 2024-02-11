# J_P_0030

import turtle
colors = [ 'darkorange' , 'darkorange' , 'white' , 'blue' , 'green' , 'green' ]
t= turtle.Pen()
t.speed(10)
turtle.bgcolor("black")

for x in range(300):
	
	t.pencolor(colors[x%6]) 
	t.width(x/100 + 1) 
	t.forward(x) 
	t.left(59) 
	
turtle.done()
t.speed(20)
turtle.bgcolor("black") 

for x in range(300):
	
	t.pencolor(colors[x%6]) 
	t.width(x/100 + 1) 
	t.forward(x)
	t.left(59) 

turtle.done()