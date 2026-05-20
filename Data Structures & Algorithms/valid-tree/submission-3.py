class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        visited = [0]*n
        
        adj = [[] for _ in range(n)]

        for edge in edges:

            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node, prev):

            if visited[node] == 1:
                return False
            
            visited[node] = 1

            for nei in adj[node]:
                if nei == prev:
                    continue

                if not dfs(nei, node):
                    return False
            
            return True
        
        for node in range(n):
            if visited[node] == 0:
                if not dfs(node, -1):
                    return False
        
        return True
            

