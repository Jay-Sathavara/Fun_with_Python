# JP0030

import turtle

wn=turtle.Screen()          
wn.setup(640,640)           
wn.title("Laptop")
wn.bgcolor("blue")

b=turtle.Turtle()
b.shapesize(1.5)
b.speed(0)

b.begin_fill()
b.color("#848283","#848283")
b.seth(90)
b.fd(320)
b.seth(180)
b.fd(320)
b.seth(-90)
b.fd(640)
b.seth(0)
b.fd(320)
b.seth(90)
b.fd(320)
b.end_fill()
