class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 == 1:
            return False
        
        target = target//2

        dp = {}
    
        def partition(i, target):   
            
            if target == 0:
                return True
            
            elif i == len(nums):
                return False
            
            if (i, target) in dp:
                return dp[(i, target)]
            
            else:
                dp[(i, target)] = partition(i + 1, target - nums[i]) or partition(i + 1, target)
                return dp[(i, target)]
        
        return partition(0, target)



        