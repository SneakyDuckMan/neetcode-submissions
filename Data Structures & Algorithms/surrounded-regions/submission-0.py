class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m, n = len(board), len(board[0])

        def dfs1(row, col):

            if row < 0 or row > m - 1:
                return
            
            elif col < 0 or col > n - 1:
                return
            
            elif board[row][col] == 'X' or board[row][col] == '#':
                return
            
            board[row][col] = '#'

            for (r, c) in [(1,0), (0,1), (-1,0), (0,-1)]:
                dfs1(row + r, col + c)

        for i in range(m):
            dfs1(i, 0)
            dfs1(i, n - 1)
        
        for j in range(1, n):
            dfs1(0, j)
            dfs1(m - 1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        
        return