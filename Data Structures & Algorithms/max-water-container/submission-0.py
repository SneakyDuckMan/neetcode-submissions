class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ans = 0

        start = 0
        end = len(heights) - 1

        while start < end:
            
            min_height = min(heights[start], heights[end])

            area = (end - start)* min_height
            ans = max(ans, area)

            if min_height == heights[end]:
                end -= 1
            
            elif min_height == heights[start]:
                start += 1
            
        return ans