# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.checkgood(root, float('-inf'))
        return self.ans

    def checkgood(self, node, max_so_far):
        
        if node is None:
            return
        
        if node.val >= max_so_far:
            max_so_far = node.val
            self.ans += 1
        
        self.checkgood(node.left, max_so_far)
        self.checkgood(node.right, max_so_far)
