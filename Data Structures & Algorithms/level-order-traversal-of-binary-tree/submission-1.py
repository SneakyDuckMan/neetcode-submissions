# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return [] 

        ans = []
        q = deque()
        q.append(root)
        while q:
            length = len(q)
            ans.append([])

            for _ in range(length):

                node = q.popleft()
                ans[-1].append(node.val)

                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)
        
        return ans


            

