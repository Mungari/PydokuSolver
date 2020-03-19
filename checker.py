import random
import itertools
import numpy as np

s = 9
divs = 3
num_list = [k for k in range(1, s+1)]
def Diff(li1, li2, li3, li4): 
    #li_dif = [i for i in li1 + li2 + li3 if i not in li1 or i not in li2 or i not in li3] 
    return list((set(li1) - set(li2)) - set(li3) - set(li4)) 

def get_square(x,y, grid):
    return grid[x*divs:x*divs+divs, y*divs:y*divs+divs].flatten()

def get_row(x,grid):
    return grid[x]

def get_col(y,grid):
    return grid[:, y]

def cellFiller(cella, x, y):
    potential_list = Diff(num_list, get_row(y, cella), get_col(x, cella), get_square(y//divs, x//divs, cella))
    random.shuffle(potential_list)
    for potential_num in potential_list:
        if(0 in cella):
            cella[y][x] = potential_num
            if(x == s - 1 and y == s - 1):
                return
            else:
                if(x == s - 1 and y < s - 1):
                    cellFiller(cella, 0, y + 1) #If all goes well, and I'm out of spaces on the row, I increment to the next column
                else:
                    if(x < s - 1 and y <= s - 1):
                        cellFiller(cella, x + 1, y) #Same as above, but if I still have spaces to fill in the row
        else:
            return True
    if(0 not in cella):
        return True
    else:
        cella[y][x] = 0
        return False

def sudokuGenerator(cella):
    for row in cella:
        for col in range(9):
            removeCol = random.randint(0,1)
            if(removeCol == 0):
                row[col] = 0
    return cella


def grouper(iterable, n, fillValue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillValue)

cell = np.ndarray((s,s), int)
cell.fill(0)
cellFiller(cell, 0, 0)
print(cell)