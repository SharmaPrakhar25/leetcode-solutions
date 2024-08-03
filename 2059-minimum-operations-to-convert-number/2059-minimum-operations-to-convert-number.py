from collections import deque
from typing import List
import math

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        if start == goal:
            return 0
        
        # Use a queue to perform BFS
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            currVal, stepCount = queue.popleft()
            
            # Try all operations
            for num in nums:
                for newVal in [currVal + num, currVal - num, currVal ^ num]:
                    if newVal == goal:
                        return stepCount + 1
                    if 0 <= newVal <= 1000 and newVal not in visited:
                        visited.add(newVal)
                        queue.append((newVal, stepCount + 1))
        
        # If no solution is found
        return -1
