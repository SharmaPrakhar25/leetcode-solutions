class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        start = 0
        word = ''
        for i in range(len(s)):
            if s[i] == ' ':
                if word != '':
                    if len(ans) > 0:
                        ans = word + ' ' +ans
                    else:
                        ans = word + ans
                    word = ''
            else:
                word += s[i]
            
        if len(word) > 0:
            if len(ans) > 0:
                ans = word + ' ' +ans
            else:
                ans = word + ans
        
        return ans
                