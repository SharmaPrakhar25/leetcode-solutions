class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start = 0
        minLen = float('inf')
        tsum = 0
        for window_end in range(len(nums)):
            tsum += nums[window_end]
            if tsum >= target:
                while tsum >= target:
                    minLen = min(minLen, window_end - window_start + 1)
                    tsum -= nums[window_start]
                    window_start += 1
            
        return minLen if minLen != float('inf') else 0