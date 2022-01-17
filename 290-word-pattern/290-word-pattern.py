class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapper = {}
        s = s.split(' ')
        # temps = []
        if len(s) != len(pattern):
            return False
        
        for idx in range(len(s)):
            if pattern[idx] not in mapper:
                if s[idx] not in mapper.values():
                    mapper[pattern[idx]] = s[idx]
                else:
                    return False
            else:
                if mapper[pattern[idx]] != s[idx]:
                    return False
                
        # for char in pattern:
        #     if char not in mapper:
        #         return False
        #     else:
        #         temps.append(mapper[char])
        
        # print(mapper)
        return True if len(set(pattern)) == len(mapper.keys()) else False
            
            
            
            