class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for i, h in enumerate(heights):
            if not stack:
                stack.append((h, i))
                continue
            
            prev_h, prev_i = stack[-1]
            
            if prev_h == h:
                continue
            
            elif prev_h < h:
                stack.append((h, i))
            
            else:

                while prev_h > h and stack:
                    pop_h, pop_i = stack.pop()
                    ans = max(ans, pop_h*(i - pop_i))

                    if stack:
                        prev_h, prev_i = stack[-1]
                
                stack.append((h, pop_i))
        
        while stack:
            h, i = stack.pop()
            ans = max(ans, h*(len(heights) - i))
        
        return ans



