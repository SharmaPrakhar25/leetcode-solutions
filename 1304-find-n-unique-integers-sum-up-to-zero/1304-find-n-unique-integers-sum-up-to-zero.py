class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] * n
        num = n//2
        idx = 0 
        while num > 0:
            ans[idx] = num
            ans[n-idx-1] = -num
            num -= 1
            idx += 1  

        return ans
        