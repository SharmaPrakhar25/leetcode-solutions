class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapper = {}
        s = s.split(' ')
        temps = []
        if len(s) != len(pattern):
            return False
        
        for idx in range(len(s)):
            if pattern[idx] not in mapper and s[idx] not in mapper.values():
                mapper[pattern[idx]] = s[idx]
                
        for char in pattern:
            if char not in mapper:
                return False
            else:
                temps.append(mapper[char])
        
        return True if temps == s else False
            
            
            
            