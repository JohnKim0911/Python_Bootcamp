# Scope

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
# enemies inside function: 2
# enemies outside function: 1


# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()  # 2
# print(potion_strength)  # Causes an error -> NameError: name 'potion_strength' is not defined


# Global Scope
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()


game()
print(player_health)
# 10
# 10


# There is no Block Scope
game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


create_enemy()  # Skeleton


# Modifying Global Scope
enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
# enemies inside function: 1
# enemies outside function: 2


# Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
