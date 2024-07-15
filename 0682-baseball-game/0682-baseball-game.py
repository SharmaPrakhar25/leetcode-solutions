class Solution:
    def isNumber(self, c: str) -> bool:
        if not c:
            return False
        
        if c[0] == '-':
            if len(c) == "-":
                return False
            newC = c[1:]
        else:
            newC = c
            
        return all('0' <= char <= '9' for char in newC)
    
    def calPoints(self, operations: List[str]) -> int:
        answer = []
        score = 0
        for operation in operations:
            isANumber = self.isNumber(operation)
            if operation == "C":
                answer.pop()
            elif operation == 'D':
                prevScore = answer[-1]
                answer.append(prevScore * 2)
            elif isANumber:
                answer.append(int(operation))  
            elif operation == "+":
                score1 = answer[-1]
                score2 = answer[-2]
                answer.append(score1+score2)
            
        for num in answer:
            score += num
        
        return score
        