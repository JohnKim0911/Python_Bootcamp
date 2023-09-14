############## Constructing Objects and Accessing their Attributes and Methods ##############
import another_module

print(another_module.another_variable)  # 12


# ----------------- Turtle Graphics ------------------- #
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)  # <turtle.Turtle object at 0x00000223A79223D0>
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)  # 300
my_screen.exitonclick()



############## How to Add Python Packages and use PyPi ##############
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)
# +--------------+----------+
# | Pokemon Name | Type     |
# +--------------+----------+
# | Pikachu      | Electirc |
# | Squirtle     | Water    |
# | Charmander   | Fire     |
# +--------------+----------+

