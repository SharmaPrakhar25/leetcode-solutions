# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            newNode = TreeNode(val)
            root = newNode
            return newNode
    
        if root.val > val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                newNode = TreeNode(val)
                root.left = newNode
        else:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                newNode = TreeNode(val)
                root.right = newNode
        
        return root