class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap = nums
        ans = []
        self.heapify()
        for _ in range(len(nums)):
            temp = self.pop()
            ans.append(temp)
        return ans
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        ele = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return ele
    
    def heapify(self):
        size = len(self.heap)
        for i in range((size - 2) // 2, -1, -1):
            self._heapify_down(i)
    
    def _heapify_down(self, index):
        size = len(self.heap)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
        return
    