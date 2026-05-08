class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                continue
            
            if not stack:
                return False
            
            if char == ')':
                if stack[-1] != '(':
                    
                    return False
                stack.pop()

            elif char == ']':
                if stack[-1] != '[':
                    
                    return False
                stack.pop()

            elif char == '}':
                if stack[-1] != '{':
                    
                    return False
                stack.pop()
        
        if not stack:
            return True
        
        return False
                
            