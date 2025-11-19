from colorama import Fore, Style

def checkValid(matrix, row, col, num):
    for x in range(9):
        if matrix[row][x] == num:
            return False
    for x in range(9):
        if matrix[x][col] == num:
            return False
    sr = row - row % 3
    sc = col - col % 3
    for i in range(3):
        for j in range(3):
            if matrix[sr + i][sc + j] == num:
                return False
    return True

def solveSudokuRec(matrix, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if matrix[row][col] != 0:
        return solveSudokuRec(matrix, row, col + 1)
    for num in range(1, 10):
        if checkValid(matrix, row, col, num):
            matrix[row][col] = num
            if solveSudokuRec(matrix, row, col + 1):
                return True
            matrix[row][col] = 0
    return False

def solveSudoku(matrix):
    if not solveSudokuRec(matrix, 0, 0):
        return False
    return True

def printSudokuGrid(matrix, highlight=None):
    print("+-------+-------+-------+")
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            v = matrix[i][j]
            if v == 0:
                d = "."
            else:
                if highlight and (i, j) in highlight:
                    d = Fore.YELLOW + str(v) + Style.RESET_ALL
                else:
                    d = Fore.CYAN + str(v) + Style.RESET_ALL
            print(d, end=" ")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")

def printSudokuPlain(matrix):
    print("+-------+-------+-------+")
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            v = matrix[i][j]
            print(v if v != 0 else ".", end=" ")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")

def printSideBySide(original, solved):
    print("\nOriginal Sudoku              Solved Sudoku")
    print("+-------+-------+-------+    +-------+-------+-------+")
    for r in range(9):
        line1 = "| "
        for c in range(9):
            v = original[r][c]
            line1 += (str(v) if v != 0 else ".") + " "
            if (c + 1) % 3 == 0:
                line1 += "| "
        line2 = "| "
        for c in range(9):
            v = solved[r][c]
            line2 += str(v) + " "
            if (c + 1) % 3 == 0:
                line2 += "| "
        print(line1 + "   " + line2)
        if (r + 1) % 3 == 0:
            print("+-------+-------+-------+    +-------+-------+-------+")

def viewSavedSudokus(name, store):
    sudokus = store[name]
    if not sudokus:
        print("No saved sudokus.\n")
        return
    print(f"\nSaved Sudokus for {name.capitalize()}:\n")
    for i in range(len(sudokus)):
        print(f"{i+1}. Sudoku #{i+1}")
    print()
    while True:
        ch = input("Enter number to view (0 to return): ").strip()
        if ch == "0":
            return
        if ch.isdigit() and 1 <= int(ch) <= len(sudokus):
            idx = int(ch) - 1
            orig, solved = sudokus[idx]
            printSideBySide(orig, solved)
            print()
            return
        print("Invalid input.\n")
