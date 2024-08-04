class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new_arr = []
        for i in range(n):
            tempSum = nums[i]
            new_arr.append(tempSum)
            for j in range(i+1, n):
                # temp = sum(nums[i:j])
                tempSum += nums[j]
                new_arr.append(tempSum)
        
        new_arr.sort()
        return sum(new_arr[left-1:right]) % (10**9 + 7)
        
        