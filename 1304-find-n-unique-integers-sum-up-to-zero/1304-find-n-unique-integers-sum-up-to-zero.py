class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] * n
        idx = 0
        for i in range(n//2,0, -1):
            ans[idx]  = i
            ans[n-idx-1] = 0-i
            idx+=1
            
        
        return ans
        