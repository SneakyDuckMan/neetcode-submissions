# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.ans = []

        def preorder(node):
            if node is None:
                self.ans.append("N")
                return
            
            self.ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)

        
        return ",".join(self.ans)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        data = data.split(",")
        self.i = 0
        def buildTree():
            
            if self.i >= len(data):
                return None

            if data[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = buildTree()
            node.right = buildTree()

            return node
        
        return buildTree()
