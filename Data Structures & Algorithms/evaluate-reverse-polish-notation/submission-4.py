class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == '+' or char == '-' or char == '*' or char == '/':
                op2 = stack.pop()
                op1 = stack.pop()
            
                if char == '+':
                    stack.append(op1 + op2)
                
                elif char == '-':
                    stack.append(op1 - op2)
                
                elif char == '*':
                    stack.append(op1*op2)
                
                elif char == '/':

                    stack.append(int(op1/op2))

                print(stack)
            else:
                stack.append(int(char))
        return stack[0]