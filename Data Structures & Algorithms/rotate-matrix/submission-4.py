class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        def setBoundary(l, r):

            if r <= l:
                return

            for i in range(r - l):
                matrix[r - i][l], matrix[l][l+i] = matrix[l][l+i], matrix[r-i][l]
                matrix[r - i][l], matrix[r][r-i] = matrix[r][r-i], matrix[r-i][l]
                matrix[l+i][r], matrix[r][r-i] = matrix[r][r-i], matrix[l+i][r]
            
            setBoundary(l + 1, r - 1)
            
        setBoundary(0, len(matrix) - 1)

