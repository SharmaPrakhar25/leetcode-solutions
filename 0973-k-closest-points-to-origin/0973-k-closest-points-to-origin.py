import math

class Node:
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []
        for idx in range(len(points)):
            point = points[idx]
            x, y = point[0], point[1]
            distance = math.sqrt(((x-0)** 2) + ((y-0)**2))
            curr = Node(idx, distance)
            self.heap.append(curr)
        
        self.heapify()
        ans = []
        for num in range(k):
            temp = self.pop()
            ans.append(points[temp.index])
        return ans

    def pop(self):
        if len(self.heap) == 0:
            return
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        ele = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return ele

    def heapify(self):
        if len(self.heap) == 0:
            return 
        
        curr = ((len(self.heap)-2) // 2)
        while curr >= 0:
            i = curr
            self._heapify_down(curr)
            curr -= 1
        return
    
    def _heapify_down(self, index):
        i = index
        while i < len(self.heap):
            left = 2 * i + 1
            right = 2 * i + 2
            small = i

            if left < len(self.heap) and self.heap[left].distance < self.heap[small].distance:
                small = left
            
            if right < len(self.heap) and self.heap[right].distance < self.heap[small].distance:
                small = right
            
            if small != i:
                self.heap[i], self.heap[small] = self.heap[small], self.heap[i]
                i = small
            else:
                break
        return


        