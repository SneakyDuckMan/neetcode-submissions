class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 0

        start = 0
        end = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while start <= end:

            mid = (start + end)//2

            if mid == 0:
                if nums[1] > nums[0]:
                    return nums[0]
                
                else:
                    return nums[1]

            elif nums[mid] < nums[mid - 1]:
                return nums[mid]

            elif nums[mid] < nums[0]:
                end = mid - 1

            else:
                start = mid + 1

        return nums[0]