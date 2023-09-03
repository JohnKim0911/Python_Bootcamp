from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def drag(self, i, j):
        self.ondrag(None)
        self.goto(i, self.ycor())
        self.ondrag(self.drag)

