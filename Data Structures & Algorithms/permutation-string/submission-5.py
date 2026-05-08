class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = {}

        for char in s1:
            counts[char] = 1 + counts.get(char, 0)

        l = 0 
        r = len(s1) - 1

        if len(s2) < len(s1):
            return False
        
        while r < len(s2):
            i = l
            while i < r +1 and r < len(s2):

                if s2[i] in counts and counts[s2[i]] > 0:
                    counts[s2[i]] -= 1
                    if i == r:
                        print(l, r, counts)
                        return True
                
                elif s2[i] not in counts:
                    while l != i:
                        counts[s2[l]] += 1
                        l += 1
                        r += 1
                    l += 1
                    r += 1

                    break
                
                else:
                    while counts[s2[i]] == 0:
                        counts[s2[l]] += 1
                        l += 1
                        r += 1

                    counts[s2[i]] -= 1
                i +=1

        return False

