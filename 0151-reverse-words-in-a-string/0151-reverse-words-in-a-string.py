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
                    if ans != '':
                        ans = word + ' ' +ans
                    else:
                        ans = word + ans
                    word = ''
            else:
                word += s[i]
            
        if word != '':
            if ans != '':
                ans = word + ' ' +ans
            else:
                ans = word + ans
        
        return ans
                