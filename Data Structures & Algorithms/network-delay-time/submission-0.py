class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        visited = [0]*n
        heap = []
        dist = [0]*n

        adj = [[] for _ in range(n)]

        for edge in times:
            adj[edge[0] - 1].append((edge[2], edge[1]))

        heap.append((0, k))

        while heap:

            time, node = heapq.heappop(heap)
            if visited[node - 1] == 1:
                continue
            
            else:
                visited[node - 1] = 1
                dist[node - 1] = time

                for t, nei in adj[node - 1]:
                    heapq.heappush(heap, (time + t, nei))
        
        for visit in visited:
            if visit == 0:
                return -1
        
        return max(dist)