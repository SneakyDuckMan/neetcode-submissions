# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        def dfs(node):

            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(right_height - left_height) > 1:
                self.ans = False
            
            return 1 + max(left_height, right_height)
        
        dfs(root)

        return self.ans