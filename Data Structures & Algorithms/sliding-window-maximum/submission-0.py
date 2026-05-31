class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q =  deque()
        
        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            
            q.append(i)
        
        ans.append(nums[q[0]])
        
        for i in range(k, len(nums)):

            if q[0] < i - k + 1:
                q.popleft()
            
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            
            q.append(i)

            ans.append(nums[q[0]])

        return ans
        
