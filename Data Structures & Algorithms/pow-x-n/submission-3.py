class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(num, n):

            if n == 1:
                return num
            
            elif n == 0:
                return 1
            
            else:
                if n % 2 == 1:
                    h = pow(num, n//2)
                    return h*h*num
                
                else:
                    h = pow(num, n//2)
                    return h*h

        return pow(x, n) if n > 0 else 1/pow(x, -n)
