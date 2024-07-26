from typing import List
from collections import Counter
import heapq

class Solution:
    # Time complexity O(N * k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        countFreq = {}
        for num in nums:
            if num not in countFreq:
                countFreq[num] = 0
            countFreq[num]+=1
        
        while k > 0:
            curr = None
            maxFreq = -math.inf
            for key,val in countFreq.items():
                if val > maxFreq:
                    maxFreq = val
                    curr = key
            del countFreq[curr]
            ans.append(curr)
            k -= 1
        
        return ans


    def topKFrequentImproved(self, nums: List[int], k:int)-> List[int]:
        countFreq = Counter(nums)
        # used heaps to improve the time complexity 
        heap = [(-freq, num) for num, freq in countFreq.items()]
        heapq.heapify(heap)
        
        top_k = [heapq.heappop(heap)[1] for _ in range(k)]
        return top_k


                

if __name__ == "__main__":
    solution = Solution()
    ans = solution.topKFrequentImproved([1,2,2,3,3,3], 2)
    print(ans)
    