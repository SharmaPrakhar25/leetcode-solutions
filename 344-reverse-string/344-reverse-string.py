class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return s
        return self.reverseChar(s, 0, len(s)-1)
    
    def reverseChar(self,s, start, end):
        if end > start:
            s[start], s[end] = s[end], s[start]
            self.reverseChar(s, start+1, end-1)
        else:
            return s
        