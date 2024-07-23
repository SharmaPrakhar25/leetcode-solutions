# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        currSum = 0
        def helper(root, targetSum, currSum):
            if not root.left and not root.right:
                temp = currSum + root.val
                if temp == targetSum:
                    return True
            
            currSum += root.val
            if root.left and helper(root.left, targetSum, currSum):
                return True
            
            if root.right and helper(root.right, targetSum, currSum):
                return True
            
            return False
        
        return helper(root, targetSum, currSum)

        