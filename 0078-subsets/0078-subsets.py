class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def helper(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            helper(i+1)
            subsets.pop()
            helper(i+1)
        
        helper(0)
        return res
            
            
            