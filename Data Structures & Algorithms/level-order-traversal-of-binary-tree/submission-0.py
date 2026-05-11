# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        level = 0

        self.traverse(root, 1)

        return self.ans
    
    def traverse(self, node, level):

        if node is None:
            return
        
        if len(self.ans) < level:
            self.ans.append([])

        self.ans[level - 1].append(node.val)

        self.traverse(node.left, level + 1)
        self.traverse(node.right, level + 1)