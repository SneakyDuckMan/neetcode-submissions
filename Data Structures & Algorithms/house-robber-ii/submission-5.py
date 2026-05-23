class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        dp1 = [-1]*(len(nums) - 1)
        dp2 = [-1]*(len(nums) - 1)

        def steal(i, nums, dp):

            if i < 0:
                return 0
            
            elif i == 0:
                return nums[0]
            
            elif i == 1:
                return max(nums[0], nums[1])
            
            elif dp[i] != -1:
                return dp[i]
            
            else:
                dp[i] = max(nums[i] + steal(i - 2, nums, dp), nums[i - 1] + steal(i - 3, nums, dp))

                return dp[i]
        
        nums2 = nums[1::]
        nums.pop()

        return max(steal(len(nums) - 1, nums, dp1), steal(len(nums2)- 1, nums2, dp2))
