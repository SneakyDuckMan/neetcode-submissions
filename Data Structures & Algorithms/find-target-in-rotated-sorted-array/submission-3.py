class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1

        while start < end:
            
            mid = (start + end)//2

            if nums[mid] > nums[end]:
                start = mid + 1
            
            else:
                end = mid

        if target <= nums[len(nums) - 1] and target >= nums[start]:
            return self.binary(nums, target, start, len(nums) - 1)

        else:
            return self.binary(nums, target, 0, start - 1) 

        return -1

    def binary(self, nums, target, start, end):

        while start <= end:

            mid = (start + end)//2 

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid + 1
            
            else: 
                end = mid - 1
        
        return -1
