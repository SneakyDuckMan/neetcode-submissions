class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ans = []
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visited = [0]*numCourses

        def dfs(crs):

            if visited[crs] == 1:
                return False
            
            elif visited[crs] == 2:
                return True
            
            elif adj[crs] == []:
                ans.append(crs)
                visited[crs] = 2

                return True
            
            visited[crs] = 1

            for pre in adj[crs]:
                if dfs(pre) == False:
                    return False
            
            ans.append(crs)
            visited[crs] = 2

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return ans
