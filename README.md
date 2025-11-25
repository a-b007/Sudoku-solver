
# Sudoku Solver

**Team Name:** π-thon

**Project Title:** Sudoku Solver 

**Authors:**
- 1.)Anamitra Basu(Roll no. BC2025008)  
- 2.)Aaronya Chakraborty(Roll no. IC2025003)


## Short Description

An interactive command-line Sudoku solver implemented in Python that uses a recursive algorithm to solve 9×9 Sudoku puzzles. The application features user login, multiple input methods, colorful grid display, and the ability to save and view solved puzzles.

## Concepts Used

- **Higher Order Functions**: like filter.
- **Lambda Functions**
- **Comprehension**: for input.
- **Recursion**: Recursing all the possible combinations by placing a valid input and then backtracking if wrong.
- **Container Data Types**: 2D lists, dictionary, sets for tracking original positions
- **Funcions**: The program implements a modular approach to code the program. 
- **User Interface Design**: Menu-driven console application with colored output

## Libraries Used

### External Libraries
- **pyfiglet**: Art text generation for banner display.
- **colorama**: Coloured text output.

### Built-in Libraries
- **time**: For animated text display
- **sys**: For stdout manipulation
- **copy**: For deep copying sudoku grids

---

## Project Structure

The project contains the following files:

- *main.py*           
- *solver.py*        
- *input_funct.py*    
- *README.md*         


---

## Main Modules and Functions

### 1. **main.py** - Application Controller

**Purpose**: 
- User Dashboard
- Calls other functions(modular approach)

**Key Features**:
- "SUDOKU SOLVER" Animation.
- Menu-driven interface
**Allows user to:**
- Login
- Store sudoku
- View Saved Sudoku

**Example input/output**:

Input: User selects "Login" → Enters name "john"
Output: Creates profile for John and enables provision for solving/ viewing sudoku.



### 2. **solver.py** - Core Solving Logic

#### Function: `check_valid(mtx, row, col, n)`
**Purpose**: Validates if a number can be placed at given position

**Parameters**:
- `matrix`: 9×9 sudoku grid
- `row`, `col`: Position coordinates (0-8)
- `num`: Number to validate (1-9)

**Returns**: `True` if valid placement, `False` otherwise

**Example**:
```python
Input: checkValid(matrix, 0, 0, 5)
Output: True (if 5 doesn't violate row/column/box constraints)
```

#### Function: `sudoku_rec(mtx, row, col)`
**Purpose**: Recursively checks all valid combinations.

**Algorithm**:
1. Base case: Reached end of grid → return True
2. Checks for validity of a row, incrementing one column at a time.
3. Moves to next row by column 9.
4. Skip filled cells
5. Try numbers 1-9 at current position
6. If valid, place number and recurse
7. If recursion succeeds, return True
8. Backtrack by removing number and trying next


**Example**:
```python
Input: Partially filled 9×9 matrix
Output: Matrix filled with solution (returns True) or unchanged (returns False)
```

#### Function: `print_sudoku_grid(mtx, highlight=None)`
**Purpose**: Display sudoku grid with color coding

**Features**:
- Yellow text for original clues
- Cyan text for solved numbers
- Formatted grid with borders

**Example Output**:
```
+-------+-------+-------+
| 5 3 4 | 6 7 8 | 9 1 2 |
| 6 7 2 | 1 9 5 | 3 4 8 |
| 1 9 8 | 3 4 2 | 5 6 7 |
+-------+-------+-------+
```

#### Function: `view_saved_sudokus(name, store)`
**Purpose**: View previously solved sudokus side-by-side

**Example**:
```
Input: User "john" has 3 saved sudokus, selects #2
Output: Displays original and solved grids side-by-side
```

---

### 3. **input_funct.py** - Input Handling

#### Function: `input_sudoku()`
**Purpose**: Get sudoku puzzle from user with two input methods

**Method 1 - Full Grid Entry**:
```
Input: User enters 9 rows of 9 numbers (0 for empty)
Example Row: 5 3 0 0 7 0 0 0 0

Output: Stores the entered 9×9 matrix.
```

**Method 2 - Coordinate Entry**:
```
Input: 
  Coordinates: 11 23 45
  Values: 5, 8, 3 (for each coordinate)

Output: 9×9 matrix with values at specified positions
```

**Validation Features**:
- Checks for valid coordinate format
- Ensures coordinates are in range (1-9)
- Validates numbers are 1-9
- Prevents conflicts using `checkValid()`

---

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation Steps

1. **Download the Project Zip File**
   ```bash
   cd sudoku-solver
   ```

2. **Install Dependencies**
   ```bash
   pip install pyfiglet colorama
   ```

3. **Run the Application**
   ```bash
   python main.py
   ```
4. **Run the Application Alternative**
Project can be run without installing the Dependencies.
- Unzip the file and select the folder named *dist*
- Run 
```bash 
main.exe
```
---

## Usage Guide

### Example

1. Run the program: `python main.py`
2. Select option `2` (Solve without login)
3. Choose input method `1` (Enter whole sudoku)
4. Enter the following puzzle (row by row):

```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

5. View the solved puzzle with color-coded numbers!

