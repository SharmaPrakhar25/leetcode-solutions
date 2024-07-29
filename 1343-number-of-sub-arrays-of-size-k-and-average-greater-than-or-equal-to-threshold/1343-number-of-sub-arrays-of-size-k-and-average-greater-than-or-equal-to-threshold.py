class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        numsMapper = {}
        for idx in range(len(arr)):
            numsMapper[idx] = arr[idx]
            
        L = 0
        avg = 0
        for R in range(len(arr)):
            avg += arr[R]
            if R-L+1 > k:
                avg -= arr[L]
                L += 1
        
            if R-L+1 == k:
                temp = avg/k
                if temp >= threshold:
                    res += 1
            
        return res
                    
            
        