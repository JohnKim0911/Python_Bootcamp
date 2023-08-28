age: int
name: str
height: float
is_human: bool


def police_check(age: int) -> bool:  # It allows only 'int' type and returns 'bool' type
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


# ----------- Imagine there are much more code in the middle --------------#


# if police_check("twelve"):   # Causes an error
if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")


# ----------------------------- Result ---------------------------------- #
# Pay a fine.

