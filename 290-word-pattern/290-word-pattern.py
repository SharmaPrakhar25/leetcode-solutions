class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapper = {}
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        
        for idx in range(len(s)):
            if pattern[idx] not in mapper:
                if s[idx] not in mapper.values():
                    mapper.setdefault(pattern[idx],s[idx])
                else:
                    return False
            else:
                if mapper[pattern[idx]] != s[idx]:
                    return False
        
        return True
            
        # dct = {}
        # for i in range(len(pattern)):
        #     if pattern[i] not in dct:
        #         if s[i] not in dct.values():
        #             dct.setdefault(pattern[i], s[i])
        #         else:
        #             return False
        #     else:
        #         if dct[pattern[i]] != s[i]:
        #             return False
        # return True
            
            