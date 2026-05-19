class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        
        def dfs(row, col):
            
            if row < 0 or row > m - 1:
                return
            
            elif col < 0 or col > n - 1:
                return

            elif visited[row][col]:
                return
            
            visited[row][col] = 1

            if grid[row][col] == '0':
                return

            for (row_add, col_add) in [(1,0), (0,1), (-1,0), (0,-1)]:
                
                dfs(row + row_add, col + col_add)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count += 1
                    dfs(i, j)
        
        return count