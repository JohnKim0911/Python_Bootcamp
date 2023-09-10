# Breakout Game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()

# Create paddle
paddle = Paddle((0, -250))

# Create multiple rows and columns of Bricks.
BRICK_STARTING_X = - 350
brick_x = BRICK_STARTING_X
brick_y = 50
brick_list = []
color_list = ["yellow", "deep sky blue", "dark orange", "lime", "magenta", "medium purple"]
brick_row = 5
brick_col = 11
i = 0
for _ in range(brick_row):
    for _ in range(brick_col):
        brick = Brick((brick_x, brick_y), color_list[i])
        brick_list.append(brick)
        brick_x += 70
    i += 1
    brick_x = BRICK_STARTING_X
    brick_y += 30


# bind the mouse with the paddle.
paddle.ondrag(paddle.drag)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with left, right wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with top
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect paddle misses:
    if ball.ycor() < -280:
        print("game over")
        game_is_on = False

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and -250 < ball.ycor() < -230:
        # Differentiate ball-bouncing depending on where it hits on the paddle.
        ball.x_move = (ball.xcor() - paddle.xcor()) / 10
        ball.bounce_y()

    # Detect collision with bricks
    for brick in brick_list:
        if ball.distance(brick) < 35:
            brick.disappear()
            ball.bounce_y()
            ball.bounce_x()
            ball.broken_bricks += 1
            if ball.broken_bricks % 5 == 0:
                ball.speed_up()


screen.exitonclick()