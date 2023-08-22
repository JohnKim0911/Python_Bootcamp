# < Constructing Objects and Accessing their Attributes and Methods >

import another_module

print(another_module.another_variable)
print("------------------------------------------------")

# ----------------- Turtle Graphics ------------------- #
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# 👇 Turtle Graphics Documentation
# https://docs.python.org/3/library/turtle.html

# 👇 Turtle Colors
# https://cs111.wellesley.edu/reference/colors
print("------------------------------------------------")


# < How to Add Python Packages and use PyPi >
# File -> Settings -> Project:_________ -> Python Interpreter -> '+'(Install) Button -> (Search) -> Install Package

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electirc", "Water", "Fire"])

table.align = "l"

print(table)

# 👇 Pokemon Pokedex
# https://pokemondb.net/pokedex/game/x-y

# 👇 Python Package Index
# https://pypi.org/

# 👇 PrettyTable Package
# https://pypi.org/project/prettytable/

# 👇 PrettyTable Package Documentation
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki