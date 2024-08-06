class Solution:
    def minimumPushes(self, word: str) -> int:
        push_count = 0
        counter = Counter(word)
        key_map = {}
        for key, value in counter.most_common():
            key_map[key] = (push_count//8) + 1
            push_count += 1
            
        res = 0
        for s in word:
            res += key_map[s]
        return res