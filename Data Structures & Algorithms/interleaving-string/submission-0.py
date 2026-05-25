class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        if len(s3) != len(s1) + len(s2):
            return False
        
        if len(s3) == 0:
            return True

        def checkPerm(i, j):
            if i == len(s1):
                return s2[j] == s3[i + j]
            
            elif j == len(s2):
                return s1[i] == s3[i + j]
            
            key = (i, j)

            if key in dp:
                return dp[key]

            if s1[i] == s3[i + j] and s2[j] == s3[i + j]:
                dp[key] = checkPerm(i + 1, j) or checkPerm(i, j + 1)
            
            elif s1[i] == s3[i + j]:
                dp[key] = checkPerm(i + 1, j)
            
            elif s2[j] == s3[i + j]:
                dp[key] = checkPerm(i, j + 1)
            
            else:
                dp[key] = False
            
            return dp[key]
        
        return checkPerm(0, 0)
                