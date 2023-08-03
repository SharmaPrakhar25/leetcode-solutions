class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        pow = abs(n)
        while pow > 0:
            if pow % 2 == 1:
                ans = ans * x
                pow = pow - 1
            else:
                x = x * x
                pow = pow // 2
        
        return ans if n > 0 else 1 / ans