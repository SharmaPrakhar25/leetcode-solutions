import math


def helperFunctionRootCalculator(x, n, m):
    """
    x : int number for raising the power
    n: int max number of power to which x can be raised
    m: int target number 


    response
    2: x to the power n is greater than m 
    1: x to the power n is equal to m 
    0: x to the power n is less than m
    """
    temp  = 0
    for i in range(n+1):
        temp  = x ** i
        if temp < m:
            continue

        if temp > m:
            return 2

        if temp == n:
            return 1
        
    return 0

def findNthRootOfM():
    """
    https://takeuforward.org/data-structure/nth-root-of-a-number-using-binary-search/
    """
    numbers = [int(x) for x in input().split(" ")]
    n = numbers[0]
    m = numbers[1]

    start = 1
    end = m
    while start <= end:
        mid = start + ((end - start) // 2)
        temp = mid ** n # calculating this might cause integer overflow if n and m are bigger numbers
        """
        The best way to tackle this to create a helper function and instead of calculating the power to n directly
        Use a loop to and raise the power from 1 to n 1 by 1 and as soon as the power becomes greater than m, discard the value of mid
        """
        if (temp == m):
            return mid

        if temp > m:
            end = mid - 1
        
        if temp < m:
            start = mid + 1

    return -1



def calculateHourHelper(arr, k):
    h = 0
    for num in arr:
        h += num // k
    
    return h


def kokoEatingBanana():
    bananaPiles = [int(x) for x in input().split(" ")]
    h = int(input())
    bananaPiles.sort() # nlog(n) tc 
    start = bananaPiles[0]
    end = bananaPiles[-1]
    k = end # what will the default output if the monkey can not eat bananas in the given hour (h)
    while start <= end:
        tempk= start + ((end - start)//2)
        tempH = calculateHourHelper(bananaPiles, tempk)

        if tempH > h:
            start = tempk + 1

        if tempH <= h:
            k = min(tempk, k)
            end = tempk - 1
    
    return k






if __name__  == "__main__":
    print(findNthRootOfM())