class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for right in range(n-1):
            if nums[right] == nums[right+1]:
                nums[right] *= 2
                nums[right+1] = 0
        
        
        def moveZeroesToEndHelper(arr):
            n = len(arr)
            left = 0
            for right in range(n):
                if arr[right] != 0:
                    arr[right], arr[left] = arr[left], arr[right]
                    left+= 1
            return arr
        
        return moveZeroesToEndHelper(nums)
                    
                