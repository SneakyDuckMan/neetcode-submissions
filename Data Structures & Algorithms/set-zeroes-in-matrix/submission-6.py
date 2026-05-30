class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n =  len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = float('inf')

        def setZeroRow(row, col):

            for j in range(n):
                if matrix[row][j] != float('inf'):
                    matrix[row][j] = 0

        def setZeroCol(row, col):
            for i in range(m):    
                matrix[i][col] = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    setZeroRow(i, j)
                    break
        
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == float('inf'):
                    setZeroCol(i, j)
                    break
        

