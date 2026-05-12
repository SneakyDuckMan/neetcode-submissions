# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        self.view(root, 1)

        return self.ans


    def view(self, node, level):

        if node is None:
            return

        if level > len(self.ans):
            self.ans.append(node.val)
        
        self.view(node.right, level + 1)
        self.view(node.left, level + 1)
