
def main():
    board = initialiseBoard()
    displayBoard(board)

def current_player():
    print()
    
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
