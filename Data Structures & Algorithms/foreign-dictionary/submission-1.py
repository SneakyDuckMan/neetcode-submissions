class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        vertices = []

        for word in words:
            for s in word:
                if s not in vertices:
                    vertices.append(s)
        
        adj = {}

        for v in vertices:
            adj[v] = []
        
        def first_diff_letter(s1, s2): 

            if len(s1) <= len(s2):

                for i in range(len(s1)):
                    if s1[i] != s2[i]:
                        return i
            
                return -1
            
            else:
                for i in range(len(s2)):
                    if s1[i] != s2[i]:
                        return i
                
                return -2
        
        for curr in range(1, len(words)):

            index = first_diff_letter(words[curr - 1], words[curr])

            if index == -1:
                continue
            
            elif index == -2:
                return ""
            
            small, large = words[curr - 1][index], words[curr][index]

            adj[large].append(small)

        visited = {}

        for v in vertices:
            visited[v] = 0

        self.ans = ""

        def dfs(v):

            if visited[v] == 1:
                print('this', v)
                return False

            elif visited[v] == 2:
                return True
            
            visited[v] = 1

            if adj[v] == []:
                self.ans += v
                visited[v] = 2
                return True

            else:
                for nei in adj[v]:
                    
                    if not dfs(nei):
                        return False

                self.ans += v
                visited[v] = 2
                
                return True

        for v in vertices:
            if not dfs(v):
                return ""

        return self.ans