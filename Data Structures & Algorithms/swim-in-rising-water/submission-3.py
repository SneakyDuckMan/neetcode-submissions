class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0 for _ in range(n)] for _ in range(n)]

        heap = []
        heap.append((grid[0][0], 0, 0))

        while heap:
            h, row, col = heapq.heappop(heap)

            if visited[row][col] == 1:
                continue
            
            if row == n - 1 and col == n - 1:
                return h
            
            visited[row][col] = 1
            
            for r, c in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= row + r < n and 0 <= col + c < n:
                    heapq.heappush(heap, (max(h, grid[row + r][col + c]), row + r, col + c))
        

