def search(nums: [int], target: int):
    # write your code logic !!
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l+r)//2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1 
