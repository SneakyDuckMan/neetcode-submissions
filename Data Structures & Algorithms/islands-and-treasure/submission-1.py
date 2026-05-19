class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        def dfs(row, col, dist):

            if row < 0 or row > m - 1:
                return
            
            elif col < 0 or col > n - 1:
                return
            
            elif grid[row][col] == -1:
                return
            
            if grid[row][col] <= dist and dist != 0:
                return

            else:
                grid[row][col] = dist

                for (row_add, col_add) in [(1,0), (0,1), (-1,0), (0,-1)]:
                    dfs(row + row_add, col + col_add, dist + 1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
