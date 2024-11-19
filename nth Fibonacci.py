def nth_fibonacci(n):
    if n==1 or n==2:
        return 1
    
    prev, curr = 1,1
    for i in range(3,n+1):
        prev,curr = curr,prev+curr

    return curr

n=int(input().strip())

print(nth_fibonacci(n))
