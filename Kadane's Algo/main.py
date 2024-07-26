from typing import List
import math
# Time Complexity O(n^2)
def kadanesAlgoBruteForce(nums: List[int])-> int:
    maxSum = -math.inf
    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            currSum += nums[j]
            maxSum = max(currSum, maxSum)
        
    return maxSum

# Time Complexity - O(n)
def kadanesAlgoBruteForce2(nums: List[int])-> int:
    maxSum = -math.inf
    '''
    either define currSum = 0 and intialize the for loop from the 0th index
    or define currSum from 0th index such as currSum = arr[0] and and run the for loop from the first index
    THIS IS NOT CORRECT
    '''
    currSum = 0
    L, R = 0, 0
    tempL = 0
    for tempR in range(len(nums)):
        # currSum = max(currSum, 0)
        # currSum += nums[i]
        if currSum < 0:
            tempL = tempR
            currSum = nums[tempR]
       
        currSum += nums[tempR]
            
        if currSum > maxSum:
            maxSum = currSum
            L = tempL
            R = tempR
    
    subArray = nums[L:R+1]
    print(f"Left index is {L} and right index is {R}")
    print('Subarray is - ',subArray)
    return maxSum 


if __name__ == "__main__":
    # print(kadanesAlgoBruteForce([4,-1,2,-7,3,4]))
    print(kadanesAlgoBruteForce2([4,-1,2,-7,3,4]))
    # print(kadanesAlgoBruteForce2([-2,-3,-4,-1,-2,-1,-5,-3]))
    pass
