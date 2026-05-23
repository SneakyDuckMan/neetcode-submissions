class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s == "" or s[0] == '0':
            return 0

        ans = 1

        dp = [1]

        for i in range(1, len(s)):
            
            cur = int(s[i])
            prev = int(s[i - 1])

            if cur == 0:
                if prev == 0 or prev > 2:
                    return 0
                
                if i - 2 >= 0:
                    if s[i - 2] == '1' or s[i - 2] == '2':
                        ans -= dp[i - 2]
                
                dp.append(ans)
                continue

            if prev == 2:
                if cur <= 6:
                    ans += dp[i - 2]
                    
            if prev == 1:
                ans += dp[i - 2]
            
            dp.append(ans)

        return ans

