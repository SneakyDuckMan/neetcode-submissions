class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.backtrack(candidates, target, [], 0, 0)

        return self.ans

    def backtrack(self, nums, target, curr, curr_sum, i):

        if curr_sum == target:
            self.ans.append(curr.copy())
            return
        
        elif curr_sum > target or i == len(nums):
            return
        
        curr.append(nums[i])
        self.backtrack(nums, target, curr, curr_sum + nums[i], i + 1)
        popped = curr.pop()

        while i != len(nums) and nums[i] == popped:
            i += 1

        self.backtrack(nums, target, curr, curr_sum, i)
