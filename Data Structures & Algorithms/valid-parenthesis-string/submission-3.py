class Solution:
    def checkValidString(self, s: str) -> bool:
        max_open_brack = 0
        min_open_brack = 0

        for char in s:
            if char == '(':
                min_open_brack += 1
                max_open_brack += 1
            
            elif char == ')':
                max_open_brack -= 1
                min_open_brack -= 1
            
            else:
                max_open_brack += 1
                min_open_brack -= 1
            
            min_open_brack = max(min_open_brack, 0)

            if max_open_brack < 0:
                return False
        
        return min_open_brack == 0