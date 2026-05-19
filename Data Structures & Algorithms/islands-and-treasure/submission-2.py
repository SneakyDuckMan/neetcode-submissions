class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = deque()

        dist = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        def setDist(row, col, dist):
            if (row < 0 or row > m - 1):
                return

            elif (col < 0 or col > n -1):
                return

            elif grid[row][col] == -1: 
                return

            elif (row, col) in visited:
                return
            
            else:
                visited.add((row, col))
                grid[row][col] = dist

                q.append((row, col))


        while q:
            size = len(q)
            for i in range(size):
                (row, col) = q.popleft()

                for (row_add, col_add) in [(1,0), (0,1), (-1,0), (0,-1)]:
                    setDist(row + row_add, col + col_add, dist)
            
            dist += 1
        
            
        



