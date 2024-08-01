# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minNumber, maxNumber):
            if not root:
                return True
            
            if root.val > minNumber and root.val < maxNumber:
                return dfs(root.left, minNumber, root.val) and dfs(root.right, root.val, maxNumber)
           
            return False 
            
    
        return dfs(root, -math.inf, math.inf)
        