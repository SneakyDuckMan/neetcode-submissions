class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = [0]*n
        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node):

            if visited[node]:
                return
            
            visited[node] = 1

            for nei in adj[node]:
                dfs(nei)
        
        count = 0

        for v in range(n):
            if visited[v] == 0:
                count += 1
                dfs(v)
        
        return count
