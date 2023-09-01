class GameManager:
    def __init__(self):
        self.board = [['  ', '  ', '  '], ['  ', '  ', '  '], ['  ', '  ', '  ']]
        self.column_index = ['1', '2', '3']
        self.row_index = ['a', 'b', 'c']
        self.users = ['🟢', '🟥']
        self.turn = self.users[0]
        self.invalid_answer_warning = "*** Invalid Answer *** "
        self.winner = ''

    def show_board(self):
        """Prints the current board."""
        print(f"\n   |  {self.column_index[0]} |  {self.column_index[1]} |  {self.column_index[2]} |")
        row_break = "---------------------"
        i = 0
        for row in self.board:
            print(row_break)
            print(f" {self.row_index[i]} | {row[0]} | {row[1]} | {row[2]} |")
            i += 1
        print(f"{row_break}\n")

    def is_valid_answer(self, answer):
        """Return True when it's valid, otherwise False."""
        # check the length
        if len(answer) == 2:
            # check if it's in the right form and within a range.
            if answer[0] in self.row_index and answer[1] in self.column_index:
                # check if it's already taken.
                row = self.row_index.index(answer[0])
                column = self.column_index.index(answer[1])
                if not self.board[row][column] == '  ':
                    print(f"{self.invalid_answer_warning}  It's already taken.")
                    return False
                return True
            else:
                return False
        else:
            return False

    def update_board(self, answer, turn):
        """Update and show the board"""
        row = self.row_index.index(answer[0])
        column = self.column_index.index(answer[1])
        self.board[row][column] = turn
        self.show_board()

    def change_turn(self):
        """Switch user's turn"""
        if self.turn == self.users[0]:
            self.turn = self.users[1]
        else:
            self.turn = self.users[0]

    def has_won(self):
        """Return True when user has won, otherwise False"""
        # Check all users
        for user in self.users:
            # Check each row
            for row in self.board:
                count_on_row = 0
                for column in row:
                    if column == user:
                        count_on_row += 1
                if count_on_row == 3:
                    self.winner = user
                    return True
            # Check each column
            for column in range(len(self.column_index)):
                count_on_col = 0
                for row in self.board:
                    if row[column] == user:
                        count_on_col += 1
                if count_on_col == 3:
                    self.winner = user
                    return True
            # Check horizontal line1 (a1, b2, c3)
            count_on_hor1 = 0
            column_i = 0
            for row in self.board:
                if row[column_i] == user:
                    count_on_hor1 += 1
                column_i += 1
            if count_on_hor1 == 3:
                self.winner = user
                return True
            # Check horizontal line1 (a3, b2, c1)
            count_on_hor2 = 0
            column_j = len(self.column_index) - 1
            for row in self.board:
                if row[column_j] == user:
                    count_on_hor2 += 1
                column_j -= 1
            if count_on_hor2 == 3:
                self.winner = user
                return True

    def has_drawn(self):
        """Return True when it's drawn, otherwise False."""
        for row in self.board:
            for column in row:
                if column == '  ':
                    return False
        return True
