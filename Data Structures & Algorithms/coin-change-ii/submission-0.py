class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def no_of_ways(i, target):

            if i >= len(coins) or target < 0:
                return 0
            
            if target == 0:
                return 1
            
            key = (i, target)

            if key not in dp:
                dp[key] = no_of_ways(i + 1, target) + no_of_ways(i, target - coins[i])

            return dp[key]
        
        return no_of_ways(0, amount)