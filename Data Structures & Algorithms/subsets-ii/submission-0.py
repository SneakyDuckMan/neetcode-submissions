class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()

        self.subset(nums, [], 0)

        return self.ans


    def subset(self, nums, curr, i):

        if i  == len(nums):
            self.ans.append(curr.copy())
            return
        
        curr.append(nums[i])
        self.subset(nums, curr, i + 1)
        curr.pop()

        i += 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
        
        self.subset(nums, curr, i)
