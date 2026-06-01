class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        ans = 1

        def lis(i):

            if dp[i] != -1:
                return dp[i]

            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], lis(j) + 1)
                
            dp[i] = max(dp[i], 1)
            return dp[i]

        for i in range(len(nums)):
            ans = max(lis(i), ans)
            
        return ans