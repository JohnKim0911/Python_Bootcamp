from game_data import data
import random
from art import logo, vs
# from replit import clear


def clear():  # Prints 50 blank lines
    print("\n" * 50)


# Generate a random account from the game data.
def get_random_account():
    """Get data from random account"""
    return random.choice(data)


# Format account data into printable format.
def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)  # Add art.
    score = 0  # Score Keeping.
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    # Make game repeatable.
    while game_should_continue:
        account_a = account_b  # Make B become the next A.
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()  # Ask user for a guess.
        a_follower_count = account_a["follower_count"]  # Get follower count.
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()  # Clear screen between rounds.
        print(logo)
        if is_correct:  # Feedback.
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). 
Instagram has more followers, so choice A is correct. 
However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. 
The reason is that everything in our list has fewer followers than Instagram. 
If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. 
This would be quite boring. 
By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. 
Hope that makes sense :-)

'''

# ------------------------------------- RESULT ------------------------------------ #
#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/
#
# Compare A: Beyoncé, a Musician, from United States.
#
#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)
#
# Against B: Neymar, a Footballer, from Brasil.
# Who has more followers? Type 'A' or 'B': A
#
#
# ==================== BLANK LINES ====================
#
#
#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/
#
# You're right! Current score: 1.
# Compare A: Neymar, a Footballer, from Brasil.
#
#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)
#
# Against B: Drake, a Musician, from Canada.
# Who has more followers? Type 'A' or 'B': A
#
#
# ==================== BLANK LINES ====================

#
#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/
#
# You're right! Current score: 2.
# Compare A: Drake, a Musician, from Canada.
#
#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)
#
# Against B: Khloé Kardashian, a Reality TV personality and businesswoman, from United States.
# Who has more followers? Type 'A' or 'B': B
#
#
# ==================== BLANK LINES ====================
#
#
#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/
#
# You're right! Current score: 3.
# Compare A: Khloé Kardashian, a Reality TV personality and businesswoman, from United States.
#
#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)
#
# Against B: Real Madrid CF, a Football club, from Spain.
# Who has more followers? Type 'A' or 'B': B
#
#
# ==================== BLANK LINES ====================
#
#
#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/
#
# Sorry, that's wrong. Final score: 3
