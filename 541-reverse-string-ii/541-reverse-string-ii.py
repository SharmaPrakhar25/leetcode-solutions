class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k: return s[::-1]
        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k)
    
    """
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) > k:
            start_idx, end_index = 0, 2*k
            self.reverseKChar(s, start_idx, end_index, k)
        else:
            self.reverseKChar(s, 0, len(s), k)

        return s


    def reverseKChar(self, s, start, end, k):
        if end > len(s):
            end = len(s)

        if len(s) > k:
            s = s[start:end][k-1::-1] + s[k:]
            print(s)
            start = end
            end += k * 2
            self.reverseKChar(s, start, end, k)
        else:
            s = s[::-1]

        return s
    """
    
        