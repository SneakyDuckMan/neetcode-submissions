class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        nums = sorted(nums)

        self.twoSum(nums, 0)

        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i-1]:
                continue

            self.twoSum(nums, i)
        
        return self.ans
    
    def twoSum(self, nums, i):

        start = i + 1
        end = len(nums) - 1

        while start < end:
            
            addition = nums[start] + nums[end]
            if -nums[i] == addition:
                
                self.ans.append([nums[i], nums[start], nums[end]])

                prev = nums[start]
                while nums[start] == prev and start < end:
                    start += 1
            
            elif addition > -nums[i]:

                prev = nums[end]
                while nums[end] == prev and start < end:
                    end -= 1
            
            else:

                prev = nums[start]
                while nums[start] == prev and start < end:
                    start += 1
        