class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        ans = ["JFK"]

        def dfs(node):
            if len(ans) == len(tickets) + 1:
                return True
            
            elif node not in adj:
                return False

            temp = list(adj[node])

            for i, nei in enumerate(temp):
                adj[node].pop(i)
                ans.append(nei)

                if dfs(nei):
                    return True
                
                adj[node].insert(i, nei)
                ans.pop()

            return False

        dfs("JFK")

        return ans
