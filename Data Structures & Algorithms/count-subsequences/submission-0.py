class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def nWays(i, j):
            if j == len(t):
                return 1
            
            if len(s) - i - 1 < len(t) - j - 1:
                return 0
            
            key = (i, j)

            if key in dp:
                return dp[key]
            
            if s[i] == t[j]:
                dp[key] = nWays(i + 1, j + 1) + nWays(i + 1, j)
            
            else:
                dp[key] = nWays(i + 1, j)
            
            return dp[key]
        
        return nWays(0, 0)