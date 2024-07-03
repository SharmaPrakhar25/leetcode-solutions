class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        currentSum = nums[0]
        maxSum = currentSum
        
        for i in range(1, len(nums)):
            if currentSum < 0:
                currentSum = 0
                
            currentSum += nums[i]
            maxSum = max(maxSum, currentSum)
            
        return maxSum
            