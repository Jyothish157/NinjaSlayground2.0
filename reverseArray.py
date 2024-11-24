from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    l = 0
    r = n-1

    while l < r:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1

    return nums
