import random
import itertools

def cellFiller(cella):
    for i in range(9):
        cella.append(random.sample(range(1,10), 9))
    return cella

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

cell = cellFiller([])

sudoku = sudokuGenerator(cell)
#for block in grouper(cell,3):
#   print(block)
for block in sudoku:
    print(block)
