class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = set()
        nums.sort()
        for idx in range(len(nums)):
            # if nums[idx] + k > nums[idx+1]:
            #     continue
            # else:
            # pairIndex = self.binarySearchInArray(nums, idx+1, len(nums)-1, nums[idx] + k) 
            # print(pairIndex)
            # if pairIndex != False:
            #     print(nums[idx])
            #     count.add(nums[idx])
            low = idx + 1
            high = len(nums) - 1
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] == nums[idx] + k :
                    count.add(nums[idx])
                    break
                elif nums[mid] < nums[idx] + k:
                    low = mid + 1
                else:
                    high = mid - 1
        
        # print(count)
        return len(count)
        
    def binarySearchInArray(self, nums, start, end, target):
        if end >= start:
            pivot = start + (end-start) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                self.binarySearchInArray(nums, start, pivot-1,target)
            else:
                self.binarySearchInArray(nums, pivot+1, end, target)
        else:
            return False
        
        

        # nums.sort()
        # count = 0
        # left = 0
        # combination = {}
        # while left < len(nums) - 1: #for pair this should stop before one element is remaining -- FOCUS POINT (missed twice in last 2 days)
        #     right = len(nums) - 1
        #     while right > left:
        #         if abs(nums[left] - nums[right]) == k:
        #             if nums[left]+nums[right] not in combination:
        #                 count += 1
        #                 combination[nums[left]+nums[right]] = k
        #         right -= 1
        #     left += 1
            
#             right = len(nums) - 1
#             while right > left:
#                 parsedRightNumber = {}
#                 if abs(nums[left] - nums[right]) == k:
#                     count += 1
                
#                 prev = right - 1
#                 if nums[prev] == nums[right]:
#                     while prev > left and nums[prev] == nums[right]:
#                         prev -= 1
#                     right = prev
#                 else:
#                     right -= 1
            
#             if left not in parsedLeftNumber:
#                 parsedLeftNumber[left] = 0
#             parsedLeftNumber[left] += 1
#             next = left + 1
#             if next < len(nums) - 1 and nums[next] == nums[left]: #check on forward pointers 
#                 while nums[next] in parsedLeftNumber:
#                     next += 1
#                 left = next
#             else:
#                 left += 1

        
        return count
                    