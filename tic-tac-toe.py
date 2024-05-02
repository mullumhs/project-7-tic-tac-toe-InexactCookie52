board = []
colom_key = {"A": 0,"B": 1,"C": 2}
def initialise_board():
    for i in range(3):
        i += 1
        board.append(["-","-","-", i])
def print_board():
    print (" A B C")
    for row in board:
        print ("", end='|')
        for col in row:
            print(col, end='|')
        print()
def move(turncount):
    
    player_count = turncount
    while True: 
        print_board()
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
                player_count += 1
                break
            else:
                print("this spot is already taken!: ")

        break
def main():
    initialise_board()
    turncount = 1
    while True:
        move(turncount)
        print_board()
        turncount += 1
        if turncount == 9:
            break
#figure out player count
main()