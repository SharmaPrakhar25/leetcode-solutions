# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            if root.left == None and root.right == None:
                return 1
            else:
                ldepth = float('inf')
                if root.left is not None:
                    ldepth = self.minDepth(root.left)
                    ldepth += 1
                
                rdepth = float('inf')
                if root.right is not None:
                    rdepth = self.minDepth(root.right)
                    rdepth += 1
                
                return min(ldepth, rdepth)
            
        