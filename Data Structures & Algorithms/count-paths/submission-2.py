class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        dp[m - 1][n - 2] = 1
        dp[m - 2][n - 1] = 1

        dp[m - 1][n - 1] = 1

        def setDp(row, col):

            if row > m - 1:
                return 0
            
            elif col < 0 or col > n - 1:
                return 0
            
            if dp[row][col] == -1:
                dp[row][col] = setDp(row + 1, col) + setDp(row, col + 1)

            return dp[row][col]
        
        return setDp(0, 0)