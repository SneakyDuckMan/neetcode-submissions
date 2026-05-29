class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        l, r = 0, len(matrix[0]) - 1
        top, bot = 0, len(matrix) - 1

        while l <= r and top <= bot:
            for i in range(r - l + 1):
                ans.append(matrix[top][l + i])
            
            top += 1

            for i in range(bot - top + 1):
                ans.append(matrix[top + i][r])
            
            r -= 1

            if not (l <= r and top <= bot):
                break

            for i in range(r - l + 1):
                ans.append(matrix[bot][r - i])
            
            bot -= 1
            
            for i in range(bot - top + 1):
                ans.append(matrix[bot - i][l])
            
            l += 1
        

        return ans