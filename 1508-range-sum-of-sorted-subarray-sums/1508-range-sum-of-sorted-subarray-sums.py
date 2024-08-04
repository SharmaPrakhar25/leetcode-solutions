class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new_arr = []
        for i in range(n):
            for j in range(i+1, n+1):
                temp = sum(nums[i:j])
                new_arr.append(temp)
        
        new_arr.sort()
        return sum(new_arr[left-1:right]) % (10**9 + 7)
        
        