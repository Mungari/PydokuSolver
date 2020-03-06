import random
import itertools

def cellFiller(cella):
    for i in range(9):
        cella.append(random.sample(range(1,10), random.randint(3,5)))
    return cella

def grouper(iterable, n, fillValue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillValue)

cell = cellFiller([])
for block in grouper(cell,3):
    print(block)