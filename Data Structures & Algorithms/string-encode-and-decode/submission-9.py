class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        
        return encoded_str

        
    def decode(self, s: str) -> List[str]:
        
        strs = []
        i = 0
        print(s)
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            string = s[j+1: j + size + 1]

            strs.append(string)
            i = j + size + 1
            

        return strs


