class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        d1 = {x:0 for x in range(97,123)}
        d2 = {x:0 for x in range(97,123)}
        for i in range(len(s1)):
            d1[ord(s1[i])] += 1
            d2[ord(s2[i])] += 1
        i = 0
        j = len(s1)
        while j<=len(s2):
            if d1==d2:
                return True
            if j<(len(s2)):
                d2[ord(s2[j])] += 1
            d2[ord(s2[i])] -= 1
            i+=1
            j+=1
        return False