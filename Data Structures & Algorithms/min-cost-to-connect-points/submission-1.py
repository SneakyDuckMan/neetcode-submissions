class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = [False]*n
        min_dist = [float('inf')]*n

        min_dist[0] = 0
        ans = 0

        for _ in range(n):
            
            point = -1
            for i in range(n):    
                if visited[i]:
                    continue

                if point == -1 or min_dist[i] < min_dist[point]:
                    point = i
        
            x, y = points[point]
            visited[point] = True
            ans += min_dist[point]

            for v in range(n):
                if visited[v]:
                    continue
                
                d = abs(points[v][0] - x) + abs(points[v][1] - y)
                min_dist[v] = min(min_dist[v], d)
        
        return ans
