class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n =  len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = float('inf')

        def setZero(row, col):

            for i in range(m):
                if matrix[i][col] != float('inf'):
                    matrix[i][col] = 0

            for j in range(n):
                if matrix[row][j] != float('inf'):
                    matrix[row][j] = 0

            matrix[row][col] = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    setZero(i, j)
        
        
