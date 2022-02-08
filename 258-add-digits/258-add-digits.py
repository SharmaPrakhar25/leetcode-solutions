class Solution:
    def addDigits(self, num: int) -> int:
        ansSum = 0
        while num > 0:
            ansSum += num % 10
            num = num // 10 
            if num == 0 and ansSum >= 10:
                num = ansSum
                ansSum = 0      
        return ansSum
            
        