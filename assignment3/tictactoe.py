class TictactoeException(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message = message
#Builds the list that will become the board cells.
class Board:
    def __init__(self):
        self.board_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
    #Used for validation of input:
    valid_moves=["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    #build board for display:
    def __str__(self):
        lines=[]
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
    #Asses player move input
    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    #Checks board for game status
    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")

Board.move
Board.whats_next

#what is done:
    #established game 
    #next move Loop
    #Prompted and taken in next desired move
    #is it valid: move(), try/except
    #place move on board: move()
#whats needed:
    #check game status given above move - winner, full card, or next move?: whats_next()
    #if while loop includes a check of whats next, then whats next will run between loops

game = Board()
while game.whats_next() == (False, "X's turn.") or game.whats_next() == (False, "O's turn."):
    try:
        turn = game.turn #To ID next move, X or O
        next_move = input(f"{turn}, enter your move by entering the relative location of the cell you desire.")
        game.move(next_move) #changes board and turn
        print(f"{game}") #print board
        game_status = game.whats_next() #tells me if card is full, winner, next move open
        if game_status == (True, "X wins!") or game_status == (True, "O wins!") or game_status == (True, "Cat's Game."):
            print(f"{game_status[1]}")
            break
    except TictactoeException as e: #if invalid move - wrong input or spot taken.
        print(f"{e}")
