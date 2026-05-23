class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans = ""

        for i in range(len(s)):

            l, r = i, i

            while l > -1 and r < len(s) and s[l] == s[r]:

                if len(ans) < r - l + 1:
                    ans = s[l:r + 1]

                l -= 1
                r += 1
        
        for i in range(len(s)):

            l, r = i, i + 1

            while l > -1 and r < len(s) and s[l] == s[r]:

                if len(ans) < r - l + 1:
                    ans = s[l:r + 1]

                l -= 1
                r += 1
        
        return ans