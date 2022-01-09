class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0  
        operationDict = {
            "A" : [x + 0, y + 1],
            "B" : [x + 1, y + 0],
            "C" : [x + 0, y - 1],
            "D" : [x - 1, y + 0]
        }
        instructions = instructions*4
        currState = 'A'
        for move in instructions:
            if move == 'G':
                x += operationDict[currState][0]
                y += operationDict[currState][1]

            if move == 'L':
                if currState == 'A':
                    currState = 'D'
                elif currState == 'D':
                    currState = "C"
                elif currState == 'C':
                    currState = 'B'
                elif currState == 'B':
                    currState = 'A'
            
            if move == 'R':
                if currState == 'A':
                    currState = 'B'
                elif currState == 'D':
                    currState = "A"
                elif currState == 'C':
                    currState = 'D'
                elif currState == 'B':
                    currState = 'C'
        
        if x == 0 and y == 0:
            return True
        else:
            return False