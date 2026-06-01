class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = nums[0]
        maxP = nums[0]
        minP = nums[0]

        for num in nums[1:]:
            temp = maxP
            maxP = max(maxP*num, num, minP*num)
            minP = min(num, temp*num, num*minP)

            ans = max(maxP, ans)

        return ans