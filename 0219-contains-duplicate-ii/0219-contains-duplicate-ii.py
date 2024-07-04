class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        windowData = set()
#         o(n2)
        # for L in range(len(nums)):
        #     for R in range(L+1, min(len(nums),L+k+1)):
        #         if nums[L] == nums[R]:
        #             return True

#         O(n)
        L = 0
        for R in range(len(nums)):
            if abs(R - L) > k:
                windowData.remove(nums[L])
                L += 1
            
            if nums[R] in windowData:
                return True
            windowData.add(nums[R])     
        return False