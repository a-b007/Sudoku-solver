import solver
import input_funct
from pyfiglet import Figlet
import time, sys, copy

store_sudoku = {}
# Prints the "SUDOKU SOLVER" font.
fig = Figlet(font="banner3-d")
title = fig.renderText("SUDOKU SOLVER")

print("="*66, "\n")
for ch in title:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.001)
print("\n" + "="*66 + "\n")

def solve_and_store(name):
    
    #Catches the return value from the inputSudoku() function present in the file input_funct
    
    mtx, original = input_funct.inputSudoku()
    
    orig_copy = copy.deepcopy(mtx)
    # solveSudoku func in solver file returns boolean value of whether the sudoku is solveable.
    if not solver.solveSudoku(mtx):
        print("Unsolvable puzzle.\n")
        return
    
    print()
    #Calls the func printSudokuGrid
    solver.printSudokuGrid(mtx, highlight=original)
    while True:
        print("\n1. Store Sudoku")
        print("2. Return")
        c = input("Enter choice: ").strip()
        print()
        if c == "1":
            #We store the orinal as well as the solved sudoku in a  dictioanry of lists. 
            store_sudoku[name].append((orig_copy, copy.deepcopy(mtx)))
            print("Stored.\n")
            break
        if c == "2":
            break
        print("Invalid choice.")

while True:
    print("Hello user, welcome to Sudoku Solver ...")
    print("1. Login")
    print("2. Solve without login")
    print("3. Exit\n")
    ch = input("Enter your choice: ").strip()
    print()
    if ch == "3":
        print("Exiting...")
        break
    if ch == "2":
        mtx, original = input_funct.inputSudoku()
        if solver.solveSudoku(mtx):
            solver.printSudokuGrid(mtx, highlight=original)
        else:
            print("Unsolvable puzzle.\n")
        print()
        continue
    if ch == "1":
        name = input("Enter name: ").lower().strip()
        print()
        if name not in store_sudoku:
            #Created a new key in the dictionary of lists; lists are now empty.
            store_sudoku[name] = []
        while True:
            print(f"Hello {name.capitalize()},")
            print("1. Solve Sudoku")
            print("2. View Saved Sudokus")
            print("3. Back to main menu")
            c2 = input("Enter your choice: ").strip()
            if c2 == "1":
                solve_and_store(name)
            elif c2 == "2":
                solver.view_saved_sudokus(name, store_sudoku)
            elif c2 == "3":
                break
            else:
                print("Invalid input.\n")
    else:
        print("Invalid choice.\n")
        

