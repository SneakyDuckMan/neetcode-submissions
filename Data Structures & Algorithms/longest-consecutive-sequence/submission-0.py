class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 0
        numSet = set(nums)

        for num in nums:
            if (num - 1) not in numSet:
                size = 1
                j = num + 1

                while j in numSet:
                    size += 1
                    j += 1

                ans = max(ans, size)

        return ans 