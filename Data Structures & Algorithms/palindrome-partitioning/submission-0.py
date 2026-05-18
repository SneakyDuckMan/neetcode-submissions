class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []

        self.backtrack(s, 0, [])

        return self.ans
    
    def backtrack(self, s, i, curr):

        if i == len(s):
            self.ans.append(curr.copy())
        
        for j in range(i, len(s)):
            if self.isPali(s, i, j):
                substr = s[i: j + 1]

                curr.append(substr)
                self.backtrack(s, j + 1, curr)
                curr.pop()
            
    
    def isPali(self, s, i, j):
        l = i
        r = j

        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
        