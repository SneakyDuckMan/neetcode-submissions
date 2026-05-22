class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        self.ans = []

        for pre in prerequisites:
            course, pre_req = pre[0], pre[1]

            adj[course].append(pre_req)
        
        def dfs(course):

            if visited[course] == 1:
                return False
            
            elif visited[course] == 2:
                return True

            elif adj[course] == []:
                self.ans.append(course)
                visited[course] = 2
                return True
            
            else:
                visited[course] = 1

                for nei in adj[course]:

                    if dfs(nei) == False:
                        return False
                    
                    elif visited[nei] == 2:
                        self.ans.append(course)

                visited[course] = 2
                return True

        for course in range(numCourses):
            if visited[course] == 0:
                if dfs(course) == False:

                    return []
        
        return self.ans