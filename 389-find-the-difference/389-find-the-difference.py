class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_freq = {}
        for char in s:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
    
        for char in t:
            if char in char_freq and char_freq[char]:
                char_freq[char] -= 1
            else:
                return char
                
        