class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        leftPos, rightPos = -1,-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                leftPos = mid
                right = mid-1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                rightPos = mid
                left = mid+1
            elif nums[mid] > target:
                right = mid-1 
            else:
                left = mid+1

        return [leftPos, rightPos]
            