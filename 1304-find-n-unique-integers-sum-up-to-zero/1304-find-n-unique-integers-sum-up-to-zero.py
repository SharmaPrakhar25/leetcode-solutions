class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(n//2,0, -1):
            ans.append(i)
            ans.append(0-i)
                
        if n%2 == 1:
            ans.append(0) 
        
        return ans
        