class Solution:
    # def moveDuplicate(self, nums:List[int], index: int):
    #     for i in range(index, len(nums)-1):
    #         nums[i], nums[i+1] = nums[i+1], nums[i]
    #     return 
    
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 1
#         while i < len(nums)-1:
#             if nums[i-1] > nums[i]:
#                 return i
            
#             if nums[i] == nums[i-1]:
#                 self.moveDuplicate(nums, i)
#             else:
#                 i = i + 1
            
#         return
                
    
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        for right in range(n):
            if nums[left] != nums[right]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
        
        return left + 1
#         left = 0
#         right = 1
#         n = len(nums)
#         while right < n:
#             if nums[left] != nums[right]:
#                 left += 1
#                 nums[left], nums[right] = nums[right], nums[left]
            
#             right += 1
        
        return left+1
            