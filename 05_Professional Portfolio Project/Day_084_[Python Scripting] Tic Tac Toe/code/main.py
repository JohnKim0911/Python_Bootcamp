from game_manager import GameManager

game = GameManager()

print('👋👋👋 Welcome to "Tic Tac Toe". 🕹️ 👋👋👋')
game.show_board()
print("Let's start!")

is_on = True
while is_on:
    user_answer = input(f"👉 [{game.turn}'s Turn] Type where to put. (i.e. b2): ").lower()

    if game.is_valid_answer(user_answer):
        game.update_board(user_answer, game.turn)
        game.change_turn()
        if game.has_won():
            print(f"👏👏👏 Player '{game.winner}' has won the game! 🏆 👏👏👏")
            is_on = False
        elif game.has_drawn():
            print("👏👏👏 The game gas been drawn. You both played well! 👏👏👏")
            is_on = False
    else:
        print(f"{game.invalid_answer_warning}  Try again.")
