class Solution:
    def reverseBits(self, n: int) -> int:
        arr = [0]*32
        for i in range(32):
            arr[i] = n & 1
            n = n >> 1

        ans = 0
        for bit in arr:
            ans = ans << 1
            ans += bit
        
        return ans