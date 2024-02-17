# JP0030

import turtle as t 

t.speed(8) 

for i in range(6): 
	t.forward(100) 
	t.backward(100) 
	t.right(60) 

side = 60

t.fillcolor("Yellow") 

t.begin_fill() 

for i in range(20): 
	t.penup() 
	t.goto(0, 0) 
	t.pendown() 
	t.setheading(0) 
	t.forward(side) 
	t.right(120) 

	for j in range(6): 
		t.forward(side-2) 
		t.right(60) 
	side = side - 10

t.end_fill() 
