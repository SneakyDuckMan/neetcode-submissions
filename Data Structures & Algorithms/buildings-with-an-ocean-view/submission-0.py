class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        q = deque()
        q.append(len(heights) - 1)

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[q[0]]:
                q.appendleft(i)
        
        return list(q)
