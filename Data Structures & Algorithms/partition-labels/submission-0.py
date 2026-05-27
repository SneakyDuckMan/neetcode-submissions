class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        i = 0
        q = deque()
        count = Counter(s)
        ans = []
        print(count)

        while i < len(s):
            counts = 0
            q.append(s[i])
            while q:
                ele = q.popleft()

                while count[ele] != 0:

                    if count[s[i]] > 1:
                        q.append(s[i])
                    count[s[i]] -= 1
                    counts += 1
                    i += 1
            
            ans.append(counts)
        
        return ans