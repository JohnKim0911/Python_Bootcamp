import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)
    # -144.0 -8.0
    # -24.0 -39.0
    # -116.0 -45.0
    # -197.0 -40.0
    # -256.0 47.0
    # -270.0 137.0
    # -138.0 161.0


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

