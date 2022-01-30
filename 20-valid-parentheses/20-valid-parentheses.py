class Solution:
    def isValid(self, s: str) -> bool: 
        openingBracketSet = set(['[','{','('])
        closingBracketSet = set([']','}',')'])
        openList = []
        mapper = {
            '}': '{',
            ')': '(',
            ']': '[' 
        }
#         {(}}
        for char in s:
            if char in closingBracketSet:
                if len(openList) < 1:
                    return False
                else:
                    if openList[-1] == mapper[char]:
                        del openList[-1]
                    else:
                        return False
            else:
                openList.append(char)
        
        return True if len(openList) == 0 else False