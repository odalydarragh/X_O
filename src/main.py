import random

class Game:
    def __init__(self):
        self.board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.debug_on = False

    def print_board(self):
        for row in self.board:
            print(row)

    def play(self, player_turn):
        self.debug("\n---------------------------")
        self.debug("-> play(" + player_turn + ")")
        print("    Its " + player_turn + "'s turn")
        row = int(input("Row?"))
        col = int(input("Col?"))
        print("    You have chosen: " + str(row) + ", " + str(col))
        while not self.board[row][col] == '_':
            print("    This square has already been chosen")
            row = int(input("Row?"))
            col = int(input("Col?"))

        self.debug("    -- Setting square " + str(row) + "," + str(col) + " to: " + player_turn)
        self.board[row][col] = player_turn
        self.debug("<-- returning from play()")
        self.debug("---------------------------\n")

    def check_win(self, symbol):
        win = False
       #rows
        if self.board[0][0] == symbol:
            if self.board[0][1] == symbol:
                if self.board[0][2] == symbol:
                    win = True

        if self.board[1][0] == symbol:
            if self.board[1][1] == symbol:
                if self.board[1][2] == symbol:
                    win = True

        if self.board[2][0] == symbol:
            if self.board[2][1] == symbol:
                if self.board[2][2] == symbol:
                    win = True
        #columns
        if self.board[0][0] == symbol:
            if self.board[1][0] == symbol:
                if self.board[2][0] == symbol:
                    win = True

        if self.board[0][1] == symbol:
            if self.board[1][1] == symbol:
                if self.board[2][1] == symbol:
                    win = True

        if self.board[0][2] == symbol:
            if self.board[1][2] == symbol:
                if self.board[2][2] == symbol:
                    win = True
        #diag
        if self.board[0][0] == symbol:
            if self.board[1][1] == symbol:
                if self.board[2][2] == symbol:
                    win = True

        if self.board[2][0] == symbol:
            if self.board[1][1] == symbol:
                if self.board[0][2] == symbol:
                    win = True

        return win

    def debug(self, msg):
        if self.debug_on:
            print(msg)

class Player:
    def __init__(self, symbol):
        self.symbol = symbol


if __name__ == "__main__":
    g = Game()
    # g.debug_on = True
    win = False
    player = Player('X')
    player2 = Player('O')
    g.print_board()
    # set who goes first
    g.debug("__main__: Changing player turn..")
    turn_count = random.randint(1, 2)
    g.debug("__main__: 1. Turn set to: " + str(turn_count))
    if turn_count % 2 == 0:
        player_turn = player
        g.debug("__main__: 2. Turn set to: " + str(turn_count))
    else:
        player_turn = player2
        g.debug("__main__: 3. Turn set to: " + str(turn_count))
    # main game loop
    while not win:
        g.debug("__main__: Start of play loop")
        if g.check_win(player_turn.symbol):
            print("You win")
            g.debug("__main__: nobody won yet..")
        # change player
        g.debug("__main__: turn_count updated to : " + str(turn_count))
        if turn_count % 2 == 0:
            player_turn = player
            g.debug("__main__: 4. Turn set to: " + str(turn_count))
        else:
            player_turn = player2
            g.debug("__main__: 5. Turn set to: " + str(turn_count))
        turn_count += 1
        g.play(player_turn.symbol)
        g.print_board()

