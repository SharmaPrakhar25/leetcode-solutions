class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] * n
        p = -(n//2)
        
        if(n % 2 == 1):
            for i in range(n):
                ans[i] = p
                p += 1
        else:
            for i in range(n):
                ans[i] = p
                p += 1
                if p == 0:
                    p+=1
        
        return ans
        