# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        answer = math.inf
        while start <= end:
            mid = start + ((end - start)//2)
            isCurrVersionBad = isBadVersion(mid)
            
            if isCurrVersionBad == True:
                answer = min(answer, mid)
                end = mid - 1
            
            if isCurrVersionBad == False:
                start = mid + 1
        
        return answer
                
        