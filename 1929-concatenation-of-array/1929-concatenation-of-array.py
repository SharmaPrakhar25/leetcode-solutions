class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        ans = [-1] * (numsLen * 2)
        ansLen = len(ans)
        for i in range(ansLen):
            if i < numsLen:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-numsLen]
        return ans
                      