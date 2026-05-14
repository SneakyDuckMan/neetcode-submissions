class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.ans = []

        if len(digits) == 0:
            return []
            
        self.backtrack(digits, [], 0)

        return self.ans

    def backtrack(self, digits, curr, i):
        
        if i == len(digits):
            s = "".join(curr)
            self.ans.append(s)
            return
        
        j = 1
        dig = self.corr_dig(int(digits[i]), j)

        while dig is not None:
            curr.append(dig)
            self.backtrack(digits, curr, i + 1)
            curr.pop()

            j += 1
            dig = self.corr_dig(int(digits[i]), j)




    def corr_dig(self, num, j):
        
        if num < 7 and j <= 3:
            return chr(ord('a') + (num-2)*3 - 1 + j)

        elif num == 7 and j <= 4:
            return chr(ord('o') + j)

        elif num == 8 and j <= 3:
            return chr(ord('s') + j)

        elif num == 9 and j <= 4:
            return chr(ord('v') + j)
        
        else:
            return None
