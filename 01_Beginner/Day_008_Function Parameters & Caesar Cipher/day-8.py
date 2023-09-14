# -------------------------- simple Function ----------------------------- #
def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice today?")


greet()

# ------------ Result -------------#
# Hello Angela
# How do you do Jack Bauer?
# Isn't the weather nice today?
# ---------------------------------#


# -------------------------- Function that allows for input ----------------------------- #
def greet_with_name(name):  # 'name' is the parameter.
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")  # 'Jack Bauer' is the argument.

# ------------ Result -------------#
# Hello Jack Bauer
# How do you do Jack Bauer?
# ---------------------------------#


# -------------------------- Functions with more than 1 input ----------------------------- #
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
# vs.
greet_with("Nowhere", "Jack Bauer")

# ------------ Result -------------#
# Hello Jack Bauer
# What is it like in Nowhere?
# ---------------------------------#
# Hello Nowhere
# What is it like in Jack Bauer?
# ---------------------------------#


# Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")

# ------------ Result -------------#
# Hello Angela
# What is it like in London?
# ---------------------------------#
