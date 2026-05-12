# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root

        t1, t2 = p.val, q.val
        if t1 > t2:
            t1, t2 = t2, t1
        
        while node.val < t1 or node.val > t2:
            node = self.search(node, t1, t2)

        return node
    
    def search(self, node, t1, t2):

        if node.val < t1:
            return node.right
        
        elif node.val > t2:
            return node.left
        
        else:
            return node

