import turtle as tl

class PONG:
    def __init__(self):
        self.create_window()
        self.leftpaddle()
        self.rightpaddle()
        self.create_ball()
        self.keys()
        self.game()
    def create_window(self):
        self.root = tl.Screen()
        self.root.title("PONG GAME by PythonGeeks")
        self.root.bgcolor("yellow")
        self.root.setup(width=600, height=400)
        self.root.tracer(0)
    def leftpaddle(self):
        self.left_paddle = tl.Turtle()
        self.left_paddle.speed(0)
        self.left_paddle.shape('square')
        self.left_paddle.color('red')
        self.left_paddle.shapesize(stretch_wid=7, stretch_len=1.2)
        self.left_paddle.penup()
        self.left_paddle.goto(-280, 0)