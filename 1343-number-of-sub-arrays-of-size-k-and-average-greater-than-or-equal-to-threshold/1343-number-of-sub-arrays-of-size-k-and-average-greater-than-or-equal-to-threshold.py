class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
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
        # for window_start in range(0, len(arr) -  k  + 1):
        #     curr_sum = 0
        #     for window_end in range(window_start, window_start + k):
        #         curr_sum += arr[window_end]
            
        #     if curr_sum // k >= threshold:
        #         res += 1
            
        return res
                    
            
        