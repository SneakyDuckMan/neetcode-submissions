class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        ans = 0
        adj = [[] for _ in range(n)]

        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        heap = []
        heap.append((0, src, -1))

        visited = [0]*n

        while heap:
            cost_so_far, airport, stops = heapq.heappop(heap)
            
            if visited[airport] or stops > k:
                continue
            
            if airport == dst:
                return cost_so_far

            visited[airport] = 1

            for nei, price in adj[airport]:

                if visited[nei] == 0:
                    heapq.heappush(heap, (cost_so_far + price, nei, stops + 1))
                
            visited[airport] = 0

        return -1

