class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = Counter(nums)
        heap = [(-freq, num) for num, freq in countFreq.items()]
        heapq.heapify(heap)
        top_k = [heapq.heappop(heap)[1] for _ in range(k)]
        return top_k
        