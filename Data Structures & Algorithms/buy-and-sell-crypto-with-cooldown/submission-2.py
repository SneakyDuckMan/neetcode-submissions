class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        dp = {}

        def maxp(i, buying):
            if i >= len(prices):
                return 0

            key = (i, buying)

            if key in dp:
                return dp[key]
            
            cooldown = maxp(i + 1, buying)

            if buying:
                profit = maxp(i + 1, not buying) - prices[i]

            else:
                profit = maxp(i + 2, not buying) + prices[i]

            dp[key] = max(profit, cooldown)

            return dp[key]
        
        return maxp(0, True)


            
