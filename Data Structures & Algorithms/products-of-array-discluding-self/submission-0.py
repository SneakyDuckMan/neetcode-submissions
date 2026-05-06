class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)

        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        
        post_product = 1

        for i in range(len(nums) - 2, -1, -1):
            post_product *= nums[i+1]
            ans[i] *= post_product
        
        return ans