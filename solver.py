import random
import string
import time


def pretty_print_grid(grid):
    for i, row in enumerate(grid):
        if i % 3 == 0:
            print("-" * 25)
        temp = []
        for j, col in enumerate(row):
            if j % 3 == 0:
                temp.append("|")
            temp.append(str(col))
        temp.append("|")
        print(" ".join(temp))
    print("-" * 25)


def find_empty_cell(grid):
    for i, row in enumerate(grid):
        try:
            return i, row.index(0)
        except ValueError:
            continue
    else:
        return -1, -1

# grid = [[random.choice(string.digits) for i in range(9)] for i in range(9)]
grid = [
    [3,0,6,5,0,8,4,0,0], 
    [5,2,0,0,0,0,0,0,0], 
    [0,8,7,0,0,0,0,3,1], 
    [0,0,3,0,1,0,0,8,0], 
    [9,0,0,8,6,3,0,0,5], 
    [0,5,0,0,9,0,6,0,0], 
    [1,3,0,0,0,0,2,5,0], 
    [0,0,0,0,0,0,0,7,4], 
    [0,0,5,2,0,6,3,0,0]] 

# pretty_print_grid(grid)
# print(find_empty_cell(grid))

def is_row_ok(row, num):
    return num not in row

def is_column_ok(grid, pos, num):
    temp = []
    for row in grid:
        temp.append(row[pos[1]])

    return is_row_ok(temp, num)

def is_block_ok(grid, pos, num):
    r = pos[0]
    c = pos[1]
    temp = []
    for i in range(r - r % 3, 3 + r - r % 3):
        for j in range(c - c % 3, 3 + c - c % 3):
            temp.append(grid[i][j])
    return is_row_ok(temp, num)

def is_safe(grid, num, pos):
    return is_row_ok(grid[pos[0]], num) and is_column_ok(grid, pos, num) and is_block_ok(grid, pos, num)

def solver(grid):
    pos = find_empty_cell(grid)
    if pos == (-1, -1):
        return True
    
    for num in range(1, 10):

        if is_safe(grid, num, pos):
            grid[pos[0]][pos[1]] = num
        
            if solver(grid):
                return True
            
            grid[pos[0]][pos[1]] = 0

    return False

if __name__ == "__main__":
    solver(grid)
    pretty_print_grid(grid)