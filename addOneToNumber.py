from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):
    #   Write your code here
    n = len(arr)

    carry = 1
    for i in range(n-1,-1,-1):
        new_digit = arr[i] + carry
        if new_digit < 10:
            arr[i] = new_digit
            carry = 0
            break
        else:
            arr[i] = 0
            carry = 1

    if carry:
        arr.insert(0,1)

    while len(arr) >1 and arr[0] == 0:
        arr.pop(0)

    return arr
