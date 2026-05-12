# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.prev = float('-inf')

        self.inorder(root)
        return self.ans

    def inorder(self, node):

        if node is None:
            return
        
        self.inorder(node.left)
        if node.val <= self.prev:
            self.ans = False
            return
        
        self.prev = node.val
        self.inorder(node.right)
