def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    l,r = 0,n-1
    ans = n
    while l <= r:
        mid = (l+r)//2

        if arr[mid] >= x:
            ans = mid
            r = mid -1
        else:
            l +=1

    return ans
