from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
            print("output", output, "\n", "left", left)
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
    
        return output 


if __name__ == "__main__":
    nums = [int(input()) for i in range(5)]
    print(nums)
    solution = Solution()
    print(solution.productExceptSelf(nums))