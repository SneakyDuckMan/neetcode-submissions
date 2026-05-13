class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        self.subset(nums, [], 0)

        return self.ans
    
    def subset(self, nums, curr_set,i):

        if i == len(nums):
            self.ans.append(curr_set.copy())
            return
        
        self.subset(nums, curr_set, i + 1)

        curr_set.append(nums[i])
        self.subset(nums, curr_set, i + 1)
        curr_set.pop()
