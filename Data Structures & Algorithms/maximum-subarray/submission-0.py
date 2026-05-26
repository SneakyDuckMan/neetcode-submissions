class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            ans = max(curr_sum, ans)

            if curr_sum < 0:
                curr_sum = 0
            
        return ans