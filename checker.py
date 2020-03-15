import random
import itertools
import numpy as np

s = 3
divs = 3
num_list = [k for k in range(1, s+1)]
def Diff(li1, li2, li3): 
    #li_dif = [i for i in li1 + li2 + li3 if i not in li1 or i not in li2 or i not in li3] 
    return list((set(li1) - set(li2)) - set(li3)) 

def get_square(x,y, grid):
    return grid[x*divs:x*divs+divs, y*divs:y*divs+divs]

def get_row(x,grid):
    return list(grid[x])

def get_col(y,grid):
    return list(grid[:, y])

def cellFiller(cella):
    for row in range(s):
        for col in range(s):
            tried = 0
            potential_list = Diff(num_list, get_row(row, cella), get_col(col, cella))
            while(True):
                if(potential_list):
                    potential_num = random.choice(potential_list)
                    #print(potential_num)
                    if(potential_num not in get_square(row//divs, col//divs, cella)):
                        cella[row][col] = potential_num
                        break
                    else:
                        tried += 1
                        if(potential_list.__len__() == tried):
                            print("unsolvable 1")
                            tmp = np.ndarray((s,s), int)
                            tmp.fill(0)
                            cellFiller(tmp)
                        else:
                            continue
                else:
                    tmp = np.ndarray((s,s), int)
                    tmp.fill(0)
                    cellFiller(tmp)
                    print("unsolvable 2")
    return cella

def sudokuGenerator(cella):
    for row in cella:
        for col in range(9):
            removeCol = random.randint(0,1)
            if(removeCol == 0):
                row[col] = 0
    return cella


'''def grouper(iterable, n, fillValue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillValue)
'''
cell = np.ndarray((s,s), int)
cell.fill(0)
cellFiller(cell)
print(cell)
#for block in grouper(cell,3):
#   print(block)