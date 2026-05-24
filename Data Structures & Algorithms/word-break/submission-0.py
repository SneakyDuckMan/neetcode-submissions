class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def wordCheck(i):

            if i == len(s):
                return True
            
            if i in dp:
                return dp[i]
            
            for word in wordDict:
                if i + len(word) > len(s):
                    continue
                
                else:
                    string = s[i: i + len(word)]
                    if string == word:
                        dp[i] =  wordCheck(i + len(word))

                        if dp[i] == True:
                            return True
                    
            return False if i not in dp else dp[i]
        
        return wordCheck(0)
            
            

