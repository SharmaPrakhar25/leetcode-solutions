class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0] * 3
        for num in nums:
            temp[num] += 1
        
        i = 0
        for index in range(len(temp)):
            curr = index
            count = temp[index]
            while count > 0:
                nums[i] = curr
                i+= 1
                count -= 1
        return nums
        