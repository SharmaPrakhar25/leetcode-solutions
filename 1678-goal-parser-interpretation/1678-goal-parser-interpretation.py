class Solution:
    def interpret(self, command: str) -> str:
        ansStr = ''
        commandlen = len(command)
        idx=0
        while idx < len(command):
            print(idx)
            if command[idx] == 'G':
                ansStr += 'G'
                idx+=1
            elif idx+2 <= commandlen and command[idx:idx+2] == '()':
                ansStr += 'o'
                idx+=2
            elif idx+4 <= commandlen and command[idx:idx+4] == '(al)':
                ansStr += 'al'
                idx+=4
        
        return ansStr
                
                
            
        