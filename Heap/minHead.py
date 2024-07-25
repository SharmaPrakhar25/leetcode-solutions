class MinHeap:
    def __init__(self):
        self.heap = [-1] * 1
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        # percolate up
        while self.heap[i] < self.head[i // 2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2
        return 
    
    
    def pop(self):
        if len(self.heap) == 1:
            return
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        ans = self.heap[1]
        lastElement = self.heap.pop()
        self.heap[1] = lastElement
        i = 1
        while 2 * i < len(self.heap):
            leftChildIdx = 2 * i
            rightChildIdx = 2 * i + 1
            smallestIdx = i
            
            if leftChildIdx < len(self.heap) and self.heap[leftChildIdx] < self.heap[smallestIdx]:
                smallestIdx = leftChildIdx
            
            if rightChildIdx < len(self.heap) and self.heap[rightChildIdx] < self.heap[smallestIdx]:
                smallestIdx = rightChildIdx
            
            if smallestIdx == i:
                break
            
            self.heap[i], self.heap[smallestIdx] = self.heap[smallestIdx], self.heap[i]
            i = smallestIdx
        
        return ans
    
        
    