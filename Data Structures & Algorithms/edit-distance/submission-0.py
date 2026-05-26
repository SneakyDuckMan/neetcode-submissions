class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dist(i, j):
            if i == len(word1):
                return len(word2) - j
            
            elif j == len(word2):
                return len(word1) - i
            
            key = (i, j)

            if key in dp:
                return dp[key]
            
            if word1[i] == word2[j]:
                dp[key] = dist(i + 1, j + 1)
            
            else:
                replace = 1 + dist(i + 1, j + 1)

                insert = 1 + dist(i, j + 1)

                delete = 1 + dist(i + 1, j)

                dp[key] = min(replace, insert, delete)

            return dp[key]

        return dist(0, 0)