import random
import itertools
import numpy as np

def cellFiller(cella):
    for row in range(9):
        cella[row] = random.sample(range(1,10), 9)
        for col in range(9):
            num_to_add = random.randint(1,9)
            passed = False
            while(not passed):
                if(num_to_add in cella[:, col]):
                    passed = True
                else:
                    print("ciao")
                    passed = False
        #cella.append(random.sample(range(1,10), 9))
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
cell = np.ndarray((9,9), int)
cell.fill(0)
cellFiller(cell)
sudoku = sudokuGenerator(cell)
#for block in grouper(cell,3):
#   print(block)
for block in sudoku:
    print(block)
