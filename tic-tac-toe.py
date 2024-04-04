#def bad():
"""
    def main():
        board = initialiseBoard()
        displayBoard(board)
        player = 1

        
    def initialiseBoard():
        board = []
        for _ in range(6):
            row = []
            for _ in range(7):
                row.append('|_|')
            board.append(row) 
        return board
        
    def displayBoard(board):
        for row in board:
            for cell in row:
                print(cell, end=' ')
            print()
        print()

    if __name__ == "__main__":
        main()
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

initialise_board()
print_board()
player_count = 1
while True: 
    token = 'X'
    if player_count % 2 == 0:
        token = 'O'

    choice = int(input("Input colum number between 1 and 7: "))
    choice -= 1
    for i in range(5, -1, -1):
        if board[i][choice] == '-':
            board[i][choice] = token   
            player_count += 1
            break
        
    print_board()