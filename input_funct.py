import solver

def inputSudoku():
    #User selects the mode of input 
    print("Enter method of sudoku input:\n")
    print("1. Enter whole sudoku.\n")
    print("2. Enter only filled coordinates and values.\n")
    choice=int(input("Enter your choice: "))
    
    if choice==2:  
        #Initializing the 9x9 matrix/sudoku with 0s
        m = [[0 for _ in range(9)] for _ in range(9)]
        print("Enter coordinates as a 2-digit number (column,row). Example: 43 means col=4, row=3.")
        print("Enter all filled coordinates separated by spaces. Example: 11 23 45 78\n")
        fs = input("Enter coordinates of filled squares: ").split()
        orig = set()
        #Checking a valid coordinate.
        for f in fs:
            if len(f) != 2 or not f.isdigit():
                print("Skipping invalid input: ", f)
                continue
            c = int(f[0]) - 1
            r = int(f[1]) - 1
            #Checking the range i.e. 1 to 9
            if not (0 <= r < 9 and 0 <= c < 9):
                print("Skipping out-of-range:", f)
                continue
            while True:
                v = input(f"Enter value at ({c+1},{r+1}): ").strip()
                #Checking entry.
                if v.isdigit():
                    v = int(v)
                    if 1 <= v <= 9:
                        break
                print("Enter a valid number 1-9.")
                #Checking whether coordinate is empty
            if not solver.checkValid(m, r, c, v):
                print("Conflict. Cannot place here.")
                continue
            m[r][c] = v
            orig.add((r, c))
        return m, orig
    
    elif choice==1:
        print("Enter row-wise while separating the numbers with spaces. ENTER 0 IF CELL IS EMPTY.")
        m=[]
        for i in range(9):
            while True:
                check=0
                l=input().split()
                filtered_l=list(filter(lambda x: x.isdigit() and int(x)>=0 and int(x)<=9,l))
                if len(filtered_l)==9:
                    l2=[int(num) for num in filtered_l]
                else:
                    print("Invalid input. Please enter digits between 0 and 9 only.")
                    continue
                if len(l2)!=9:
                    print("Invalid input. Please enter the row again.")
               
                else:
                    m.append(l2)
                    break
        
        orig=set()   
        for r in range(9):
            for c in range(9):
                if m[r][c]!=0:
                    orig.add((r,c))
        return m, orig
                
            
