class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        ans = []
        
        def dfs(row, col, parent_height, ocean):
            
            if row < 0 or row > m - 1:
                return
            
            elif col < 0 or col > n - 1:
                return
            
            elif (row, col) in ocean:
                return
            
            elif parent_height > heights[row][col]:
                return

            ocean.add((row, col))

            for (r, c) in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(row + r, col + c, heights[row][col], ocean)
            
        for i in range(m):
            dfs(i, 0, 0, pacific)
            dfs(i, n - 1, 0, atlantic)
        
        for j in range(n):
            dfs(0, j, 0, pacific)
            dfs(m - 1, j, 0, atlantic)

        for coord in atlantic:
            if coord in pacific:
                x, y = coord
                ans.append([x, y])

        return ans