class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_set = set(s)
        longest = {}
        ans = 0
        l = 0

        for i in range(len(s)):
            if s[i] not in longest:

                longest[s[i]] = i
                if i == len(s) - 1:
                    return max(ans, i - l + 1)

                continue

            else:
                ans = max(ans, i - l)
                new_l = longest[s[i]] + 1

                for j in range(l, new_l):
                    del longest[s[j]]

                longest[s[i]] = i
                l = new_l

        return ans


            

