# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modesMap = {}
        def dfs(curr):
            if curr is None:
                return
            
            if curr.val not in modesMap:
                modesMap[curr.val] = 0
            modesMap[curr.val] += 1
            dfs(curr.left)
            dfs(curr.right)
            return
        
        dfs(root)
        res = []

        maxVal = -math.inf
        for d in modesMap.values():
            maxVal = max(maxVal,d)
        
        for key in modesMap.keys():
            if modesMap[key] == maxVal:
                res.append(key)
        
        return res
        