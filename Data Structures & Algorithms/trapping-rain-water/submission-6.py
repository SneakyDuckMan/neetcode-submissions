class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0
        max_height_pos = 0

        for i in range(len(height)):
            if height[i] > height[max_height_pos]:
                max_height_pos = i 

        start = 0
        end = len(height) - 1

        curr_max_height = height[0]
        for i in range(max_height_pos):

            if height[i] > curr_max_height:
                curr_max_height = height[i]
                continue
            
            ans += curr_max_height - height[i]
        
        curr_max_height = height[len(height) - 1]
        for i in range(len(height) - 1, max_height_pos, -1):

            if height[i] > curr_max_height:
                curr_max_height = height[i]
                continue
            
            ans += curr_max_height - height[i]

        return ans