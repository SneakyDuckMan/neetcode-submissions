class PrefixTree:

    def __init__(self):
        self.strset = set()
        

    def insert(self, word: str) -> None:
        self.strset.add(word)

    def search(self, word: str) -> bool:
        if word in self.strset:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        
        for word in self.strset:
            
            if len(word) < len(prefix):
                continue

            for i in range(len(prefix)):
                if word[i] != prefix[i]:
                    break
                
                elif i == len(prefix) - 1:
                    return True
            
        return False
        