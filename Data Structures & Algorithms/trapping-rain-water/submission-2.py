class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_height_pos = 0

        for i in range(len(height)):
            if height[i] > height[max_height_pos]:
                max_height_pos = i 

        empty_space = [0]*len(height)

        start = 0
        end = len(height) - 1

        while start < end and height[start + 1] > height[start]:
            start += 1

        while start < end and height[end - 1] > height[end]:
            end -= 1

        curr_max_height = height[start]
        for i in range(start + 1, max_height_pos):

            if height[i] > curr_max_height:
                curr_max_height = height[i]
                continue
            
            empty_space[i] = curr_max_height - height[i]
        
        curr_max_height = height[end]
        for i in range(end - 1, max_height_pos, -1):

            if height[i] > curr_max_height:
                curr_max_height = height[i]
                continue
            
            empty_space[i] = curr_max_height - height[i]
        
        return sum(empty_space)
            



            
