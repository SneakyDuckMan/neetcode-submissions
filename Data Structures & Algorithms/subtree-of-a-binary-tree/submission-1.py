# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans = False
        self.traverse(root, subRoot)

        return self.ans
    
    def traverse(self, node, subRoot):
        if node is None:
            return
        
        elif node.val == subRoot.val:
            
            self.ans  = self.isSame(node, subRoot) or self.ans

        self.traverse(node.left, subRoot)
        self.traverse(node.right, subRoot)
        

    def isSame(self, n1, n2):

        if n1 is None and n2 is None:
            return True
        
        elif n1 is None and n2 is not None:
            return False
        
        elif n2 is None and n1 is not None:
            return False
        
        if n1.val != n2.val:
            return False
        
        else:
            return self.isSame(n1.left, n2.left) and self.isSame(n1.right, n2.right)
        
