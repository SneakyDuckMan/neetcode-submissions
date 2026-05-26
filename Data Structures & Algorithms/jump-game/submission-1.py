class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True

        i = 0
        max_p = nums[0]

        while i < len(nums):
            if max_p >= len(nums) - 1:
                return True
            
            prev_max_p = max_p

            for j in range(i, max_p + 1):
                max_p = max(max_p, j + nums[j])
            
            if prev_max_p == max_p:
                return False
            
            i = prev_max_p
            