class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        window_start = 0
        mapper = {}
        ans = 0 
        for window_end in range(len(s)):
            current_char = s[window_end]
            if current_char not in mapper:
                mapper[current_char] = 0
            mapper[current_char] += 1
            
            if mapper[current_char] > 1:
                while mapper[current_char] > 1:
                    left_char = s[window_start]
                    mapper[left_char] -= 1
                    window_start += 1
            ans = max(ans, window_end - window_start+1)
        return ans