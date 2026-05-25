class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = {}
        path = set()

        def lis(i, j):

            if i == m or j == n:
                return 0

            key = (i, j)

            if key in dp:
                return dp[key]

            ans = 1

            for (r, c) in [(1,0), (0,1), (-1,0), (0,-1)]:
                
                if i + r >= m or j + c >= n or i + r < 0 or j + c < 0:
                    continue

                if matrix[i + r][j + c] > matrix[i][j]:
                    ans = max(ans, lis(i + r, j + c) + 1) 

            dp[key] = ans

            return dp[key]
        
        res = 0

        for i in range(m):
            for j in range(n):
                res = max(res, lis(i, j))

        return res


