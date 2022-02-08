class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1
        idx = 0
        while idx <= high:
            if nums[idx] == 0:
                nums[low], nums[idx] = nums[idx], nums[low]
                low += 1
                idx += 1
            elif nums[idx] == 1:
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[high] = nums[high], nums[idx]
                high -= 1
            
        return nums
    
        # elem = 0 
        # left = 0
        # while left < len(nums):
        #     if nums[left] == elem:
        #         left += 1
        #     else:
        #         right = left + 1
        #         while right < len(nums):
        #             if nums[right] == elem:
        #                 nums[left], nums[right] = nums[right], nums[left]
        #                 left += 1
        #             right += 1
        #         elem += 1
        # return nums