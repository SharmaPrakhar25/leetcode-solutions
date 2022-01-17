class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapper = {}
        taken = set()
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        
        for idx in range(len(s)):
            if pattern[idx] not in mapper:
                if s[idx] not in taken:
                    mapper.setdefault(pattern[idx],s[idx])
                    taken.add(s[idx])
                else:
                    return False
            else:
                if mapper[pattern[idx]] != s[idx]:
                    return False
        
        return True
            
            