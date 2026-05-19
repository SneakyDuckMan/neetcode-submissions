"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        link = {}
        if node is None:
            return None

        def dfs(node):        
            
            copy = Node(node.val)
            link[node] = copy
            
            for v in node.neighbors:
                if v not in link:
                    dfs(v)

                copy.neighbors.append(link[v])

        dfs(node)

        return link[node]

