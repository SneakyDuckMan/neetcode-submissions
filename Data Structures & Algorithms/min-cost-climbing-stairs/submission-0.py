class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [-1]*(len(cost) + 1)

        def climbCost(n):

            if n == 1 or n == 0:
                return 0

            elif dp[n] != -1:
                return dp[n]
            
            else:
                dp[n] = min(climbCost(n - 1) + cost[n - 1], climbCost(n - 2) + cost[n - 2])
                return dp[n]
        
        return climbCost(len(cost))