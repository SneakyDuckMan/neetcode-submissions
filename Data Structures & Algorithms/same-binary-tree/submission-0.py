# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.ans = True

        self.isSame(p, q)
        return self.ans

    def isSame(self, n1, n2):

        if n1 is None and n2 is None:
            return
        
        elif n1 is None and n2 is not None:
            self.ans = False
            return
        
        elif n2 is None and n1 is not None:
            self.ans = False
            return
        
        if n1.val != n2.val:
            self.ans = False
            return

        else:
            self.isSame(n1.left, n2.left)
            self.isSame(n1.right, n2.right)