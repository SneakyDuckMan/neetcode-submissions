class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums = [1] + nums + [1]

        def maxC(l, r):

            if l > r:
                return 0

            key = (l, r)
            if key in dp:
                return dp[key]
            
            ans = 0
            for i in range(l, r + 1):
                ans = max(ans, nums[i]*nums[l - 1]*nums[r + 1] + maxC(l, i - 1) + maxC(i + 1, r))

            dp[key] = ans

            return ans
        
        return maxC(1, len(nums) - 2)
