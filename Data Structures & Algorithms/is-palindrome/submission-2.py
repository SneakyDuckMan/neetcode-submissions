class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s) - 1

        while start < end:
            
            while not self.alphanumeric(s[start]) and start < end:
                start += 1

            while not self.alphanumeric(s[end]) and start < end:
                end -= 1
            
            if s[start].lower() != s[end].lower():
                print(start, end)
                print(s[start], s[end])
                return False
            
            start += 1
            end -= 1 
        
        return True
    
    def alphanumeric(self, s):
        return (ord('A') <= ord(s) <= ord('Z') or
                ord('a') <= ord(s) <= ord('z') or
                ord('0') <= ord(s) <= ord('9'))
                