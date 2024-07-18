class Solution:
    def __init__(self): 
        self.map = {}
        
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        if n not in self.map:
            self.map[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            
        return self.map[n]
        