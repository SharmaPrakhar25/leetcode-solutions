class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:]
        heapq.heapify(heap)
        temp = len(heap) - k
        while temp >= 0:
            ans = heapq.heappop(heap)
            temp-=1
        return ans
        