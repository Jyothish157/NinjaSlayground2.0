def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    l,r = 0,n

    while l < r:
        mid = (l+r)//2
        if arr[mid] > x:
            r = mid
        else:
            l = mid + 1

    return l
