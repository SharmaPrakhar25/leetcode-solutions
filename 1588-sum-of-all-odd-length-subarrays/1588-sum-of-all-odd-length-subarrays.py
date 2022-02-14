class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0 
        for idx in range(len(arr)):
            j = idx
            counter = 1
            local = 0
            while j < len(arr):
                if counter % 2 == 1:
                    local += arr[j]
                    total += local
                else:
                    local += arr[j]
                j+=1
                counter+=1
        
        return total 