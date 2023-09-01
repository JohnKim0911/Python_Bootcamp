# I followed this tutorial below:
# https://www.youtube.com/watch?v=QvtlEj_T55o&list=PLlEgNdBJEO-lqvqL5nNNZC6KoRdSrhQwK&index=1

import turtle
import math
import os   # To add sound for Mac, Linux
import platform
import pygame.mixer  # To add sound for Windows:  # pip install pygame

# If on Windows, you import winsound
if platform.system() == "Windows":
    try:
        import winsound
    except:
        print('Winsound module not available.')

pygame.mixer.init()


# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")
wn.tracer(0)  # Shut off all the screen update. Otherwise, it's way too slow to play.

# Register the shapes
# (Only works with '.gif' format images.)
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)  # 0 is actually fast.
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
score_string = f"Score: {score}"
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)  # method
player.setposition(0, -250)
player.setheading(90)
player.speed = 0  # variable

# Choose a number of enemies
number_of_enemies = 30
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    # Update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemy_speed = 0.05

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)  # x, y
bullet.hideturtle()

bullet_speed = 4

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bullet_state = "ready"


# Move the player left and right
def move_left():
    player.speed = - 1


def move_right():
    player.speed = 1


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # Declare bullet_state as a global if it needs to be changed
    global bullet_state
    if bullet_state == "ready":
        play_sound("laser.wav")
        bullet_state = "fire"
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


def play_sound(sound_file, time=0):  # time in seconds
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    if time > 0:
        pygame.time.delay(int(time * 1000))

    # # Windows
    # if platform.system() == "Windows":
    #     winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # # Linux
    # elif platform.system() == "Linux":
    #     os.system(f"aplay -q {sound_file}&")
    # # Mac
    # else:
    #     os.system(f"afplay {sound_file}&")
    #
    # # Repeat sound
    # if time > 0:
    #     turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))  # 't' is in milliseconds


# Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# Play background music
pygame.mixer.music.load("bgm.wav")
pygame.mixer.music.play(-1)
# play_sound("bgm.wav", 115)  # 5. It stops the sound once you play other sound, so use 'pygame' instead.
# 1. Download the mp3 file here:    https://orangefreesounds.com/cinematic-electronic-track/
# 2. Convert mp3 to wav for free:   https://cloudconvert.com/
# 3. the length of audio file (1:59min -> 119sec, but there's a bit of quite sound at the end so cut off those part)
# 4. If the sound still runs after stopping the program, run terminal and type below.
#    (Mac) killall afplay
#    (Linux) killall aplay


# Main game loop
while True:
    wn.update()  # Goes along with wn.tracer(0)
    move_player()

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemy_speed *= -1

        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemy_speed *= -1

        # Check for a collision between the bullet and the enemy
        if is_collision(bullet, enemy):
            play_sound("explosion.wav")
            # Reset the bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            enemy.setposition(0, 10000)
            # Update the score
            score += 10
            score_string = f"Score: {score}"
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        if is_collision(player, enemy):
            play_sound("explosion.wav")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

