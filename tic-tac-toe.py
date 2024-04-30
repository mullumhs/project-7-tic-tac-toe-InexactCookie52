board = []
#colom_key = {[]}
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
def move():
    player_count = 1
    while True: 
        
        if not player_count % 2 == 0:
            token = 'X'
            print ("player X turn; ")
        if player_count % 2 == 0:
            token = 'O'
            print ("Player O turn")

        choice_col = input("please select the colom you would like to place, Either A B or C: ").title
        if choice_col == 'A':
            choice_col = 0
        elif choice_col == 'B':
            choice_col = 1
        elif choice_col == 'C':
            choice_col = 2
        else:
            print("invalid input: ")




        choice_row = int(input("now please select a row to place in, either 1 2 or 3: "))
        choice_row += 1
        board[choice_row][choice_col] = token
        """
        for i in range(5, -1, -1):
            if board[i][choice] == '-':
                board[i][choice] = token   
                player_count += 1
                break
        
        for row in range(6):
            for col in row:
                print()
"""
initialise_board()
move()
print_board()