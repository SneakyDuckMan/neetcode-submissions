class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        self.ans = False
        
        self.find(word, self.root, 0)
        return self.ans

    def find(self, word, node, index):

        if self.ans == True:
            return

        cur = node

        for i in range(index, len(word)):

            if i == len(word) - 1:
                
                if word[i] == '.':
                    for child in cur.children.values():
                        if child.end == True:
                            self.ans = True
                            return

                elif word[i] in cur.children and cur.children[word[i]].end:
                    self.ans = True
                    return

                return

            if word[i] == '.':
            
                for child in cur.children.values():
                    self.find(word, child, i + 1)
                return
            
            elif word[i] not in cur.children:
                return
            
            else:
                cur = cur.children[word[i]]
        
        return


        
