from collections import *
from math import *

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    result = []
    for i in range(n):
        row = [1]
        for j in range(1,i):
            row.append(result[i-1][j-1] + result[i-1][j])
        if i > 0:
            row.append(1)
        result.append(row)
    return result
