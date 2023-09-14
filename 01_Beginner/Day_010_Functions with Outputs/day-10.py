# Functions with Outputs

# --------------- Not working like below ---------------- #
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    f"Result: {formatted_f_name} {formatted_l_name}"
    # No return...
# ------------------------------------------------------ #


# Return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it
  to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# Your first name: john
# Your last name: kim
# Result: John Kim


# or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))
# What is your first name? john
# What is your last name? kim
# Result: John Kim


# Already used functions with outputs.
length = len(formatted_name)
print(formatted_name)
print(length)
# Result: John Kim
# 16
