class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] != 9:
            digits[-1] += 1

            return digits
        
        n = len(digits) - 1

        while digits[n] == 9:

            if n == 0:
                digits.append(0)
                digits[0] = 1
                return digits
            
            else:
                digits[n] = 0
                n -= 1

        digits[n] += 1
        
        return digits
        
