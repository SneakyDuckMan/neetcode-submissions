class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)

        for crs, preReq in prerequisites:
            adj[crs].append(preReq)
        
        visited = [0]*numCourses

        def dfs(course):

            if visited[course] == 1:
                return False
            
            elif visited[course] == 2 or adj[course] == []:
                return True
            
            visited[course] = 1

            for preReq in adj[course]:
                if dfs(preReq) == False:
                    return False
            
            visited[course] = 2

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True
            

