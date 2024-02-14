# JP0030

from turtle import *
def ankle(x,y):
    penup()
    goto(x,y)
    pendown()

def eyes():
    fillcolor("#ffffff")
    begin_fill()
    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i <30 or 60 <= i <90:
            a -=0.05
            lt(3)
            fd(a)
        else:
            a +=0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()

def daari():
    ankle(-32, 135)
    seth(165)
    fd(60)

    ankle(-32, 125)
    seth(180)
    fd(60)

    ankle(-32, 115)
    seth(193)
    fd(60)

    ankle(37, 135)
    seth(15)
    fd(60)

    ankle(37, 125)
    seth(0)
    fd(60)

    ankle(37, 115)
    seth(-13)
    fd(60)

