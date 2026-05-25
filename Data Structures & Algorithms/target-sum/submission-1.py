class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def nWays(i, target):

            if i == len(nums):
                return 0 if target != 0 else 1
            
            key = (i, target)

            if key not in dp:
                dp[key] = nWays(i + 1, target + nums[i]) + nWays(i + 1, target - nums[i])

            return dp[key]
        
        return nWays(0, target)