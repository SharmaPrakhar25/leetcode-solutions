class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        nedlen = len(needle)
        haystacklen = len(haystack)
#         if len(needle) > len(haystack):
#             return -1
        
#         ansIdx = None
#         nedidx = 0
#         idx = 0
#         while nedidx < len(needle) and idx < len(haystack):
#             if haystack[idx] == needle[nedidx]:
#                 if nedidx == 0:
#                     nedidx += 1
#                     ansIdx = idx
#                 else:
#                     nedidx += 1
#             else:
#                 if nedidx == len(needle):
#                     return ansIdx
#                 else:
#                     nedidx = 0
#             idx += 1
            
#         return ansIdx if ansIdx != None else -1
        for idx in range(haystacklen - nedlen + 1):
            if haystack[idx:idx+nedlen] == needle:
                return idx
        
        return -1