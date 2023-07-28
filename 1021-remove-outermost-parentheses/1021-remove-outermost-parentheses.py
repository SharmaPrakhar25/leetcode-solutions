class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        openParam = 0
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                openParam += 1
            
            if s[i] == ")":
                openParam -= 1
            
            if i > 0 and openParam == 0:
                ans += s[start+1:i]
                start = i + 1
        
        return ans

