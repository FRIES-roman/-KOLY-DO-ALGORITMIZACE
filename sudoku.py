import random

def je_platne(board, row, col, num):

    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def najdi_prazdne(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def resit_sudoku(board):
    prazdna_pozice = najdi_prazdne(board)
    if not prazdna_pozice:
        return True  
    
    row, col = prazdna_pozice
    for num in range(1, 10):
        if je_platne(board, row, col, num):
            board[row][col] = num
            if resit_sudoku(board):
                return True
            board[row][col] = 0  
    return False

def generuj_sudoku():
    board = [[0] * 9 for _ in range(9)] 


    for _ in range(20): 
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if je_platne(board, row, col, num):
            board[row][col] = num
    return board

def tiskni_sudoku(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def hlavni():
    sudoku = generuj_sudoku()
    print("Generované Sudoku:")
    tiskni_sudoku(sudoku)

    if resit_sudoku(sudoku):
        print("\nVyřešené Sudoku:")
        tiskni_sudoku(sudoku)
    else:
        print("\nSudoku nelze vyřešit.")

if __name__ == "__main__":
    hlavni()
