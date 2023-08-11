class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start)//2)
            if nums[mid] == target:
                return mid
            
            # left part is sorted
            if nums[mid] >= nums[start]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1