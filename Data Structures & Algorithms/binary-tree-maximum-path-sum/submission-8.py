# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        if root is None:
            return 0
        
        self.pathSum(root)

        return self.ans

    
    def pathSum(self, node):
        
        if node is None:
            return 0
        
        left_sum = self.pathSum(node.left)
        right_sum = self.pathSum(node.right)

        self.ans = max(self.ans, node.val + max(left_sum + right_sum, left_sum, right_sum, 0))

        return node.val + max(left_sum, right_sum, 0)