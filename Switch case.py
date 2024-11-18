from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    match ch:
        case 1:
            result = math.pi * (a[0]*a[0])
            return ("{:.5f}".format(result))
        case 2:
            result = a[0]*a[1]
            return "{:.5f}".format(result)