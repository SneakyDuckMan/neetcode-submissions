class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        self.root = TrieNode()
        self.ans = []

        def addWord(word):
            
            cur = self.root
            
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            
            cur.isEnd = True

        for word in words:
            addWord(word)

        def dfs(row, col, node, currStr):

            if row < 0 or row > len(board) - 1:
                return 
            
            elif col < 0 or col > len(board[0]) - 1:
                return
            
            elif (row, col) in visit or board[row][col] not in node.children:
                return
            
            node = node.children[board[row][col]]
            currStr.append(board[row][col])

            visit.add((row, col))

            if node.isEnd == True:
                node.isEnd = False
                foundWord = "".join(currStr)
                self.ans.append(foundWord)

            for r, c in [(1,0), (0,1), (-1,0), (0,-1)]:
                dfs(row + r, col + c, node, currStr)
            
            visit.remove((row, col))
            currStr.pop()

        for i in range(len(board)):
            for j in range(len(board[0])):
                visit = set()

                dfs(i, j, self.root, [])

        return self.ans
        
