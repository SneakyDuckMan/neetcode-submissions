class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        dp= [[-1 for _ in range(n)] for _ in range(m)]

        def LCS(i, j):
            if i == m or j == n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            else:
                if text1[i] == text2[j]:
                    dp[i][j] =  1 + LCS(i + 1, j + 1)
                
                else:
                    dp[i][j] = max(LCS(i + 1, j), LCS(i, j + 1))
                
                return dp[i][j]
            
        return LCS(0, 0)

