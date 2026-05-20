class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        ans = True

        for pre in prerequisites:
            course, pre_req = pre[0], pre[1]

            adj[course].append(pre_req)
        
        def dfs(course):

            if visited[course] == 1:
                return False
            
            elif visited[course] == 2:
                return True

            elif adj[course] == []:
                return True
            
            else:
                visited[course] = 1

                for nei in adj[course]:
                    if not dfs(nei):
                        return False
                
                visited[course] = 2
                return True

        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):

                    return False
        
        return True
        

        