# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def preOrder(self, root: TreeNode):
        res = []
        if root.left:
            res.append(root.left)
        if root.right:
            res.append(root.right)
        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        tempMap = {}
        if not root:
            return res
        
        currentLevel = 0
        currentNodes = []
        currentNodes.append(root)

        while len(currentNodes):
            nextNodes = []
            for i in range(len(currentNodes)):
                if currentLevel not in tempMap:
                    tempMap[currentLevel] = []

                tempMap[currentLevel].append(currentNodes[i].val)
                nextNodes.extend(self.preOrder(currentNodes[i]))
            currentLevel += 1
            currentNodes = nextNodes
            
        for values in tempMap.values():
            res.append(values)
        
        return res