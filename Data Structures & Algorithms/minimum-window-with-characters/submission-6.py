class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        found = 0

        window = [0, len(s)]
        l = 0

        for r in range(len(s)):

            if s[r] in countT:
                countT[s[r]] -= 1

                if countT[s[r]] == 0:
                    found += 1

                while found == len(countT):

                    if r - l < window[1] - window[0]:
                        window = [l, r]
                    
                    if s[l] in countT:
                        countT[s[l]] += 1

                        if countT[s[l]] == 1:
                            found -= 1
                    
                    l += 1
        
        if l == 0 and found != len(countT):
            return ""

        return s[window[0]: window[1] + 1]


