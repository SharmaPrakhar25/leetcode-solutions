class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_start, matched = 0, 0
        char_frequency = {}
        ans = []

        for chr in p:
            if chr not in char_frequency:
                char_frequency[chr] = 0
            char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_frequency:
          # decrement the frequency of matched character
              char_frequency[right_char] -= 1
              if char_frequency[right_char] == 0:
                matched += 1

            if matched == len(char_frequency):
                ans.append(window_start)

        # shrink the window by one character
            if window_end >= len(p) - 1:
                left_char = s[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        return ans
                    