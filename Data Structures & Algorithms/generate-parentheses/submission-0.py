class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.gen(n, 0, 0, [])

        return self.ans

    def gen(self, n, op, cl, curr):

        if op + cl == 2*n:
            s = "".join(curr)
            self.ans.append(s)
            return
        
        if cl < op:
            curr.append(')')
            self.gen(n, op, cl + 1, curr)
            curr.pop()

            if op < n:
                curr.append('(')
                self.gen(n, op + 1, cl, curr)
                curr.pop()
        
        else:
            curr.append('(')
            self.gen(n, op + 1, cl, curr)
            curr.pop()
