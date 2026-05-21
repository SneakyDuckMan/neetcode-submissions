class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par= [i for i in range(n + 1)]
        rank = [1]*(n + 1)

        def find_parent(n1):
            if par[n1] != n1:
                par[n1] = find_parent(par[n1])
            
            return par[n1]

        def union(n1, n2):

            p1, p2 = find_parent(n1), find_parent(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            
            return True
        
        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]