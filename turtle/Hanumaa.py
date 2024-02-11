import turtle
from turtle import *

# Screen setup
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Adjust background color
screen.title("Hanumanji")
screen.tracer(0)  # Turn off animation for smoother drawing

# Hanumanji's body
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-120, -120)
t.pendown()

# Orange body
t.begin_fill()
t.color("orange")
t.forward(240)
t.left(90)
t.forward(120)
t.left(90)
t.forward(240)
t.left(90)
t.forward(120)
t.end_fill()

# Green dhoti
t.penup()
t.goto(-120, -240)
t.pendown()
t.begin_fill()
t.color("green")
t.forward(240)
t.left(90)
t.forward(60)
t.left(90)
t.forward(240)
t.left(90)
t.forward(60)
t.end_fill()

# Hanumanji's face
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
t.color("pink")
t.circle(80)
t.end_fill()

# Eyes
t.penup()
t.goto(-30, 40)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(7)
t.end_fill()

t.penup()
t.goto(30, 40)
t.pendown()
t.begin_fill()
t.circle(7)
t.end_fill()

# Nose
t.penup()
t.goto(0, 20)
t.pendown()
t.pensize(3)
t.forward(12)

# Mouth (adjust shape and position)
t.penup()
t.goto(-20, 10)
t.pendown()
t.pensize(2)
t.setheading(270)
t.circle(25, 180)

# Gada mace (optional)
t.penup()
t.goto(140, 0)
t.pendown()
t.pensize(3)
t.color("brown")

t.begin_fill()
t.forward(40)
t.left(90)
t.forward(10)
t.left(90)
t.forward(40)
t.left(90)
t.forward(10)
t.end_fill()

# Mace head
t.penup()
t.goto(180, 0)
t.pendown()
t.begin_fill()
t.color("gold")
t.circle(15)
t.end_fill()

# Vanara details (optional)
# Use smaller circles, triangles, or lines for ears, fur, etc.

# Tail
t.penup()
t.goto(120, -120)
t.pendown()
t.color("orange")

t.begin_fill()
t.forward(60)
t.left(90)
t.forward(35)
t.left(90)
t.forward(60)
t.left(90)
t.forward(35)
t.end_fill()

# Curved tail segments
for i in range(6):
    t.penup()
    t.forward(35)
    t.right(20)
    t.pendown()
    t.begin_fill()
    t.color("orange")
    t.circle(25)
    t.end_fill()

# Angada anklet (optional)
# Draw a golden band around the ankle

# Update the screen
screen.update()  # This line displays the drawn image

# Keep the window open until closed manually
turtle.done()
