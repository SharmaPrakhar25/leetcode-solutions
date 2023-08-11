class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        2,0,2,1,1,0 
        zero_index = we will do a for loop and get 0th index for 0 number 
        last_index = we will do another for loop and 5th index for 2 number 
        
        one_index = we will start from 1st index and one_index < last_index
        if one_index == 1:
            one_index += 1
        
        if one_index == 0:
            replace the number at zero_index and one_index += 1 and zero_index += 1
        
        if one_index == 2:
            replace the number at last_index and last_index -= 1
        """
        red, white = 0, 0 
        blue = len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1  
        return  
                