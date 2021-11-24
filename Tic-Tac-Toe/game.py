class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]#We will use a single list to rep 3*3 board
        self.current_winner = None #Keep track of winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' +' | '.join(row) + ' |')
        
    @staticmethod
    def print_board_nums():
        # 0| 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' +' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i,x) in enumerate(self.board):
        #     # ['x','x','o'] --> [(0,'x'),(1,'o'),(2,'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves      

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move, then make the move(assign square to letter)
        # then return true. if valid, return false
        if self.board[square]== ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False       

def play(game, x_player, o_player, print_game=True):
    #return the winner of the game(the letter)! or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # staring letter
    #iterate while the game still has empty squares
    # (We don't have to worry about winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        #let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #just empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!')
                return letter

            #after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'

        if print_game:
            print('It\'s a tie!!')
        