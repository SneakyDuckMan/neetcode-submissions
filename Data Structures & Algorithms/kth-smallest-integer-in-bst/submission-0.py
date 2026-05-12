# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        self.index = 0

        self.inorder(root)

        return self.ans

    
    def inorder(self, node):

        if node is None or self.index == k:
            return

        self.inorder(node.left)
        self.index += 1

        if self.index == k:
            self.ans = node.val
        
        self.inorder(node.right)