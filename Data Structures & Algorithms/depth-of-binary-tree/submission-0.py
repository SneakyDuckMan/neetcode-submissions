# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        self.traverse(root, 0)
        
        return self.ans
    
    def traverse(self, node, depth):

        if node is not None:
            depth += 1
            self.ans = max(self.ans, depth)
        
            self.traverse(node.left, depth)
            self.traverse(node.right, depth)
        