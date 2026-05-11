# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        self.dfs(root)

        return self.ans

    def dfs(self, node):

        if node is None:
            return 0
        
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)

        self.ans = max(self.ans, left_height + right_height)

        return 1 + max(left_height, right_height)
