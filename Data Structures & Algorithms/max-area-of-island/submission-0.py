class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def dfs(row, col):
            if row < 0 or row > m - 1:
                return
            
            elif col < 0 or col > n - 1:
                return

            elif grid[row][col] == 0:
                return

            self.area += 1
            grid[row][col] = 0

            for (row_add, col_add) in [(1,0), (0,1), (-1,0), (0,-1)]:
                
                dfs(row + row_add, col + col_add)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.area = 0
                    dfs(i, j)
                    ans = max(ans, self.area)
        
        return ans
