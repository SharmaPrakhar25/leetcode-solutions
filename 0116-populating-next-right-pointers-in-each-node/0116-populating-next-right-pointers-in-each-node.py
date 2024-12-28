"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        queue = deque([root])
        while len(queue):
            temp = deque([])
            for _ in range(len(queue)):
                curr = queue.popleft()
                if len(queue):
                    curr.next = queue[0]
                
                if curr.left:
                    temp.append(curr.left)
                
                if curr.right:
                    temp.append(curr.right)     
            queue = temp
        return root