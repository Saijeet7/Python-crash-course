#play the game

class Board:
    def __init__(self, dim_size, num_bombs):
        #let keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #let's create the board
        self.board == self.make_new_board() #plant the bombs
        #initilaize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set()

    def make_new_board(self):
        #generate a new Board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant the bombs
        bombs_planted = 0
        while bombs_planted <self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                #this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*'
            bombs_planted +=1

def play(dim_size=10, num_bombs=10):
    #Step 1: create the board and plant the bombs
    #Step 2: show the user the board and ask for where they want to dig
    #Step 3a: if location is a bomb, show game over message
    #Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bombs
    #STep 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    pass
