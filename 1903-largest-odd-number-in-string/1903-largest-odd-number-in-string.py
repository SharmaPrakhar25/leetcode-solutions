class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        oddIndex = -1
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                oddIndex = i
                break
        
        if oddIndex == -1:
            return ""
        else:
            return num[0:oddIndex+1]