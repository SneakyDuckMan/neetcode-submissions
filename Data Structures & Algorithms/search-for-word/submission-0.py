class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool: 
        m = len(board)
        n = len(board[0])
        path = set()
    
        def search(row, col, i):

            if i == len(word):
                return True
            
            if (row, col) in path:
                return False

            if row < 0 or row > m - 1:
                return False 
            
            elif col <  0 or col > n - 1:
                return False

            if board[row][col] == word[i]:
                path.add((row, col))

                for (row_add, col_add) in [(1,0), (0,-1), (-1,0), (0,1)]:
                    if search(row + row_add, col + col_add, i + 1):
                        return True
                path.remove((row,col))
            
            return False
        
        for i in range(m):
            for j  in range(n):
                if search(i, j, 0): return True
        
        return False
