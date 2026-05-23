class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)

        def steal(i):

            if i < 0:
                return 0

            elif i == 0:
                return nums[0]
            
            elif i == 1:
                return max(nums[1], nums[0])

            elif dp[i] != -1:
                return dp[i]
            
            else:
                dp[i] = max(nums[i] + steal(i - 2), nums[i - 1] + steal(i - 3))
                return dp[i]
        
        return steal(len(nums) - 1)