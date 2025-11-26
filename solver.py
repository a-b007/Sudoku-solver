from colorama import Fore, Style

#Checks if n is present in the row, column and 3x3 grid.
def check_valid(mtx, row, col, n):
    for x in range(9):
        if mtx[row][x] == n:
            return False
    for x in range(9):
        if mtx[x][col] == n:
            return False
    sr = row - row % 3
    sc = col - col % 3
    for i in range(3):
        for j in range(3):
            if mtx[sr + i][sc + j] == n:
                return False
    return True


#Recursive function
def sudo_rec(mtx, row, col):
    # BASE CASE: The 2nd last entry of the Sudoku
    if row == 8 and col == 9:
        return True
    #if the last column is reached in a row, we move to column 0 of next row
    if col == 9:
        row += 1
        col = 0
        #If Cell already filled just skip it.
    if mtx[row][col] != 0:
        return sudo_rec(mtx, row, col + 1)
    
    for n in range(1, 10):
        
        if check_valid(mtx, row, col, n):
            mtx[row][col] = n
            
            #recursive step
            if sudo_rec(mtx, row, col + 1):
                return True
            mtx[row][col] = 0
    return False

#Checks if the input matrix is valid.
def initial_valid(mtx):
    for row in range(9):
        for col in range(9):
            n = mtx[row][col]
            if n != 0:
                
                mtx[row][col] = 0
                if not check_valid(mtx, row, col, n):
                    mtx[row][col] = n 
                    return False, (row, col, n)
                mtx[row][col] = n
    return True, None

def solve_sudoku(mtx):
    valid, bad_cell = initial_valid(mtx)
    if not valid:
        r, c, n = bad_cell
        print(f"{Fore.RED}Invalid Sudoku: duplicate {n} found at row {r+1}, col {c+1}.{Style.RESET_ALL}")
        return False

    if not sudo_rec(mtx, 0, 0):
        print(f"{Fore.RED}No solution exists for this Sudoku.{Style.RESET_ALL}")
        return False
    
    return True

#Prints the solved sudoku immediately after entry of user
def print_sudoku_grid(mtx, highlight=None):
    print("+-------+-------+-------+")
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            v = mtx[i][j]
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


#Prints the unsolved and solved sudoku side by side with entries of different colours
#Can be viewed in "View Saved Sudoku"
def side_by_side(original, solved):
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
            o_v = original[r][c]
            if o_v!=0:
                line2 += Fore.YELLOW+str(v)+Style.RESET_ALL + " "
            else:
                line2 +=Fore.CYAN+str(v)+Style.RESET_ALL + " "
            if (c + 1) % 3 == 0:
                line2 += "| "
        print(line1 + "   " + line2)
        if (r + 1) % 3 == 0:
            print("+-------+-------+-------+    +-------+-------+-------+")

def view_saved_sudokus(name, store):
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
            side_by_side(orig, solved)
            print()
            return
        print("Invalid input.\n")
