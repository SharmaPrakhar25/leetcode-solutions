class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [-1] * (len((nums) * 2))
        for i in range(len(ans)):
            if i < len(nums):
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-len(nums)]
        return ans
                      