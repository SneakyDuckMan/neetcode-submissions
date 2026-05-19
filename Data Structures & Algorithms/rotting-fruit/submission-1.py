class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        self.fresh = 0
        q = deque()

        self.time = 0
        dist = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                
                elif grid[i][j] == 1:
                   self.fresh += 1

        def setCond(row, col, dist):

            if row < 0 or row > m - 1:
                return
            
            elif col < 0 or col > n - 1:
                return
            
            elif grid[row][col] != 1:
                return
            
            else:
                self.time = max(self.time, dist)
                grid[row][col] = 2
                self.fresh -= 1

                q.append((row, col))
        
        while q:
            for i in range(len(q)):
                (row, col) = q.popleft()

                for (r, c) in [(1,0), (0,1), (-1,0), (0,-1)]:
                    setCond(row + r, col + c, dist)
            
            dist += 1
        
        return self.time if not self.fresh else -1



            

