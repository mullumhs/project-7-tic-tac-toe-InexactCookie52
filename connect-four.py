#def bad():
"""
while True:
        if choice.isdigit():
            choice = int(choice)
            if choice>=1 and choice <=7:
                break
            else: 
                choice = input("Input colum number between 1 and 7: ")
        else: 
            choice = input("Input colum number between 1 and 7: ")

"""
board = []
def initialise_board():
    for i in range(6):
        board.append(["-","-","-","-","-","-","-",])
        

def print_board():
    print (" 1 2 3 4 5 6 7")
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

        choice = int(input("Input colum number between 1 and 7: "))
        choice -= 1
        for i in range(5, -1, -1):
            if board[i][choice] == '-':
                board[i][choice] = token   
                player_count += 1
                break
        
        for row in range(6):
            for col in row:
                print(col)
                
        print_board()
        

initialise_board()
print_board()
move()
