class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
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
        idx = 0 
        for idx in range(len(haystack)):
            if idx + len(needle) - 1 < len(haystack) and haystack[idx:idx+len(needle)] == needle:
                return idx
        
        return -1