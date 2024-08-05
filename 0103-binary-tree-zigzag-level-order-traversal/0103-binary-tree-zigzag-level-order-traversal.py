# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([root])
        res = []
        l = 0
        while len(queue):
            temp = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                   
                if curr.right:
                    queue.append(curr.right)
            
            if l == 0:
                res.append(temp)
            else:
                res.append(temp[::-1])
            l = abs(l-1)
        return res