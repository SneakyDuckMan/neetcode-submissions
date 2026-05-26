class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        count = 0
        i = 0
        max_p = nums[0]

        while True:
            count += 1

            if max_p >= len(nums) - 1:
                return count

            for j in range(i, i + nums[i] + 1):

                if nums[j] + j >= max_p:
                    next_jump = j
                    max_p = nums[j] + j
            
            i = next_jump