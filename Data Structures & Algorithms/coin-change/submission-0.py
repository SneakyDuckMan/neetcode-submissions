class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = Counter(coins)

        def change(amount):

            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]

            elif amount < coins[0]:
                return -1
            
            ans = float('inf')
            for i in range(n - 1, -1, -1):

                check = change(amount - coins[i])
                if check == -1:
                    continue
                
                ans = min(ans, 1 + check)
            
            dp[amount] = ans if ans != float('inf') else -1
            
            return dp[amount]
        
        return change(amount)
                

                
