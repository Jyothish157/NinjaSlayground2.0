def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    flarge = float('-inf')
    slarge = float('-inf')
    fsmall = float('inf')
    ssmall = float('inf')

    for i in range(n):

        if a[i] > flarge and flarge != a[i]:
            slarge = flarge
            flarge = a[i]

        elif a[i] > slarge and a[i] < flarge:
            slarge = a[i]

        if a[i] < fsmall and fsmall != a[i]:
            ssmall = fsmall
            fsmall = a[i]

        elif a[i] < ssmall and a[i] > fsmall:
            ssmall = a[i]

    
    return slarge,ssmall
    
