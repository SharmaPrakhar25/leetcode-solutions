class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] * n
        num = n//2
        idx = 0 
        # while num > 0:
        #     ans[idx] = num
        #     ans[n-idx-1] = -num
        #     num -= 1
        #     idx += 1  
        
        for i in range(-(n//2), n//2+1, 1):
            if i==0 and n%2==0:
                continue;   
            ans[idx] = i
            idx+=1
            
        return ans
        