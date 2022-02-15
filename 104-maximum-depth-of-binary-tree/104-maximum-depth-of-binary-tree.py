# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0 
        
        
        if root.left == None and root.right == None:
            return 1
        else:
            ldepth = 0
            if root.left is not None:
                ldepth = self.maxDepth(root.left)
                ldepth += 1

            rdepth = 0
            if root.right is not None:
                rdepth = self.maxDepth(root.right)
                rdepth += 1
    
        return max(ldepth,rdepth)
    