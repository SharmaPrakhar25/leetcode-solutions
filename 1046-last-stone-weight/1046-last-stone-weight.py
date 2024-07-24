class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones
        self.heapify(self.heap)
        return self._simulation()
    
    def popFromLeft(self):
        if len(self.heap) == 0:
            return -1
        
        if len(self.heap) == 1:
            return self.heap.pop()

        element = self.heap[0]
        lastElement = self.heap.pop()
        if self.heap:
            self.heap[0] = lastElement
            self._heapify_down(0)
        return element
    
    def _simulation(self):
        while len(self.heap) > 1:
            firstStone = self.popFromLeft()
            if len(self.heap) == 0:
                return firstStone  # If there's only one stone left
            secondStone = self.popFromLeft()
            if firstStone != secondStone:
                self.heap.append(firstStone - secondStone)
                self._heapify_up(len(self.heap) - 1)
        return self.heap[0] if self.heap else 0

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            return
        
        self.heap = nums
        n = len(self.heap)
        
        # Start from the last non-leaf node and heapify down
        for curr in range((n - 2) // 2, -1, -1):
            self._heapify_down(curr)
        return

    def _heapify_down(self, index: int) -> None:
        size = len(self.heap)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            biggest = index
            
            # Check if left child exists and is smaller than current
            if left < size and self.heap[left] > self.heap[biggest]:
                biggest = left
            
            # Check if right child exists and is smaller than current (or left child)
            if right < size and self.heap[right] > self.heap[biggest]:
                biggest = right
            
            # If the smallest is not the current index, swap and continue heapifying down
            if biggest != index:
                self.heap[index], self.heap[biggest] = self.heap[biggest], self.heap[index]
                index = biggest
            else:
                break
        return 
    
    def _heapify_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break