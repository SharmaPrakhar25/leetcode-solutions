class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for i in range(len(s)):
            ans = ans ^ ord(s[i]) ^ ord(t[i])
            print(ans)
        ans ^= ord(t[-1])
        return chr(ans)
#         char_freq = {}
#         for char in s:
#             if char not in char_freq:
#                 char_freq[char] = 0
#             char_freq[char] += 1
    
#         for char in t:
#             if char in char_freq and char_freq[char]:
#                 char_freq[char] -= 1
#             else:
#                 return char

                
        