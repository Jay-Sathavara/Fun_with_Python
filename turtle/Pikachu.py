import turtle
def gajurel(x, y):
    turtle.setx(x)
    turtle.sety(y)
    print(x, y)
class Shinchan:
    def __init__(self):
        self.t = turtle.Turtle()
        t = self.t
        t.pensize(3)
        t.speed(9)
        t.ondrag(gajurel)
    def meme(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
    def aankha1(self, x, y):
        self.meme(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()
        self.meme(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        self.meme(x + 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()
    def aankha2(self, x, y):
        self.meme(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()
        self.meme(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        self.meme(x - 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()