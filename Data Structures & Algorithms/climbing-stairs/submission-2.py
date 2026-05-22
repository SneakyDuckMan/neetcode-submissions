class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n + 1)

        def climb(n):

            if n == 1:
                return 1
            
            elif n == 2:
                return 2

            elif dp[n] != 0:
                return dp[n]
            
            else:
                dp[n - 1] = climb(n - 1)
                dp[n - 2] = climb(n - 2)

                return dp[n -1] + dp[n - 2]
        
        return climb(n)