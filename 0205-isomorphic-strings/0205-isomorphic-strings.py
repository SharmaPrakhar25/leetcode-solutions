class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            c1 , c2 = s[i], t[i]
            if (s[i] in map1 and map1[s[i]] != t[i]) or (t[i] in map2 and map2[t[i]] != s[i]):
                return False
                
            map1[s[i]] = t[i]
            map2[t[i]] = s[i]
            
        return True