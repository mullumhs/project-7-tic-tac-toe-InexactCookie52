board = []
colom_key = {"A": 0,"B": 1,"C": 2}
def initialise_board():
    for i in range(3):
        # adds the number to the side of the board
        board.append(["-","-","-"])
        #makes a list of dictionarys to make the board
def print_board():
    i = 0
    for row in board: 
        i += 1
        print (i, end= '|')
        for col in row:
            print(col, end='|')
            #makes the dividing lines between the board
        print()
    print ("  A B C")
    #makes the abc under the board
def move(turncount):
    player_count = turncount
    while True: 
        if not player_count % 2 == 0:
            token = 'X'
            print ("player X turn; ")
        if player_count % 2 == 0:
            token = 'O'
            print ("Player O turn")
        while True:
            choice_col = (input("please select the colom you would like to place, Either A B or C: ")).upper()
            while not choice_col in colom_key:
                #checks if user input is in the dictionary
                print("invalid input: ")
                choice_col = (input("please select the colom you would like to place, Either A B or C: ")).upper()
            while True:
                choice_row = input("now please select a row to place in, either 1 2 or 3: ")
                try:    
                    choice_row = int(choice_row) - 1
                    if choice_row > -1 and choice_row < 3:
                    #checks if between 1 and 3
                        break
                    else:
                        print("invalid input: ")
                except:
                    print("invalid input: ")
                # checks if the row choice is a number and if that number is between 1 and 3.
            

            if board[choice_row][colom_key[choice_col]] == '-':
                board[choice_row][colom_key[choice_col]] = token
                break
            else:
                print("this spot is already taken!: ")
        break
def hor_win():
    for i in range(0,3):
        if board[0][i] == board[1][i] == board[2][i] and not board [0][i] == '-':
            if board[0][i] == 'X':
                return 'X'
            if board[0][i] == 'O':
                return 'O'
    return 'false'
def vert_win(): 
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] and not board [i][0] == '-':
            if board[i][0] == 'X':
                return 'X'
            if board[i][0] == 'O':
                return 'O'
    return 'false'
def diagonal_win():
    if board[0][0] == board[1][1] == board[2][2] and not board [1][1] == '-' or board[0][2] == board[1][1] == board[2][0] and not board [1][1] == '-':
        if board[1][1] == 'X':
            return "X"
        if board[1][1] == 'O':
            return "O"
    return 'false'
def main():
    print ("Welcome To Tic Tac Toe!")
    initialise_board()
    turncount = 1
    while True:
        print_board()
        move(turncount)
        turncount += 1
        if hor_win() == "X" or vert_win() == "X" or diagonal_win() == 'X':
            print_board()
            print("X wins!")
            break
        elif hor_win() == "O" or vert_win() == "O" or diagonal_win() == 'O':
            print_board()
            print("O wins!")
            break
        elif hor_win() == "false" or vert_win() == "false" or diagonal_win() == 'false':
            print("")
        if turncount == 10:
            print("Draw!")
            break
main()