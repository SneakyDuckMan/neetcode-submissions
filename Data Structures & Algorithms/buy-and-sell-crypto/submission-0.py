class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        i = 1

        while i < len(prices) and prices[i] < prices[i-1]:
            i += 1
        
        if i == len(prices) - 1 and prices[i] < prices[i-1]:
            return 0

        curr_min = prices[0]

        for j in range(i - 1, len(prices)):
            
            curr_min = min(curr_min, prices[j])
            ans = max(ans, (prices[j] - curr_min))
        
        return ans