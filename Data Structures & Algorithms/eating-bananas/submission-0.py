class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        ans = max(piles)

        start = 1
        end = ans

        while start <= end:
            time = 0
            speed = (start + end)//2

            for bananas in piles:
                time  += math.ceil(bananas/speed)
            
            if time <= h:
                ans = speed
                end = speed - 1
            
            else:
                start = speed + 1
        
        return ans
            

