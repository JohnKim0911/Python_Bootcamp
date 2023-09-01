from turtle import Turtle

ORIGINAL_POSITION = (0, -230)
MOVE_SPEED = 0.005


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(ORIGINAL_POSITION)
        self.x_move = 3
        self.y_move = 3
        self.move_speed = MOVE_SPEED
        self.broken_bricks = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def speed_up(self):
        self.move_speed *= 0.9

    # def reset_position(self):
    #     self.goto(ORIGINAL_POSITION)
    #     self.move_speed = MOVE_SPEED
    #     self.bounce_y()




