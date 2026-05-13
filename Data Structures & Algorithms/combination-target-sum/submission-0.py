class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        
        self.backtrack(nums, target, [], 0, 0)

        return self.ans
    
    def backtrack(self, nums, target, curr, curr_sum,i):
        
        if curr_sum == target:
            self.ans.append(curr.copy())
            return

        elif curr_sum > target or i == len(nums):
            return


        self.backtrack(nums, target, curr, curr_sum, i + 1)

        curr.append(nums[i])
        self.backtrack(nums, target, curr, curr_sum + nums[i], i)
        curr.pop()
        